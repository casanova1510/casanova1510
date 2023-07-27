def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "Fail"


def main():
    while True:
        try:
            marks = float(input("Enter the marks obtained by the student (0 to 100): "))
            if not 0 <= marks <= 100:
                print("Invalid input. Please enter marks between 0 and 100.")
                continue

            grade = calculate_grade(marks)
            print(f"The grade for the student is: {grade}")
        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")
        finally:
            choice = input("Do you want to calculate the grade for another student? (yes/no): ")
            if choice.lower() != "yes":
                break


if __name__ == "__main__":
    main()
