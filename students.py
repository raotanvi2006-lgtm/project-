# students.py

def calculate_average(marks):
    # ... your logic here ...
    return sum(marks) / len(marks)

def placement_eligibility(avg):
    return avg >= 40

def get_student_details():
    name = input("Enter student name: ")
    # ... rest of logic ...

# this prevents running on import
if __name__ == "__main__":
    student = get_student_details()
