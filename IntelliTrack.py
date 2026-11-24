import mysql.connector
from datetime import date

DB_CONFIG = {
    'host': "localhost",
    'user': "root",                                                                                                                                       
    'passwd': "Kaizen",
    'database': "intellitrack"}

def connect_db():
    try:
        Myconn = mysql.connector.connect(**DB_CONFIG)
        return Myconn
    except mysql.connector.Error as err:
        print(f"\n❌ Connection Failed! Error: {err}")
        print("Please ensure MySQL is running, the database 'Intellitrack' exists, and credentials are correct.")
        return None

def homepage():
    while True:
        print("\n=====================================")
        print("    🏫 WELCOME TO INTELLITRACK SYSTEM   ")
        print("=====================================")
        print("1. 🔐 Login")
        print("2. 🚪 Exit")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            role, username = login()

            if role == "Admin":
                admin_dashboard()
            elif role == "Faculty":
                faculty_dashboard()
    
            elif role == "Student":
                student_dashboard()
            
            elif role is None: 
                print("❌ Login failed! Please try again.")

        elif choice == "2":
            ch = input("Are You Sure You Want To Close The Program (Yes/No): ").lower()
            if ch == "yes":
                print("\n👋 Thank you for using IntelliTrack!")
                print("Exiting... Goodbye!\n")
                break
            elif ch == "no":
                continue 
            else:
                print("⚠️ Invalid choice. Returning to menu.")

        else:
            print("⚠️ Invalid choice. Please enter 1 or 2.")
            
def login():
    conn = connect_db()
    if conn is None:return None, None
    cur = conn.cursor()
    
    print("\n==== 🔐 LOGIN PAGE ====")
    username = input("Username: ")
    password = input("Password: ")

    try:
        sql = "SELECT Role, Password FROM LOGIN WHERE Username = %s"
        cur.execute(sql, (username,))
        result = cur.fetchone()
        cur.fetchall() 
        
        if result:
            role = result[0]
            db_password = result[1]
            
            if password == db_password: 
                print(f"✅ {role} login successful!")
                return role, username 
            else:
                print("❌ Invalid password!")
                return None, None
        else:
            print("❌ Invalid username!")
            return None, None
    
    except Exception as e:
        print(f"An error occurred during login: {e}")
        return None, None
    
    finally:
        cur.close()
        conn.close()

def admin_dashboard():
    while True:
        print("\n=====================================")
        print("👑 ADMIN DASHBOARD: MAIN MENU")
        print("=====================================")
        print("1. 🎓 Student Management (STUDENTS)")
        print("2. 👨‍🏫 Faculty Management (FACULTY)")
        print("3. 📝 Marks Management (MARKS)")
        print("4. ✅ Attendance Management (ATTENDANCE)")
        print("5. 💰 Fees Management (FEES)")
        print("6. 📅 Timetable Management (TIMETABLE)")
        print("7. 📚 Library Management (LIBRARY)")
        print("0. 🚪 Logout")
        print("=====================================")
        
        choice = input("Enter choice (0-7): ")

        if choice == "1": student_menu()
        elif choice == "2": faculty_menu()
        elif choice == "3": marks_menu()
        elif choice == "4": attendance_menu()
        elif choice == "5": fees_menu()
        elif choice == "6": timetable_menu()
        elif choice == "7": library_menu()
        elif choice == "0":
            print("👋 Logging out from Admin Dashboard...")
            break
        else:
            print("❌ Invalid choice.")

def student_menu():
    while True:
        print("\n==== 1. STUDENT MANAGEMENT ====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Delete Student (Full Record Removal)")
        print("4. Update Student Record")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": delete_student()
        elif choice == "4": update_student() 
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def faculty_menu():
    while True:
        print("\n==== 2. FACULTY MANAGEMENT ====")
        print("1. Add New Faculty")
        print("2. View All Faculty")
        print("3. Delete Faculty Record")
        print("4. Update Faculty Record")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == "1": add_faculty()
        elif choice == "2": view_faculty()
        elif choice == "3": delete_faculty()
        elif choice == "4": update_faculty_record()
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def marks_menu():
    while True:
        print("\n==== 3. MARKS MANAGEMENT ====")
        print("1. Record Student Marks (Add)")
        print("2. Delete Student Marks Sub-Menu")
        print("3. Update Mark Record")
        print("4. Display Marks ")
        print("5. Generate School-wide Marks Report")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1": add_marks()
        elif choice == "2": delete_marks()
        elif choice == "3": update_marks()
        elif choice == "4": view_marks_by_student()
        elif choice == "5": get_school_marks_report()
        elif choice == "0": break
        else: print("❌ Invalid choice.")
        
def attendance_menu():
    while True:
        print("\n==== 4. ATTENDANCE MANAGEMENT ====")
        print("1. Record Daily Attendance (Add)")
        print("2. View Attendance Summary (by Student ID)")
        print("3. View Class Attendance Report")
        print("4. Update Attendance Record")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == "1": record_attendance()
        elif choice == "2": 
            sid = input("Enter Student ID for summary: ")
            view_attendance_summary(sid)
        elif choice == "3": view_class_attendance_summary()
        elif choice == "4": update_attendance_record()
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def fees_menu():
    while True:
        print("\n==== 5. FEES MANAGEMENT ====")
        print("1. Record Fee Payment (Add New)")
        print("2. View Fee Status (by Student ID)")
        print("3. Update Fee Payment Record")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == "1": record_fee_payment()
        elif choice == "2": 
            sid = input("Enter Student ID to view fee status: ")
            view_fee_status(sid)
        elif choice == "3": update_fee_payment()
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def timetable_menu():
    while True:
        print("\n==== 6. TIMETABLE MANAGEMENT ====")
        print("1. Add Timetable Entry")
        print("2. View Timetable (Filter by Class)")
        print("3. Update Timetable Entry")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == "1": add_timetable_entry()
        elif choice == "2": view_timetable()
        elif choice == "3": update_timetable_entry()
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def library_menu():
    while True:
        print("\n==== 7. LIBRARY MANAGEMENT ====")
        print("1. Issue Book")
        print("2. Return Book (Close Issue Record)")
        print("3. View Overdue Book Returns")
        print("4. Update Issued Book Record")
        print("5. View All Issued Books (Sorted by Class)")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == "1": issue_book()
        elif choice == "2": return_book()
        elif choice == "3": view_pending_returns()
        elif choice == "4": update_issued_book()
        elif choice == "5": view_issued_books_by_class()
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def faculty_dashboard():
    faculty_id = input("\n👨‍🏫 Enter your Faculty ID to access your dashboard: ") 
    try:
        fid = int(faculty_id)
    except ValueError:
        print("❌ Invalid ID format. Please enter a number.")
        return

    while True:
        print("\n=====================================")
        print(f"👨‍🏫 FACULTY DASHBOARD: ID {fid}")
        print("=====================================")
        print("1. 📝 Academic Record Management")
        print("2. 🔍 Information & Reports")
        print("0. 🚪 Logout")
        print("=====================================")
        
        choice = input("Enter choice (0-2): ")

        if choice == "1": academic_management_menu()
        elif choice == "2": info_and_reports_menu(fid)
        elif choice == "0":
            print("👋 Logging out from Faculty Dashboard...")
            break
        else:
            print("❌ Invalid choice.")

def academic_management_menu():
    while True:
        print("\n==== 1. ACADEMIC RECORD MANAGEMENT ====")
        print("1. Record New Student Marks")
        print("2. Update Existing Student Marks")
        print("3. Record Daily Attendance")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == "1": add_marks()
        elif choice == "2": update_marks()
        elif choice == "3": record_attendance()
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def info_and_reports_menu(fid):
    while True:
        print("\n==== 2. INFORMATION & REPORTS ====")
        print("1. View My Profile & Info")
        print("2. View My Assigned Timetable")
        print("3. Generate Full Student Academic Report")
        print("4. View Marks Breakdown (by Student ID)")
        print("5. View Attendance Summary (by Student ID)")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")
        
        if choice == "1": view_faculty_profile(fid)
        elif choice == "2": view_faculty_timetable(fid)
        elif choice == "3": get_student_report()
        elif choice == "4": view_marks_by_student()
        elif choice == "5": 
            sid = input("Enter Student ID for attendance summary: ")
            view_attendance_summary(sid)
        elif choice == "0": break
        else: print("❌ Invalid choice.")

def student_dashboard():
    student_id=input("\n‍🎓 Enter your Student ID to access your dashboard: ")  
    try:
        sid = int(student_id)
    except ValueError:
        print("❌ Invalid ID format.")
        return
    
    while True:
        print("\n==== 👨‍🎓 STUDENT DASHBOARD ====")
        print(f"Viewing records for Student ID: {sid}") 
        print("1. View My Attendance Summary")
        print("2. View My Fee Status")
        print("3. View My Marks Breakdown")
        print("4. View My Issued Books")
        print("0. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_attendance_summary(sid)
        elif choice == "2":
            view_fee_status(sid)
        elif choice == "3":
            view_marks_by_student(sid)
        elif choice == "4":
            view_issued_books_by_student(sid)
        elif choice == "0":
            print("👋 Logging out...")
            break
        else:
            print("❌ Invalid choice.")

def add_student():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Add New Student ---")
    try:
        a = int(input("Enter The Student_ID: "))
        b = input("Enter The Name: ")
        c = int(input("Enter The Adm_No: "))
        d = input("Enter The DOB (YYYY-MM-DD): ")
        e = input("Enter The Class: ")
        f = input("Enter The Section: ")
        g = input("Enter The Aadhar No: ")
        h = input("Enter The Contact_No: ")
        i = input("Enter The Email: ")
        
        sql = "INSERT INTO STUDENTS VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (a, b, c, d, e, f, g, h, i))
        conn.commit()
        print("✅ Student added successfully!")
    except Exception as e:
        print(f"❌ Error adding student: {e}")
    finally:
        cur.close()
        conn.close()

def view_students():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM STUDENTS")
    data = cur.fetchall()
    
    print("\n--- Full Student List ---")
    if not data:
        print("No student records found.")
        return
        
    for i in data:
        print(f"ID: {i[0]}, Name: {i[1]}, Adm_No: {i[2]}, Class: {i[4]}-{i[5]}, Contact: {i[7]}")
    
    cur.close()
    conn.close()

def delete_student():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    sid = input("Enter Student ID to delete (WARNING: Deletes all related data): ")
    
    try:
        cur.execute("SELECT Student_ID FROM STUDENTS WHERE Student_ID = %s", (sid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Student ID {sid} not found. Deletion aborted.")
            return

        print("  -> Deleting related ATTENDANCE records...")
        cur.execute("DELETE FROM ATTENDANCE WHERE Student_ID = %s", (sid,))
        
        print("  -> Deleting related MARKS records...")
        cur.execute("DELETE FROM MARKS WHERE Student_ID = %s", (sid,))
        
        print("  -> Deleting related FEES records...")
        cur.execute("DELETE FROM FEES WHERE Student_ID = %s", (sid,))
        
        print("  -> Deleting related LIBRARY records...")
        cur.execute("DELETE FROM LIBRARY WHERE Student_ID = %s", (sid,))
        
        print("  -> Deleting student record...")
        cur.execute("DELETE FROM STUDENTS WHERE Student_ID = %s", (sid,))
        
        conn.commit()
        print(f"✅ Student ID {sid} and all related academic records have been successfully deleted.")

    except Exception as e:
        print(f"❌ Error deleting student: {e}")
    finally:
        cur.close()
        conn.close()

def update_student():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    print("\n--- 📝 Comprehensive Update Student Record ---")
    try:
        sid = input("Enter the Student_ID of the record to update: ")
        sql_select = "SELECT Name, Adm_No, DOB, Class, Section, Aadhar_No, Contact, Email FROM STUDENTS WHERE Student_ID = %s"
        cur.execute(sql_select, (sid,))
        record = cur.fetchone()
        if record is None:
            print(f"❌ ERROR: Student ID {sid} not found. Update aborted.")
            return
        current_data = list(record)
        print("\n--- Current Data for Student ID {} ---".format(sid))
        print("Name: {}, Adm_No: {}, Class: {}-{}".format(
            current_data[0], current_data[1], current_data[3], current_data[4]
        ))
        print("DOB: {}, Contact: {}, Email: {}".format(
            current_data[2], current_data[6], current_data[7]
        ))
        
        print("\n--- Enter NEW Values (Must provide new value for ALL fields) ---")
        new_name = input("Enter NEW Name: ")
        new_adm_no_str = input("Enter NEW Admission No: ")
        new_dob = input("Enter NEW DOB (YYYY-MM-DD): ")
        new_class = input("Enter NEW Class: ")
        new_section = input("Enter NEW Section: ")
        new_aadhar = input("Enter NEW Aadhar No: ")
        new_contact = input("Enter NEW Contact No: ")
        new_email = input("Enter NEW Email: ")
        try:
            new_adm_no = int(new_adm_no_str)
        except ValueError:
            print("❌ Invalid input. Admission Number must be a valid number. Update aborted.")
            return
        sql_update = """
        UPDATE STUDENTS SET 
            Name = %s, Adm_No = %s, DOB = %s, Class = %s, Section = %s, 
            Aadhar_No = %s, Contact = %s, Email = %s 
        WHERE Student_ID = %s
        """
        update_values = (
            new_name, new_adm_no, new_dob, new_class, new_section, 
            new_aadhar, new_contact, new_email, sid
        )
        
        cur.execute(sql_update, update_values)
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"\n✅ Student record (ID {sid}) successfully updated. New Name: '{new_name}'.")
        else:
            print("⚠️ Warning: Record found, but no changes were made (all new values were the same as the old ones).")

    except Exception as e:
        print(f"❌ Error updating student record: {e}")
    finally:
        cur.close()
        conn.close()


def add_faculty():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Add New Faculty ---")
    try:
        fid = int(input("Enter The Faculty_ID: "))
        name = input("Enter The Name: ")
        subject = input("Enter The Main Subject: ")
        contact = input("Enter The Contact_No: ")
        exp = int(input("Enter Years of Experience: "))

        sql = "INSERT INTO FACULTY VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (fid, name, subject, contact, exp))
        conn.commit()
        print("✅ Faculty added successfully!")
    except Exception as e:
        print(f"❌ Error adding faculty: {e}")
    finally:
        cur.close()
        conn.close()

def view_faculty():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM FACULTY")
    data = cur.fetchall()
    
    print("\n--- Faculty List ---")
    if not data:
        print("No faculty records found.")
        return
        
    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}, Contact: {row[3]}, Experience: {row[4]} yrs")
    
    cur.close()
    conn.close()

def delete_faculty():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    fid = input("Enter Faculty ID to delete (WARNING: Deletes related Timetable data): ")
    
    try:
        cur.execute("SELECT Faculty_ID FROM FACULTY WHERE Faculty_ID = %s", (fid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Faculty ID {fid} not found. Deletion aborted.")
            return

        print("  -> Deleting related TIMETABLE entries...")
        cur.execute("DELETE FROM TIMETABLE WHERE Faculty_ID = %s", (fid,))
        
        print("  -> Deleting faculty record...")
        cur.execute("DELETE FROM FACULTY WHERE Faculty_ID = %s", (fid,))
        
        conn.commit()
        print(f"✅ Faculty ID {fid} and all related timetable records have been successfully deleted.")

    except Exception as e:
        print(f"❌ Error deleting faculty: {e}")
    finally:
        cur.close()
        conn.close()

def update_faculty_record():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 📝 Update Faculty Record ---")
    try:
        fid = input("Enter the Faculty_ID of the record to update: ")
        
        cur.execute("SELECT Name, Subject, Contact FROM FACULTY WHERE Faculty_ID = %s", (fid,))
        record = cur.fetchone()
        if record is None:
            print(f"❌ ERROR: Faculty ID {fid} not found. Update aborted.")
            return

        print(f"Current Record: Name: {record[0]}, Subject: {record[1]}, Contact: {record[2]}")
        
        new_name = input("Enter NEW Name: ")
        new_subject = input("Enter NEW Main Subject: ")
        new_contact = input("Enter NEW Contact Number: ")
        new_exp = int(input("Enter NEW Years of Experience: "))

        sql = "UPDATE FACULTY SET Name = %s, Subject = %s, Contact = %s, Experience = %s WHERE Faculty_ID = %s"
        cur.execute(sql, (new_name, new_subject, new_contact, new_exp, fid))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"✅ Faculty record (ID {fid}) successfully updated. New Name: '{new_name}'.")
        else:
            print("⚠️ Warning: Record found, but no changes were made (values were the same).")

    except ValueError:
        print("❌ Invalid input. Please ensure Years of Experience is a number.")
    except Exception as e:
        print(f"❌ Error updating faculty record: {e}")
    finally:
        cur.close()
        conn.close()

def view_faculty_profile(fid):
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    try:
        sql = "SELECT Name, Subject, Contact, Experience FROM FACULTY WHERE Faculty_ID = %s"
        cur.execute(sql, (fid,))
        profile = cur.fetchone()
        
        print(f"\n--- Your Faculty Profile ---")
        if profile:
            name, subject, contact, experience = profile
            print(f"👤 Name: {name}")
            print(f"🆔 Faculty ID: {fid}")
            print(f"📚 Subject Expertise: {subject}")
            print(f"📞 Contact Number: {contact}")
            print(f"⭐ Experience (Years): {experience}")
        else:
            print(f"❌ Error: Your Faculty ID {fid} was not found in the database.")

    except Exception as e:
        print(f"❌ Error viewing profile: {e}")
    finally:
        cur.close()
        conn.close()

def view_faculty_timetable(fid):
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    try:
        sql = "SELECT Course, Day, Time_Slot, Subject FROM TIMETABLE WHERE Faculty_ID = %s ORDER BY Day, Time_Slot"
        cur.execute(sql, (fid,))
        data = cur.fetchall()
        
        print(f"\n--- Assigned Timetable for Faculty ID: {fid} ---")
        if not data:
            print("No classes currently assigned to you.")
            return
            
        for row in data:
            print(f"Course: {row[0]} | Day: {row[1]} | Time: {row[2]} | Subject: {row[3]}")
            
    except Exception as e:
        print(f"❌ Error viewing timetable: {e}")
    finally:
        cur.close()
        conn.close()

def add_marks():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Enter Student Marks ---")
    try:
        sid = int(input("Enter Student_ID: "))
        subject = input("Enter Subject Name: ")
        marks = float(input("Enter Marks Obtained: "))

        cur.execute("SELECT Student_ID FROM STUDENTS WHERE Student_ID = %s", (sid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Student ID {sid} not found in the STUDENTS database. Cannot record marks.")
            return

        sql = "INSERT INTO MARKS (Student_ID, Subject, Marks_Obtained) VALUES (%s, %s, %s)"
        cur.execute(sql, (sid, subject, marks))
        conn.commit()
        print(f"✅ Marks for {subject} successfully recorded for Student ID {sid}.")
        
    except ValueError:
        print("❌ Invalid input. Please enter valid numbers for Student ID and Marks.")
    except Exception as e:
        print(f"❌ Error adding marks: {e}")
    finally:
        cur.close()
        conn.close()

def delete_marks():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 🗑️ Delete Student Mark Record ---")
    try:
        sid = int(input("Enter Student ID to delete marks for: "))
        subject = input("Enter Subject Name (e.g., Computer Science): ")

        cur.execute("SELECT Mark_ID FROM MARKS WHERE Student_ID = %s AND Subject = %s", (sid, subject))
        if cur.fetchone() is None:
            print(f"❌ ERROR: No marks found for Student ID {sid} in {subject}. Deletion aborted.")
            return

        sql = "DELETE FROM MARKS WHERE Student_ID = %s AND Subject = %s"
        cur.execute(sql, (sid, subject))
        conn.commit()
        
        print(f"✅ Marks for Student ID {sid} in {subject} successfully deleted.")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number for Student ID.")
    except Exception as e:
        print(f"❌ Error deleting marks: {e}")
    finally:
        cur.close()
        conn.close()
        
def update_marks():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 📝 Update Existing Student Marks ---")
    try:
        sid = int(input("Enter Student ID to update marks for: "))
        subject = input("Enter Subject to update: ")
        new_marks = float(input("Enter NEW Marks Obtained: "))

        cur.execute("SELECT * FROM MARKS WHERE Student_ID = %s AND Subject = %s", (sid, subject))
        if cur.fetchone() is None:
            print(f"❌ ERROR: No existing marks found for Student ID {sid} in {subject}. Cannot update.")
            return

        sql = "UPDATE MARKS SET Marks_Obtained = %s WHERE Student_ID = %s AND Subject = %s"
        cur.execute(sql, (new_marks, sid, subject))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"✅ Marks successfully updated for Student {sid} in {subject} to {new_marks}.")
        else:
            print(f"⚠️ Warning: No changes were made.")

    except ValueError:
        print("❌ Invalid input. Please enter valid numbers for ID and Marks.")
    except Exception as e:
        print(f"❌ Error updating marks: {e}")
    finally:
        cur.close()
        conn.close()


def get_school_marks_report():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    print("\n" + "=" * 60)
    print("        🏫 SCHOOL-WIDE MARKS PERFORMANCE REPORT 📊")
    print("=" * 60)
    try:
        sql_report = """
        SELECT
            s.Class,
            s.Section,
            COUNT(DISTINCT s.Student_ID) AS Total_Students,
            AVG(m.Marks_Obtained) AS Avg_Class_Marks
        FROM
            STUDENTS s
        JOIN 
            MARKS m ON s.Student_ID = m.Student_ID
        GROUP BY
            s.Class, s.Section
        ORDER BY 
            s.Class, s.Section;
        """
        cur.execute(sql_report)
        report_data = cur.fetchall()
        
        if not report_data:
            print("❌ No marks records found across the entire school to generate a report.")
            return

        print(f"{'CLASS':<8} | {'SECTION':<8} | {'TOTAL STUDENTS':<15} | {'AVG MARKS':<10}")
        print("-" * 60)
        
        for class_name, section, total_students, avg_marks in report_data:
            print(f"{class_name:<8} | {section:<8} | {total_students:<15} | {avg_marks:.2f}")

        print("=" * 60)

    except Exception as e:
        print(f"❌ Error generating school report: {e}")
    finally:
        cur.close()
        conn.close()


def view_marks_by_student(student_id=None):
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    if student_id is None:
        try:
            sid = int(input("Enter The Student_ID To View Marks: "))
        except ValueError:
            print("❌ Invalid input. Student ID must be a number.")
            return
    else:
        try:
            sid = int(student_id)
        except ValueError:
            print(f"❌ Internal error: Passed ID '{student_id}' is not a valid number.")
            return
    print(f"\n--- Marks for Student ID: {sid} ---")
    
    try:
        sql = "SELECT Subject, Marks_Obtained FROM MARKS WHERE Student_ID = %s"
        cur.execute(sql, (sid,))
        marks_data = cur.fetchall()
        if marks_data:
            total_marks = 0
            count = 0
            
            for subject, marks in marks_data:
                print(f"  - {subject}: {marks}")
                total_marks += marks
                count += 1
                
            print("-" * 25)
            print(f"  Total Subjects: {count}")
            print(f"  Average Score:  {total_marks / count:.2f}")

        else:
            print(f"⚠️ No marks records found for Student ID: {sid}.")
            
    except Exception as e:
        print(f"❌ Error viewing marks: {e}")
        
    finally:
        cur.close()
        conn.close()
        
def get_student_report():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    sid = input("Enter Student ID for Full Academic Report: ")
    
    try:
        cur.execute("SELECT Name, Class, Section FROM STUDENTS WHERE Student_ID = %s", (sid,))
        student_info = cur.fetchone()
        
        if not student_info:
            print(f"❌ ERROR: Student ID {sid} not found in the database. Cannot generate report.")
            return

        print("\n==============================================")
        print(f"  📝 ACADEMIC REPORT FOR: {student_info[0].upper()}")
        print(f"  ID: {sid} | Class: {student_info[1]}-{student_info[2]}")
        print("==============================================")
        
        print("\n--- MARKS BREAKDOWN ---")
        cur.execute("SELECT Subject, Marks_Obtained FROM MARKS WHERE Student_ID = %s", (sid,))
        marks_data = cur.fetchall()
        total_marks = 0
        
        if marks_data:
            for subject, marks in marks_data:
                print(f"  > {subject.ljust(15)}: {marks}")
                total_marks += marks
            print(f"  > Average Score: {(total_marks / len(marks_data)):.2f}")
        else:
            print("  No marks records available.")
            
        print("\n--- ATTENDANCE STATUS ---")
        cur.execute("SELECT COUNT(*) FROM ATTENDANCE WHERE Student_ID = %s", (sid,))
        total_days = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM ATTENDANCE WHERE Student_ID = %s AND Status = 'Present'", (sid,))
        present_days = cur.fetchone()[0]
        
        if total_days > 0:
            percentage = (present_days / total_days) * 100
            print(f"  Total Days Tracked: {total_days}")
            print(f"  Days Present: {present_days}")
            print(f"  Attendance Percentage: {percentage:.2f}%")
        else:
            print("  No attendance records available.")
            
    except Exception as e:
        print(f"❌ Error generating report: {e}")
    finally:
        cur.close()
        conn.close()


def record_attendance():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Record Student Attendance ---")
    try:
        sid = int(input("Enter Student_ID: "))
        date_str = input(f"Enter Date (YYYY-MM-DD, default today: {date.today()}): ") or str(date.today())
        status = input("Enter Status (P/A/L): ").upper()
        
        cur.execute("SELECT Student_ID FROM STUDENTS WHERE Student_ID = %s", (sid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Student ID {sid} not found in the STUDENTS database. Cannot record attendance.")
            return

        status_map = {'P': 'Present', 'A': 'Absent', 'L': 'Leave'}
        if status not in status_map:
            print("❌ Invalid status. Must be P, A, or L.")
            return

        sql = "INSERT INTO ATTENDANCE (Student_ID, Date, Status) VALUES (%s, %s, %s)"
        cur.execute(sql, (sid, date_str, status_map[status]))
        conn.commit()
        print(f"✅ Attendance recorded as {status_map[status]} for Student {sid} on {date_str}.")
    except Exception as e:
        print(f"❌ Error recording attendance: {e}")
    finally:
        cur.close()
        conn.close()

def update_attendance_record():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 📝 Update Attendance Record ---")
    try:
        sid = input("Enter Student ID: ")
        date_str = input("Enter Date of Attendance to update (YYYY-MM-DD): ")
        
        cur.execute("SELECT Status FROM ATTENDANCE WHERE Student_ID = %s AND Date = %s", (sid, date_str))
        record = cur.fetchone()
        if record is None:
            print(f"❌ ERROR: No attendance record found for Student ID {sid} on {date_str}. Cannot update.")
            return

        current_status = record[0]
        print(f"Current Status: {current_status}")
        
        new_status_abbr = input("Enter NEW Status (P/A/L): ").upper()
        status_map = {'P': 'Present', 'A': 'Absent', 'L': 'Leave'}
        
        if new_status_abbr not in status_map:
            print("❌ Invalid status. Must be P, A, or L. Update aborted.")
            return

        new_status = status_map[new_status_abbr]

        sql = "UPDATE ATTENDANCE SET Status = %s WHERE Student_ID = %s AND Date = %s"
        cur.execute(sql, (new_status, sid, date_str))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"✅ Attendance for Student {sid} on {date_str} successfully updated to '{new_status}'.")
        else:
            print("⚠️ Warning: Record found, but no changes were made (new status was the same as the old one).")

    except Exception as e:
        print(f"❌ Error updating attendance record: {e}")
    finally:
        cur.close()
        conn.close()

def view_attendance_summary(sid):
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    sid_str = str(sid) 

    print(f"\n--- 📊 Attendance Summary for Student ID: {sid_str} ---")

    try:

        cur.execute("SELECT Name FROM STUDENTS WHERE Student_ID = %s", (sid_str,))
        student_name = cur.fetchone()
        if student_name is None:
            print(f"❌ ERROR: Student ID {sid_str} not found in the STUDENTS database.")
            return
        
        print(f"Name: {student_name[0]}")


        sql_total = "SELECT COUNT(*) FROM ATTENDANCE WHERE Student_ID = %s"
        cur.execute(sql_total, (sid_str,))
        total_days = cur.fetchone()[0]


        sql_present = "SELECT COUNT(*) FROM ATTENDANCE WHERE Student_ID = %s AND Status = 'Present'"
        cur.execute(sql_present, (sid_str,))
        present_days = cur.fetchone()[0]

        sql_absent = "SELECT COUNT(*) FROM ATTENDANCE WHERE Student_ID = %s AND Status = 'Absent'"
        cur.execute(sql_absent, (sid_str,))
        absent_days = cur.fetchone()[0]

        sql_leave = "SELECT COUNT(*) FROM ATTENDANCE WHERE Student_ID = %s AND Status = 'Leave'"
        cur.execute(sql_leave, (sid_str,))
        leave_days = cur.fetchone()[0]

        if total_days > 0:
            percentage = (present_days / total_days) * 100
            print("-" * 35)
            print(f"Total Days Tracked: {total_days}")
            print(f"Days Present:      {present_days}")
            print(f"Days Absent:       {absent_days}")
            print(f"Days on Leave:     {leave_days}")
            print("-" * 35)
            print(f"Attendance Percentage: {percentage:.2f}%")
        else:
            print(f"⚠️ No attendance records found for Student ID: {sid_str}.")
            
    except Exception as e:
        print(f"❌ Error generating attendance summary: {e}")
    finally:
        cur.close()
        conn.close()

def view_class_attendance_summary():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 📋 Class Attendance Report ---")
    
    target_class = input("Enter Class Name (e.g., 10): ")
    target_section = input("Enter Section (e.g., A): ")
    
    try:
        sql_report = """
        SELECT
            s.Student_ID,
            s.Name,
            COUNT(CASE WHEN a.Status = 'Present' THEN 1 END) AS Present_Days,
            COUNT(a.Status) AS Total_Days_Tracked
        FROM
            STUDENTS s
        LEFT JOIN
            ATTENDANCE a ON s.Student_ID = a.Student_ID
        WHERE
            s.Class = %s AND s.Section = %s
        GROUP BY
            s.Student_ID, s.Name
        ORDER BY
            s.Student_ID;
        """
        cur.execute(sql_report, (target_class, target_section))
        report_data = cur.fetchall()
        
        print(f"\nReport for Class {target_class}-{target_section}:")
        print("=" * 60)
        
        if not report_data:
            print(f"❌ No student or attendance records found for Class {target_class}-{target_section}.")
            return

        print(f"{'ID':<5} | {'NAME':<20} | {'PRESENT DAYS':<15} | {'TOTAL TRACKED':<15} | {'PERCENTAGE':<10}")
        print("-" * 60)
        
        for sid, name, present_days, total_days in report_data:
            percentage = (present_days / total_days * 100) if total_days > 0 else 0.00
            print(f"{sid:<5} | {name:<20} | {present_days:<15} | {total_days:<15} | {percentage:.2f}%")

        print("=" * 60)

    except Exception as e:
        print(f"❌ Error generating class attendance report: {e}")
    finally:
        cur.close()
        conn.close()

def record_fee_payment():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Record Fee Payment ---")
    try:
        sid = int(input("Enter Student_ID: "))
        paid = float(input("Enter Amount Paid: "))
        pending = float(input("Enter Remaining Pending Amount: "))
        date_str = input(f"Enter Payment Date (YYYY-MM-DD, default today: {date.today()}): ") or str(date.today())
        
        cur.execute("SELECT Student_ID FROM STUDENTS WHERE Student_ID = %s", (sid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Student ID {sid} not found in the STUDENTS database. Cannot record payment.")
            return

        sql = "INSERT INTO FEES (Student_ID, Amount_Paid, Pending_Amount, Date) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (sid, paid, pending, date_str))
        conn.commit()
        print(f"✅ Payment of {paid} recorded for Student {sid}. Pending: {pending}.")
    except Exception as e:
        print(f"❌ Error recording payment: {e}")
    finally:
        cur.close()
        conn.close()

def view_fee_status(sid):
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    try:
        cur.execute("SELECT SUM(Amount_Paid), SUM(Pending_Amount) FROM FEES WHERE Student_ID = %s", (sid,))
        result = cur.fetchone()
        
        total_paid = result[0] if result[0] is not None else 0
        total_pending = result[1] if result[1] is not None else 0

        print(f"\n--- Fee Status for Student ID: {sid} ---")
        
        if total_paid == 0 and total_pending == 0:
            cur.execute("SELECT Student_ID FROM STUDENTS WHERE Student_ID = %s", (sid,))
            if cur.fetchone() is None:
                print(f"❌ ERROR: Student ID {sid} not found in the database.")
                return
            else:
                print("No fee records found for this student.")
                return

        print(f"Total Paid So Far: ₹{total_paid:.2f}")
        print(f"Total Pending Amount: ₹{total_pending:.2f}")

        if total_pending > 0:
            print("⚠️ ACTION REQUIRED: Pending fee amount detected.")
        else:
            print("✅ All Fees Cleared.")

    except Exception as e:
        print(f"❌ Error viewing fee status: {e}")
    finally:
        cur.close()
        conn.close()

def update_fee_payment():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 📝 Update Fee Payment Record ---")
    try:
        fee_id = input("Enter the Fee_ID of the record to update: ")
        
        cur.execute("SELECT Fee_ID FROM FEES WHERE Fee_ID = %s", (fee_id,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Fee ID {fee_id} not found. Update aborted.")
            return

        new_paid = float(input("Enter NEW Amount Paid: "))
        new_pending = float(input("Enter NEW Remaining Pending Amount: "))
        
        sql = "UPDATE FEES SET Amount_Paid = %s, Pending_Amount = %s WHERE Fee_ID = %s"
        cur.execute(sql, (new_paid, new_pending, fee_id))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"✅ Fee record (ID {fee_id}) successfully updated. New Paid: {new_paid}, New Pending: {new_pending}.")
        else:
            print("⚠️ Warning: Record found, but no changes were made (values were the same).")

    except ValueError:
        print("❌ Invalid input. Please enter valid numbers for amounts.")
    except Exception as e:
        print(f"❌ Error updating fee payment: {e}")
    finally:
        cur.close()
        conn.close()
        
def add_timetable_entry():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Add Timetable Entry ---")
    try:
        course = input("Enter Course/Class (e.g., XII-A): ")
        day = input("Enter Day (e.g., Monday): ")
        time_slot = input("Enter Time Slot (e.g., 9:00-10:00): ")
        subject = input("Enter Subject Name: ")
        fid = int(input("Enter Assigned Faculty_ID: "))
        
        cur.execute("SELECT Faculty_ID FROM FACULTY WHERE Faculty_ID = %s", (fid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Faculty ID {fid} not found in the FACULTY database. Cannot assign timetable.")
            return

        sql = "INSERT INTO TIMETABLE (Course, Day, Time_Slot, Subject, Faculty_ID) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (course, day, time_slot, subject, fid))
        conn.commit()
        print("✅ Timetable entry added successfully!")
    except Exception as e:
        print(f"❌ Error adding timetable entry: {e}")
    finally:
        cur.close()
        conn.close()

def view_timetable():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    course_filter = input("Enter Course/Class to view (e.g., XII-A) or leave blank for all: ")
    
    try:
        if course_filter:
            sql = "SELECT t.Course, t.Day, t.Time_Slot, t.Subject, f.Name FROM TIMETABLE t JOIN FACULTY f ON t.Faculty_ID = f.Faculty_ID WHERE t.Course = %s ORDER BY t.Day, t.Time_Slot"
            cur.execute(sql, (course_filter,))
        else:
            sql = "SELECT t.Course, t.Day, t.Time_Slot, t.Subject, f.Name FROM TIMETABLE t JOIN FACULTY f ON t.Faculty_ID = f.Faculty_ID ORDER BY t.Course, t.Day, t.Time_Slot"
            cur.execute(sql)
            
        data = cur.fetchall()
        
        print(f"\n--- Timetable for {course_filter if course_filter else 'All Courses'} ---")
        if not data:
            print(f"No timetable entries found for {'this course' if course_filter else 'any course'}.")
            return
            
        for row in data:
            print(f"Course: {row[0]} | Day: {row[1]} | Time: {row[2]} | Subject: {row[3]} | Faculty: {row[4]}")
            
    except Exception as e:
        print(f"❌ Error viewing timetable: {e}")
    finally:
        cur.close()
        conn.close()

def update_timetable_entry():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 📝 Update Timetable Entry ---")
    try:
        timetable_id = input("Enter the Timetable_ID of the record to update: ")
        
        cur.execute("SELECT Timetable_ID FROM TIMETABLE WHERE Timetable_ID = %s", (timetable_id,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Timetable ID {timetable_id} not found. Update aborted.")
            return

        new_course = input("Enter NEW Course/Class (e.g., XII-A): ")
        new_day = input("Enter NEW Day (e.g., Monday): ")
        new_time_slot = input("Enter NEW Time Slot (e.g., 9:00-10:00): ")
        new_subject = input("Enter NEW Subject Name: ")
        new_fid = int(input("Enter NEW Assigned Faculty_ID: "))
        
        cur.execute("SELECT Faculty_ID FROM FACULTY WHERE Faculty_ID = %s", (new_fid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: New Faculty ID {new_fid} not found in the FACULTY database. Update aborted.")
            return

        sql = "UPDATE TIMETABLE SET Course = %s, Day = %s, Time_Slot = %s, Subject = %s, Faculty_ID = %s WHERE Timetable_ID = %s"
        cur.execute(sql, (new_course, new_day, new_time_slot, new_subject, new_fid, timetable_id))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"✅ Timetable entry (ID {timetable_id}) successfully updated to: {new_course}, {new_day}, {new_time_slot}.")
        else:
            print("⚠️ Warning: Record found, but no changes were made (values were the same).")

    except ValueError:
        print("❌ Invalid input. Please ensure Faculty ID is a number.")
    except Exception as e:
        print(f"❌ Error updating timetable entry: {e}")
    finally:
        cur.close()
        conn.close()

def issue_book():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Issue Book ---")
    try:
        book_id = input("Enter Book ID: ")
        sid = int(input("Enter Student ID: "))
        title = input("Enter Book Title: ")
        issue_date = input(f"Enter Issue Date (YYYY-MM-DD, default today: {date.today()}): ") or str(date.today())
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        
        cur.execute("SELECT Student_ID FROM STUDENTS WHERE Student_ID = %s", (sid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Student ID {sid} not found in the STUDENTS database. Cannot issue book.")
            return

        sql = "INSERT INTO LIBRARY (Book_ID, Student_ID, Book_Title, Issue_Date, Due_Date) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (book_id, sid, title, issue_date, due_date))
        conn.commit()
        print(f"✅ Book '{title}' issued successfully to Student {sid}.")
    except Exception as e:
        print(f"❌ Error issuing book: {e}")
    finally:
        cur.close()
        conn.close()

def return_book():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- Return Book (Check-in) ---")
    issue_id = input("Enter Issue_ID of the book to be returned: ")
    
    try:
        cur.execute("SELECT Issue_ID FROM LIBRARY WHERE Issue_ID = %s", (issue_id,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: Issue ID {issue_id} not found. Check ID or the book is already returned.")
            return

        sql = "DELETE FROM LIBRARY WHERE Issue_ID = %s"
        cur.execute(sql, (issue_id,))
        
        conn.commit()
        print(f"✅ Book with Issue_ID {issue_id} successfully returned (record closed).")

    except Exception as e:
        print(f"❌ Error processing return: {e}")
    finally:
        cur.close()
        conn.close()

def view_issued_books_by_class():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    print("\n--- 📚 Issued Books Sorted by Class ---")
    
    try:
        sql = """
        SELECT 
            s.Class, 
            s.Section, 
            s.Name, 
            l.Book_Title, 
            l.Due_Date 
        FROM 
            LIBRARY l
        JOIN 
            STUDENTS s ON l.Student_ID = s.Student_ID
        ORDER BY 
            s.Class, s.Section, s.Name
        """
        cur.execute(sql)
        data = cur.fetchall()

        if not data:
            print("No books are currently issued to any student.")
            return

        current_class = ""
        print("-" * 75)
        
        for class_name, section, student_name, book_title, due_date in data:
            class_section = f"{class_name}-{section}"
            
            if class_section != current_class:
                current_class = class_section
                print(f"\n--- CLASS: {current_class} ---")
                print(f"{'STUDENT NAME':<25} | {'BOOK TITLE':<30} | {'DUE DATE':<10}")
                print("-" * 75)
            
            print(f"{student_name:<25} | {book_title:<30} | {str(due_date):<10}")

        print("\n" + "-" * 75)
        
    except Exception as e:
        print(f"❌ Error generating book report: {e}")
    finally:
        cur.close()
        conn.close()

def view_pending_returns():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    try:
        sql = "SELECT l.Issue_ID, s.Name, l.Book_Title, l.Due_Date FROM LIBRARY l JOIN STUDENTS s ON l.Student_ID = s.Student_ID WHERE l.Due_Date < CURDATE()"
        cur.execute(sql)
        data = cur.fetchall()
        
        print("\n--- 🚨 PENDING/OVERDUE LIBRARY RETURNS ---")
        if not data:
            print("🎉 No overdue books found. Library is clear.")
            return
            
        for row in data:
            print(f"Issue ID: {row[0]} | Student: {row[1]} | Book: {row[2]} | DUE: {row[3]}")
            
    except Exception as e:
        print(f"❌ Error viewing pending returns: {e}")
    finally:
        cur.close()
        conn.close()

def update_issued_book():
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    print("\n--- 📝 Update Issued Book Record ---")
    try:
        issue_id = input("Enter the Issue_ID of the record to update: ")
        
        cur.execute("SELECT Book_Title, Student_ID FROM LIBRARY WHERE Issue_ID = %s", (issue_id,))
        record = cur.fetchone()
        if record is None:
            print(f"❌ ERROR: Issue ID {issue_id} not found. Update aborted.")
            return

        print(f"Current Record: Book '{record[0]}' issued to Student ID {record[1]}.")
        
        new_book_id = input("Enter NEW Book ID: ")
        new_sid = int(input("Enter NEW Student ID: "))
        new_title = input("Enter NEW Book Title: ")
        new_issue_date = input("Enter NEW Issue Date (YYYY-MM-DD): ")
        new_due_date = input("Enter NEW Due Date (YYYY-MM-DD): ")

        cur.execute("SELECT Student_ID FROM STUDENTS WHERE Student_ID = %s", (new_sid,))
        if cur.fetchone() is None:
            print(f"❌ ERROR: New Student ID {new_sid} not found in the STUDENTS database. Update aborted.")
            return

        sql = "UPDATE LIBRARY SET Book_ID = %s, Student_ID = %s, Book_Title = %s, Issue_Date = %s, Due_Date = %s WHERE Issue_ID = %s"
        cur.execute(sql, (new_book_id, new_sid, new_title, new_issue_date, new_due_date, issue_id))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"✅ Library record (Issue ID {issue_id}) successfully updated. New title: '{new_title}'.")
        else:
            print("⚠️ Warning: Record found, but no changes were made (values were the same).")

    except ValueError:
        print("❌ Invalid input. Please ensure Student ID is a number.")
    except Exception as e:
        print(f"❌ Error updating book record: {e}")
    finally:
        cur.close()
        conn.close()

def view_issued_books_by_student(sid):
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()
    
    try:
        sql = "SELECT Book_Title, Issue_Date, Due_Date FROM LIBRARY WHERE Student_ID = %s"
        cur.execute(sql, (sid,))
        data = cur.fetchall()
        
        print(f"\n--- Your Issued Books ---")
        if not data:
            print("You have no books currently issued.")
            return

        for title, issue, due in data:
            print(f"  - Title: {title} | Issued: {issue} | Due: {due}")

    except Exception as e:
        print(f"❌ Error viewing issued books: {e}")
    finally:
        cur.close()
        conn.close()
if __name__ == "__main__":
    homepage()
