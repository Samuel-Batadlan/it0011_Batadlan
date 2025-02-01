user_input = input ("Please Enter some Strings: ")

digit_sum = 0

for char in user_input:
    if char.isdigit():
        digit_sum += int(char)
    
print("Sum of Digits: ", digit_sum)