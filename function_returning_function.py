def outer_func(msg):
    def inner_func():
        print(f"you are Abhishek maurya Abhishek {msg}")
    return inner_func
var=outer_func("jhjhjh")
print(var())
