l_name = input("Please Enter your last Name: ")
f_name = input("Please Enter your first Name: ")
age = input("Enter your age: ")
con_num = input("Enter your contact Number: ")
course = input("Enter your Course: ")

print("=====================================")
lines = "Last Name:{}\nFirst Name:{}\nAge:{}\nContact Number:{}\nCourse:{}"
f = open("TF2/students.txt", "w")
f.writelines(lines.format(l_name, f_name, age, con_num, course))
print("Student information has been saved to 'students.txt'.")
f.close()