X = 'Spam'


def func():
    global X
    X = 'NI'
    print(X)


def func1():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)


func()
func1()
