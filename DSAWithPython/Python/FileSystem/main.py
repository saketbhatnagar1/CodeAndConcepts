import os
# print(os.getcwd())
# File = open("myfile.txt")
# contents = File.read()
# print(contents)

with open("myfile.txt",mode="w") as f:
    f.write("Hello after reading")

your_name = input("Please Enter Your Name")
with open("myfile.txt",mode="a") as f:
    f.write(f"Hello {your_name} your stupid name is appended in the file")
with open("myfile.txt",mode="r") as f:
    contents = f.read()
    print(contents)
