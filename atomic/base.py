
from functools import total_ordering

from cffi import FFI


class FFIWrapper:
    """ A class that wraps an FFI functions for atomic integers
    """

    def __init__(self, type_name):
        self.__type_name = type_name

        self.__ffi = FFI()
        self.__ffi.cdef("""
            void store(%s *, %s *);
            %s add_and_fetch(%s *, %s);
            %s sub_and_fetch(%s *, %s);
            %s get_and_set(%s *v, %s n);
            %s compare_and_set(%s *v, %s *e, %s n);
        """ % ((self.__type_name,) * 15))

        self.__ffi_implementation = self.__ffi.verify(
            """
            void store(%s *v, %s *n){__atomic_store(v, n, __ATOMIC_SEQ_CST);}
            %s add_and_fetch(%s *v, %s i){return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);}
            %s sub_and_fetch(%s *v, %s i){return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);}
            %s get_and_set(%s *v, %s n){return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);}
            %s compare_and_set(%s *v, %s *e, %s n){
                return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
            }
            """ % ((self.__type_name,) * 15)
        )

    def new(self, value=None):
        return self.__ffi.new('%s *' % self.__type_name, value)

    def store(self, old_value, new_value):
        self.__ffi_implementation.store(old_value, new_value)

    def add_and_fetch(self, value, inc):
        self.__ffi_implementation.add_and_fetch(value, inc)

    def sub_and_fetch(self, value, dec):
        self.__ffi_implementation.sub_and_fetch(value, dec)

    def get_and_set(self, old_value, new_value):
        return self.__ffi_implementation.get_and_set(old_value, new_value)

    def compare_and_set(self, old_value, expected_value, new_value):
        return self.__ffi_implementation.compare_and_set(old_value, expected_value, new_value)


__ffi_declarations__ = {
    x: FFIWrapper(x) for x in (
        'short', 'unsigned short',
        'int', 'unsigned int',
        'long', 'unsigned long',
        'long long', 'unsigned long long'
    )
}


@total_ordering
class AtomicBase(object):
    """
    A basic atomic class that guarantees atomic updates to its contained integer value.
    """

    def __init__(self, type_name, value=None):
        """
        Creates a new Atomic integer with the given initial value.
        :param type_name: a name of integer type like 'long' or 'unsigned short'
        :param value: initial value
        """
        self.__ffi_declaration = __ffi_declarations__[type_name]
        self._value = self.__ffi_declaration.new(value)

    @property
    def value(self):
        return self._value[0]

    @value.setter
    def value(self, new):
        self.__ffi_declaration.store(self._value, self.__ffi_declaration.new(new))

    def __repr__(self):
        return '<{0} at 0x{1:x}: {2!r}>'.format(
            self.__class__.__name__, id(self), self.value)

    def __iadd__(self, inc):
        self.__ffi_declaration.add_and_fetch(self._value, inc)
        return self

    def __isub__(self, dec):
        self.__ffi_declaration.sub_and_fetch(self._value, dec)
        return self

    def get_and_set(self, new_value):
        """Atomically sets to the given value and returns the old value

        :param new_value: the new value
        """
        return self.__ffi_declaration.get_and_set(self._value, new_value)

    def swap(self, new_value):
        return self.get_and_set(new_value)

    def compare_and_set(self, expect_value, new_value):
        """
        Atomically sets the value to the given value if the current value is
        equal to the expected value.

        :param expect_value: the expected value
        :param new_value: the new value
        """
        return bool(self.__ffi_declaration.compare_and_set(self._value, self.__ffi_declaration.new(expect_value), new_value))

    def compare_and_swap(self, expect_value, new_value):
        return self.compare_and_set(expect_value, new_value)

    def __eq__(self, a):
        if self is a:
            return True
        elif isinstance(a, self.__class__):
            return self.value == a.value
        else:
            return self.value == a

    def __ne__(self, a):
        return not (self == a)

    def __lt__(self, a):
        if self is a:
            return False
        elif isinstance(a, self.__class__):
            return self.value < a.value
        else:
            return self.value < a


class AtomicArrayBase(object):
    """
    A basic atomic class that guarantees atomic updates to its contained integer values.
    """

    def __init__(self, atomic_cls, array=None):
        """
        Creates a new AtomicLongArray with the given initial array of integers.

        :param atomic_cls:
        :param array: initial values
        """

        if issubclass(atomic_cls, AtomicBase) is False:
            raise TypeError('Invalid atomic class was specified')

        self.__atomic_cls = atomic_cls
        self._array = [self.__atomic_cls(x) for x in array] if array is not None else []

    def __repr__(self):
        return '<{0} at 0x{1:x}: {2!r}>'.format(
            self.__class__.__name__, id(self), self.value)

    def __len__(self):
        return len(self._array)

    def __getitem__(self, key):
        return self._array[key]

    def __setitem__(self, key, value):
        if isinstance(value, self.__atomic_cls):
            self._array[key] = value
        else:
            self._array[key].value = value

    def __iter__(self):
        for a in self._array:
            yield a.value

    @property
    def value(self):
        return [a.value for a in self._array]

    @value.setter
    def value(self, new=None):
        self._array = [self.__atomic_cls(int(x)) for x in new] if new is not None else []
