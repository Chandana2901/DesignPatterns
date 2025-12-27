# when only 1 instance of a class has to be created

class Test:
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Test, cls).__new__(cls, *args, **kwargs)
        return cls._instance

t1 = Test()
t2 = Test()

print(t1 is t2) 