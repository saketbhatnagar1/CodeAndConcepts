# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("Inhale, Exhale")


# class Fish(Animal):
#     def __init__(self):
#         super().__init__() #super() allows the child class to call the parent class’s method.

    
#     def swim(self):   
#         print("Moving in Water. ")

# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)



# # 📌 Types of Inheritance in Python
# # ✅ 1. Single Inheritance

# # One child → one parent

# # class A: ...
# # class B(A): ...

# # ✅ 2. Multilevel Inheritance

# # Child → parent → grandparent

# # class A: ...
# # class B(A): ...
# # class C(B): ...

# # ✅ 3. Multiple Inheritance

# # Child inherits from multiple parents

# # class A: ...
# # class B: ...
# # class C(A, B): ...

# # ✅ 4. Hierarchical Inheritance

# # Multiple children → same parent

# # class A: ...
# # class B(A): ...
# # class C(A): ...
# 4
#Super is a funciton used in child class to call methods from a parent class(superclass)
#Allows you to extend the functionality of the inherited methods
class Shape:
    def __init__(self,color,is_filled,peremeter):
        self.color = color
        self.is_filled = is_filled
        self.peremeter = peremeter
class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

class square(Shape):
    def __init__(self,width,color,is_filled):
        super().__init__(color,is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,width,height,color,is_filled,peremetre):
        super().__init__(color,is_filled,peremeter=0)
        self.width = width
        self.height= height


circle = Circle(color="Blue",is_filled=False,radius=5)
tringle = Triangle(color="Red",is_filled=False,height=10,width=10)
print(tringle.perimeter)