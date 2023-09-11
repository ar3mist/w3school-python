#7. Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java
#Output : java

# Answer

name = input("Enter the file name with the extension :")

f_extension = name.split(".")

print("The extension of the file is : " + (f_extension[-1]))
