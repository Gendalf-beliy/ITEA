class Stack:
    """
    Stack realization by principe Last In - First Out (LIFO)
    """

    class LimitExceedError(Exception):
        """Exception raised for errors in the input, when user try to push new element over stack limit.
            Attributes:
                message -- explanation of the error
            """

        def __init__(self, message):
            self.message = message

    class TypeError(Exception):

        def __init__(self):
            self.message = "You are trying to push inappropriate data type to stack"

    class EmptyStackError(Exception):
        def __init__(self):
            self.message = "Stack is empty"


    def __init__(self, data_type=object, limit=None):
        self.storage = []
        self.data_type = data_type
        self.limit = limit
        self.length = 0

    def _push(self, new):
        if self.data_type != type(new):
            raise self.TypeError("Stack type: {}, you are trying to push {} type".format(self.data_type, type(new)))

        if len(self.storage) >= self.limit:
            raise self.LimitExceedError("Stack overflow")

    def push(self, new):
        self._push(new)
        self.storage.append(new)

    def pull(self):
        if len(self.storage) == 0:
            raise self.EmptyStackError()
        return self.storage.pop()

    def count(self):
        return len(self.storage)

    def clear(self):
        self.storage = []

    @property
    def type(self):
        return self.data_type

    def __str__(self):
        return "Stack<{}>".format(self.data_type)


n = Stack(int, 10)
n.push(1)
n.pull()
n.pull()