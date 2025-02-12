file_handle = open("Technical Midterm Exam/numbers.txt", 'r')
content_lines = file_handle.readlines()
file_handle.close()

for index, line_content in enumerate(content_lines, 1):
    digits = [item.strip() for item in line_content.strip().split(',')]
    
    if all(digit.isdigit() for digit in digits):
        converted_numbers = [int(digit) for digit in digits]
        sum_of_numbers = sum(converted_numbers)
        status = "Palindrome" if str(sum_of_numbers) == str(sum_of_numbers)[::-1] else "Not a palindrome"
        print(f"Line {index}: {line_content.strip()} (sum {sum_of_numbers}) - {status}")
    else:
        print(f"Line {index}: {line_content.strip()} - Contains invalid data")
