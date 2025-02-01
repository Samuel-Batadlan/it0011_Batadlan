text = input("Please Enter a String:")

vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0
space_count = 0
others_count = 0

for char in text:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1
    elif char == " ":
        space_count += 1
    else:
        others_count += 1

print("Vowels: ", vowels_count)
print("Consonants: ", consonants_count)    
print("Space: ", space_count)  
print("Other characters: ", others_count)


