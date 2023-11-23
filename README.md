# Database Interaction with PostgreSQL and Application Programming:
# Students Table Supporting Application 
DEMO VIDEO: https://www.loom.com/share/b7cfc89cb5fc47f7b42113ca5fb6a1de?sid=c075be63-65f9-46a9-8e0a-c5db9b859c3c

## Setup Instructions:
**Prerequisites**
As a prerequisite, this application is python-based and makes use of [psycopg2](https://pypi.org/project/psycopg2/) and Python. If you havent, you can install psycopg2 using: pip install psycopg2
Equally, if you do not have python installed, that can be done by downloading from [here] (https://www.python.org/downloads/)

**How to run the application:**
1. Navigate to the correct directory. You should be in "3005"
2. Open your command line/terminal interface and enter: python3 app.py
3. A command line interface will pop up, continue to follow the instructions given there to operate the functions
and make changes to the table Students.

**Brief Explanation of Functions**

- deleteHelper() - takes input and passes them to deleteStudent()
- deleteStudent() - deletes a student record by a specified student_id, retrieved by the helper function
- updateStudentHelper() - takes input and passes them to updateStudentEmail()
- updateStudentEmail() - updates a student email by a specified student_id, retrieved by the helper function
- getStudentInfoForAddStudent() - takes input and passes them to addStudent()
- updateStudentEmail() - adds a student by a specified fields, retrieved by the helper function
- endSession() - raises exception to exit looping the interface
- getAllStudents() - retrieves and displays all records in the Students table
- main() - prints the main interface instructions and calls other functions
- create_students_table() - creates a students table from this application but per the instructions is commented out and currently not needed.
