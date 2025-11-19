# with open("a_file.txt") as file:
#     file.read()

#types=>KeyError,indexError,FileNotFound,TypeError

#EXCEPTION HANDLING=> try,except,else,finally

try:
    file = open("a_file.txt")
except:
    open("a_file.txt","w")
