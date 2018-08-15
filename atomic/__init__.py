
from atomic.base import AtomicBase, AtomicArrayBase


class AtomicShort(AtomicBase):
    """
    An atomic class that stores integer value as a "short"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicShort with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'short', value=value)


class AtomicUShort(AtomicBase):
    """
    An atomic class that stores integer value as an "unsigned short"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicUShort with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'unsigned short', value=value)


class AtomicInt(AtomicBase):
    """
    An atomic class that stores integer value as an "int"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicInt with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'int', value=value)


class AtomicUInt(AtomicBase):
    """
    An atomic class that stores integer value as an "unsigned int"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicUInt with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'short', value=value)


class AtomicLong(AtomicBase):
    """
    An atomic class that stores integer value as a "long"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicShort with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'long', value=value)


class AtomicULong(AtomicBase):
    """
    An atomic class that stores integer value as an "unsigned long"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicULong with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'unsigned long', value=value)


class AtomicLongLong(AtomicBase):
    """
    An atomic class that stores integer value as a "long long"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicLongLong with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'long long', value=value)


class AtomicULongLong(AtomicBase):
    """
    An atomic class that stores integer value as an "unsigned long long"
    This class guarantees atomic updates to its contained integer value.
    """

    def __init__(self, value=None):
        """
        Creates a new AtomicULongLong with the given initial value.

        :param value: initial value
        """
        AtomicBase.__init__(self, 'unsigned long long', value=value)


class AtomicShortArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("short" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicShort, array=array)


class AtomicUShortArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("unsigned short" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicUShort, array=array)


class AtomicIntArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("int" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicInt, array=array)


class AtomicUIntArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("unsigned int" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicUInt, array=array)


class AtomicLongArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("long" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicLong, array=array)


class AtomicULongArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("unsigned long" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicULong, array=array)


class AtomicLongLongArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("long long" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicLongLong, array=array)


class AtomicULongLongArray(AtomicArrayBase):
    """
    An atomic class that guarantees atomic updates to its contained integer values ("unsigned long" type integers).
    """
    def __init__(self, array=None):
        AtomicArrayBase.__init__(self, AtomicULongLong, array=array)
