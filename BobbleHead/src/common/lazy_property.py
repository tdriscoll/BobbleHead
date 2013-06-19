class LazyProperty(object):
    """ A property that only is calculated the first time it is called """
    
    def __init__(self, calculate_function):
        self._calculate = calculate_function

    def __get__(self, obj, klass):
        value = self._calculate(obj)
        setattr(obj, self._calculate.func_name, value)
        return value