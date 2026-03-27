import mysql.connector
from mysql.connector import errorcode
import os

# Connection
def connect():
    try:
        con = mysql.connector.connect(user='root', password='jairus', host='localhost', database='Sale')
        print('Connection successful')
        return con
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
           

#Insert Record
def add(con):
    try:
        while True:
            code = input('Enter Product Code : ')
            name = input('Enter Product Name : ')
            price = float(input('Enter Product Price : '))

            # Execute SQL
            cursor = con.cursor()
            sql = "Insert Into tblProduct Values ('%s', '%s', '%f')" % (code, name, price)

            # Insert new Product
            #cursor.execute("Insert Into tblProduct (Code, Name, Price) Values ('%s', '%s', '%f')" % (code, name, price))
            cursor.execute(sql)
            con.commit()

            print('Record save')
            x = input("Do you want to add another record [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    except mysql.connector.Error as err:
            print(err)
           
    else:
        cursor.close()
        con.close()

#Delete Record
def delete (con):
    try:
        while True:
            code = input('Enter Product Code : ')

            # Execute SQL
            cursor = con.cursor()
            sql = "Delete From tblProduct Where Code = '%s'" % code
            cursor.execute(sql)
            con.commit()

            print('Record deleted')
            x = input("Do you want to delete another record [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    except mysql.connector.Error as err:
        print(err)
       
    else:
        cursor.close()
        con.close()

#Edit Record
def edit(con):
    try:
        while True:
            code = input('Enter Product Code : ')
            name = input('Enter Product Name : ')
            price = float(input('Enter Product Price : '))

            # Execute SQL
            cursor = con.cursor()
            sql = "Update tblProduct Set Name = '%s', Price = '%f' Where Code = '%s'" % (name, price, code)
            cursor.execute(sql)
            con.commit()

            print('Changes save')
            x = input("Do you want to edit another record [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    except mysql.connector.Error as err:
            print(err)
            
    else:
        cursor.close()
        con.close()


#Search Record
def search(con):
    try:
        while True:
            code = input('Enter Product Code : ')

            # Executing SQL-DML Commands
            cursor = con.cursor()
            query = "Select * From tblProduct Where Code ='%s'" % code

            # Search Product
            cursor.execute(query)
            row = cursor.fetchone()
            if row is not None:
                print('Product Name :', row[1])
                print('Product Price', row[2])
            else:
                print("Record not found")

            x = input("Do you want to search another record [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    except mysql.connector.Error as err:
            print(err)
            
    else:
        cursor.close()
        con.close()

#Retrive all records
def searchAll(con):
    try:
            # Executing SQL-DML Commands
            cursor = con.cursor()
            query = "Select * From tblProduct"
            cursor.execute(query)
            for row in cursor:
                print("Product Code : ", row[0])
                print("Product Name : ", row[1])
                print("Product Price : ", row[2], "\n")

    except mysql.connector.Error as err:
            print(err)
            
    else:
        cursor.close()
        con.close()
    


def main():
   while True:
       connect()
       print("[1] Add New Record")
       print("[2] Edit Record")
       print("[3] Delete Record")
       print("[4] Search Record")
       print("[5] Display All Record")
       choice = input("Enter your choice : ")

       if choice == "1":
           os.system('cls')
           c = connect()
           add(c)
       elif choice == "2":
           os.system('cls')
           c = connect()
           edit(c)
       elif choice == "3":
           os.system('cls')
           c = connect()
           delete(c)
       elif choice == "3":
           os.system('cls')
           c = connect()
           delete(c)
       elif choice == "4":
           os.system('cls')
           c = connect()
           search(c)
       elif choice == "5":
           os.system('cls')
           c = connect()
           searchAll(c)

       x = input("Return to main menu [y/n]? ")
       if x == 'y':
           os.system('cls')
           continue
       else:
           break

       exit(0)


main()
