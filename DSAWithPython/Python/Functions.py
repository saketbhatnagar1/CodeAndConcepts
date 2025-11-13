def format_name(fname,lname):
    """Function To Format First and Lastname""" #""" """ comments in """ """ allow us to write the documentation and description of the function
    if fname == "" or lname == "":
        return "Please Provide FirstName and Lastname"
    else:
        formatted_fname = fname.title()
        formatted_lname = lname.title()
    return f"{formatted_fname} {formatted_lname}"
 
name = format_name("SAKET","BHATNAGAR")
print(name)