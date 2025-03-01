student_data = []
file_name = "student_records.txt"

while True:
    print("\nMenu:")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("11. Exit")
    
    user_choice = input("Enter choice: ")
    
    if user_choice == "1":
        try:
            with open(file_name, "r") as file:
                student_data = [tuple(line.strip().split(",")) for line in file]
            print("Records loaded successfully!")
        except FileNotFoundError:
            print("File not found.")
    
    elif user_choice == "2":
        with open(file_name, "w") as file:
            for student in student_data:
                file.write(",".join(student) + "\n")
        print("Records saved.")
    
    elif user_choice == "3":
        file_name = input("Enter new filename: ")
        with open(file_name, "w") as file:
            for student in student_data:
                file.write(",".join(student) + "\n")
        print("Saved as", file_name)
    
    elif user_choice == "4":
        for student in student_data:
            final_grade = 0.6 * float(student[3]) + 0.4 * float(student[4])
            print(f"ID: {student[0]} | Name: {student[1]} {student[2]} | Grade: {final_grade:.2f}")
    
    elif user_choice == "5":
        student_data.sort(key=lambda student: student[2])
        print("Sorted by last name.")
    
    elif user_choice == "6":
        student_data.sort(key=lambda student: 0.6 * float(student[3]) + 0.4 * float(student[4]), reverse=True)
        print("Sorted by grade.")
    
    elif user_choice == "7":
        search_id = input("Enter Student ID: ")
        for student in student_data:
            if student[0] == search_id:
                print(student)
                break
        else:
            print("Not found.")
    
    elif user_choice == "8":
        student_id = input("Enter 6-digit Student ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_score = input("Class Standing: ")
        exam_score = input("Major Exam: ")
        student_data.append((student_id, first_name, last_name, class_score, exam_score))
        print("Record added.")
    
    elif user_choice == "9":
        student_id = input("Enter Student ID: ")
        for i in range(len(student_data)):
            if student_data[i][0] == student_id:
                first_name = input("New First Name: ")
                last_name = input("New Last Name: ")
                class_score = input("New Class Standing: ")
                exam_score = input("New Major Exam: ")
                student_data[i] = (student_id, first_name, last_name, class_score, exam_score)
                print("Updated.")
                break
        else:
            print("Not found.")
    
    elif user_choice == "10":
        student_id = input("Enter Student ID: ")
        student_data = [student for student in student_data if student[0] != student_id]
        print("Deleted.")
    
    elif user_choice == "11":
        break
    
    else:
        print("Invalid choice.")
