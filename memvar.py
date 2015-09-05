class MemVar(object):

    def __init__(self):
        self._x = None
        self._memory = list()
        self._position = 0

    def position(self, i):
        if i < 0:
            raise Exception("Position {0} is less than zero".format(i))
        elif i > len(self._memory-1):
            raise Exception("Position {0} is too far".format(i))
        else:
            self._position = i
			return self

    @property
    def x(self):
        return self._memory[self._position]

    @x.setter
    def x(self, value):
        self._memory.append(self._x)
        self._x = value
