numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

#COMPREHENSION

new_list_1 = [item+1 for item in numbers]
print(new_list_1)

name = "SAKET"
words_in_name = [letter for letter in name]
print(words_in_name)

doubled = [number*2 for number in range(1,5)]
print(doubled)

#Conditional Comprehension
new_names = ["Alex","Beth","Dave","Elanor","Freddie","caroline"]
short_name = [name for name in new_names if len(name)<5]
print(short_name)
long_names = [name.upper() for name in new_names if len(name)>4]
print(long_names)

###############DictionaryComprehension##############
import random
# new_dict = {new_key:new_value ofr item in iterable(either a list,dictionary,string,range etc)}
names = ["Alex","Beth","Dave","Elanor","Freddie","caroline"]
student_score = [random.randint(1,100) for _  in range(len(names)) ]
print(student_score)
# student_data = {name: score for name, score in zip(names, student_score)}

student_data = {student:random.randint(1,100) for student in names}
print(student_data)

passed_students = {
    student:score for (student,score) in student_data.items() if score>=60
}
print(f"passed students : {passed_students}")

'''
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   

Try Googling to find out how to convert a sentence into a list of words.  *

*Do NOT** Create a dictionary directly.

Try to use Dictionary Comprehension instead of a Loop. 



To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
'''

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = { word:len(word) for word in sentence.split()}
#Iterating over pandas dataframe:
student_dict = {
    "students" : ["student1","student2","student3"],
    "score":[56,76,98]
}

#LOOP THROUGH:

for (key,value) in student_dict.items():
    print(key)


#ITER ROWS:

for (index,row) in student_dict.iterrows():
    print(row)#row.COLUMNNAME will give that row 