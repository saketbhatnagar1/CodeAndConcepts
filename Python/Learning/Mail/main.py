#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Fetch The Names




def fetchName():
    with open("Input/Names/invited_names.txt") as names_list:
        names = names_list.readlines()
#Copy The Letter and paste the names
    for i in range(len(names)):
        with open("Input/Letters/starting_letter.txt") as letter:
            sample_letter = letter.read()
            new_letter = sample_letter.replace("[name]",names[i])
            print(new_letter)
        with open(f"Output/ReadyToSend/letter{i}.txt","w") as letter:
            letter1 = letter.write(new_letter)
fetchName()

