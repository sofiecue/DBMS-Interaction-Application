import psycopg2

try:
    # initialize connection object
    connection = psycopg2.connect(database = "a4", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

    # cursor is our tool to executes queries connection on db
    cursor = connection.cursor()

    print("PostgreSQL server connection to database A4 information:")
    print(connection.get_dsn_parameters(), "\n")

    # takes input and passes them to deleteStudent()
    def deleteHelper():
        selected_sid = input("Enter a student id to remove that student: ")
        deleteStudent(selected_sid)
    
    # Deletes the record of the student with the specified student_id
    def deleteStudent(student_id):
        delete_student_sql = f"DELETE FROM students WHERE student_id = {student_id};"
        cursor.execute(delete_student_sql)
        connection.commit()
        print("Student removed successfully.")
        print("Updated table:")
        getAllStudents();

    # takes input and passes them to updateStudentEmail()
    def updateStudentHelper():
        selected_sid = input("Enter the student id of the student whose email field requires updating: ")
        new_email = input("Enter new email address for student: ")
        updateStudentEmail(selected_sid, new_email)

    # Updates the email address for a student with the specified student_id
    def updateStudentEmail(student_id, new_email):
        update_student_email_sql = f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id};"
        cursor.execute(update_student_email_sql)
        connection.commit()
        print("Email updated successfully.")
        print("Updated table:")
        getAllStudents();

        # helper for addStudent. Gets the necessary information for a student to be added
    def getStudentInfoForAddStudent():
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        email = input("Enter student's email: ")
        enrollment_date = input("Enter student's date of enrollment in form YYYY-MM-DD: ")
        addStudent(first_name, last_name, email, enrollment_date)

    # addStudent: accurately inserts new records
    def addStudent(first_name, last_name, email, enrollment_date):
        add_student_sql = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');"
        cursor.execute(add_student_sql)
        connection.commit()

        print("Student added to students table successfully.")
        print("Updated table:")
        getAllStudents()

    # kicks user out of session, ends CL interface
    def endSession():
        raise Exception;

        # getAllStudents: correctly retrieves and displays records
    def getAllStudents():
        cursor.execute("SELECT * FROM students;")
        records = cursor.fetchall()

        connection.commit()
        # loops through all records to display on each line
        for record in records:
            print(record)
        return;

    def main():
        print("Welcome to the CRUD application for managing the students table!")
        choice = input("Pick one of the following actions to perform: \n0. Exit session \n1. Display all student records \n2. Add new student record \n3. Update a student email \n4. Delete a student \n")
        while (choice != 0):

            if choice =="1":
                getAllStudents()
                choice = input("Pick one of the following actions to perform: \n0. Exit session \n1. Display all student records \n2. Add new student record \n3. Update a student email \n4. Delete a student \n")

            elif choice =="2":
                getStudentInfoForAddStudent()
                choice = input("\nPick one of the following actions to perform: \n0. Exit session \n1. Display all student records \n2. Add new student record \n3. Update a student email \n4. Delete a student \n")
            elif choice =="3":
                updateStudentHelper()
                choice = input("\nPick one of the following actions to perform: \n0. Exit session \n1. Display all student records \n2. Add new student record \n3. Update a student email \n4. Delete a student \n")
            elif choice =="4":
                deleteHelper()
                choice = input("\nPick one of the following actions to perform: \n0. Exit session \n1. Display all student records \n2. Add new student record \n3. Update a student email \n4. Delete a student \n")
            elif choice =="0":
                endSession();

    main()

    # additional code optional for creating table - since it's not in the specs I commented it out for assignment scope
    # def create_students_table():
    #             # creates table
    #     cursor.execute("""CREATE TABLE students
    #     (student_id SERIAL, 
    #         first_name	TEXT NOT NULL, 
    #         last_name TEXT NOT NULL,
    #         email TEXT UNIQUE NOT NULL,
    #         enrollment_date DATE DEFAULT CURRENT_DATE,
    #         PRIMARY KEY (student_id));
    #                 """)
        
    #     # commit table creation to db
    #     connection.commit()
    #     print("Students table created successfully. ")


except (Exception) as e:
    print("Some error occurred while attempting to connect to PostgreSQL", e)

finally:
    if (1):
        #close everything when done
        cursor.close()
        connection.close()
        exit()


