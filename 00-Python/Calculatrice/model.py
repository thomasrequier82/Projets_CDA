class MyScreenModel:
    """
    MyScreenModel class is a data model implementation. The model stores
    the values of the variables. The model provides an
    interface through which to work with stored values. The model contains
    methods for registration, deletion and notification observers.

    The model is (primarily) responsible for the logic of the application.
    MyScreenModel class task is to add two numbers.
    """

    def __init__(self):
        self._c = 0
        self._d = 0
        self._sum = 0
        self._observers = []

    @property
    def c(self):
        return self._c

    @property
    def d(self):
        return self._d

    @property
    def sum(self):
        return self._sum

    @c.setter
    def c(self, value):
        self._c = value
        self._sum = self._c + self._d
        self.notify_observers()

    @d.setter
    def d(self, value):
        self._d = value
        self._sum = self._c + self._d
        self.notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()
