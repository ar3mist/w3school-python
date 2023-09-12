#Write a Python program to get a newly-generated string from a given string where "Is" has been
# added to the front. Return the string unchanged if the given string already begins with "Is".

# answer

def new_string(txt):

    if len(txt) >= 2 and txt[:2] == "IS":
        return txt

    return "IS" + txt

print(new_string("Array"))
print(new_string("ISstring "))

