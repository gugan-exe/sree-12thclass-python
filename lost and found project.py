import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sreegugan",     
    database="lost_found_db")

cur = db.cursor()
print("Welcome to EPS lost and found Reporting System")
    
def report_lost():
    item = input("Enter item name: ")
    desc = input("Enter description: ")
    place = input("Enter location lost: ")
    date = input("Enter date lost (YYYY-MM-DD): ")
    student = input("Enter student name who lost it: ")

    sql = "INSERT INTO lost_items (name, description, location, lost_date, student_name) VALUES (%s, %s, %s, %s, %s)"
    data = (item, desc, place, date, student)
    cur.execute(sql, data)
    db.commit()
    print("Lost item recorded!\n")
    
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    clas = input("Enter class: ")
    sec = input("Enter section: ")
    
    sql = "INSERT INTO students (roll_no, name, class, section) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (roll, name, clas, sec))
    db.commit()
    print("Student added successfully!\n")

def report_found():
    item = input("Enter found item name: ")
    desc = input("Enter description: ")
    place = input("Enter location found: ")
    date = input("Enter date found (YYYY-MM-DD): ")

    sql = "INSERT INTO found_items (name, description, location, found_date) VALUES (%s,%s,%s,%s)"
    data = (item, desc, place, date)
    cur.execute(sql, data)
    db.commit()
    print("Found item recorded!\n")

def show_lost():
    cur.execute("SELECT * FROM lost_items")
    rows = cur.fetchall()
    print("\n Lost Items ")
    for r in rows:
        print(r)

def show_found():
    cur.execute("SELECT * FROM found_items")
    rows = cur.fetchall()
    print("\n--- Found Items ---")
    for r in rows:
        print(r)
def search_lost():
    keyword = input("Enter item name to search: ")
    cur.execute("SELECT * FROM lost_items WHERE name LIKE %s", ("%" + keyword + "%",))
    rows = cur.fetchall()
    if rows:
        print("\nSearch Results:")
        for r in rows:
            print(r)
    else:
        print("\nNo such item found.")
def delete_item():
    table = input("Delete from (lost/found): ").lower()
    item_id = input("Enter item ID to delete: ")
    if table == "lost":
        cur.execute("DELETE FROM lost_items WHERE id=%s", (item_id,))
    else:
        cur.execute("DELETE FROM found_items WHERE id=%s", (item_id,))
    db.commit()
    print("\n Item deleted successfully!\n")
def count_items():
    cur.execute("SELECT COUNT(*) FROM lost_items")
    lost = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM found_items")
    found = cur.fetchone()[0]
    print(f"\n Total Lost Items: {lost}, Total Found Items: {found}\n")

while True:
    print("\n====== Lost & Found System ======")
    print("1. Add Student")
    print("2. Report Lost Item")
    print("3. Report Found Item")
    print("4. View Lost Items")
    print("5. View Found Items")
    print("6. Search Lost Item")
    print("7. Delete Item")
    print("8. Count Items")
    print("9. Exit")
    
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        report_lost()
    elif choice == "3":
        report_found()
    elif choice == "4":
        show_lost()
    elif choice == "5":
        show_found()
    elif choice == "6":
        search_lost()
    elif choice == "7":
        delete_item()
    elif choice == "8":
        count_items()
    elif choice == "9":
        print("Thank you for using EPS Lost & Found System")
        break
    else:
        print("Invalid choice, try again!")


db.close()
