x = 5
def func():
    global x
    print(x)
    x = 10
    print(x)
func()