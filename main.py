def load_data():
    """Load in student data"""
    with open("students.txt", "r") as student_data:
        for line in student_data:
            data = line.split()
    student1 = {'Name': 'Haythen', 'StudentID': '1234567', 'Credits': '35', 'GPA': '2.45'}
    student2 = {'Name': 'Dilip', 'StudentID': '2345678', 'Credits': '20', 'GPA': '1.39'}
    student3 = {'Name': 'Shama', 'StudentID': '3456789', 'Credits': '22', 'GPA': '2.14'}
    student4 = {'Name': 'Fances', 'StudentID': '4567890', 'Credits': '35', 'GPA': '2.45'}
    student5 = {'Name': 'Alistair', 'StudentID': '5678901', 'Credits': '80', 'GPA': '0.53'}
    student6 = {'Name': 'Pallavi', 'StudentID': '6789012', 'Credits': '65', 'GPA': '2.45'}
    student7 = {'Name': 'Manu', 'StudentID': '7890123', 'Credits': '20', 'GPA': '1.90'}
    student8 = {'Name': 'Pavan', 'StudentID': '8901234', 'Credits': '100', 'GPA': '0.81'}
    student9 = {'Name': 'Manika', 'StudentID': '1212121', 'Credits': '20', 'GPA': '2.46'}
    student10 = {'Name': 'Chris', 'StudentID': '3334444', 'Credits': '89', 'GPA': '3.38'}
    student11 = {'Name': 'John', 'StudentID': '2121212', 'Credits': '90', 'GPA': '2.09'}
    student12 = {'Name': 'Stuart', 'StudentID': '9999888', 'Credits': '100', 'GPA': '2.02'}
    all_students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10, student11, student12]
    return all_students
#This reads all the student data in, puts each into a dictionary, and then puts those dictionaries into a list.
def print_menu():
    """Print to command line menu"""
    print("Hello!, What would you like to do?")
    a = input("Add a student?: ")
    if a == "yes":
        newstudent = {}
        all_students.append(student)
    b = input("Find masters students?: ")
    if b = "yes":
        if 'Credits' in ("students.txt") >25: print("Name")
    c = input("Find students on probation?: ")
    if c == "yes":
        if 'GPA' in ("students.ext") <2.0: print("Name")
    d = input("Find honors students?: ")
    if d == "yes":
        if 'GPA' in ("students.txt") >3.0: print("Name")
#This asks the user what they would like to do in the program.
def main(load_data)
    prompt = "What would you like to do? "
    while print_menu() = True
    input(prompt)
#This is supposed to give the user a prompt that would only work if print_menu function was working.

#I would like to apologize to you Dr. Santore for anything not finished in this project, I am submitting it now because I wont have access to it tonight as im working late.
#I couldn't get a good grip on the functions, im hoping the dictionaries work right. I think missing the last class really got me.
#I should've asked for help earlier but for some reason I am scared to and this is a consequence of that terrible quality, hope you have a good evening.

