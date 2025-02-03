f_name = input("Please Enter your first Name: ")
l_name = input("Please Enter your last Name: ")
age = input("Enter your age: ")

print("=====================================")
print("Full Name: " + f_name + " " + l_name)

sliced_name = f_name[0:3]
print("Sliced Name: ", sliced_name)

txt = "Greeting Message: Hello {}! Welcome. You are {} years old."
print(txt.format(sliced_name, age))

