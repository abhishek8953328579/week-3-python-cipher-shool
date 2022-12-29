def multiply(*args):
    print(args)

names=["Abhishek","kamlesh","raju","roshan","Aman thekedar"]
multiply(multiply(names))
multiply(multiply(*names))
# * will take every element of list as a argument in function
# where nums will take whole list as a single argument
