def add (*args):
    print(type(args)) #<class 'tuple'>
add(2,3,4,1)

#**kwargs allows to add many arguments
def calculate(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    print(kwargs)# {'add': 5, 'subtract': 90}
calculate(add=5,subtract=90)
