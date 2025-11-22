# with open("a_file.txt") as file:
#     file.read()

#types=>KeyError,indexError,FileNotFound,TypeError

#EXCEPTION HANDLING=> try,except,else,finally

try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("something")
finally:
    print("EXECUTES WHEN NONE OF THE CRITERIAN ARE MT")

