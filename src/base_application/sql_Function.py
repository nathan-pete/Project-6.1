import sqlite3
import re
from utils import parse_mt940_file, check_mt940_file
from json import *

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


def insertIntoAssociation(accountId, name):
    try:
        sqliteConnection = sqlite3.connect('quintor.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        if isinstance(accountId, str):
            if isinstance(name, str):
                sqlite_insert_with_param = """ INSERT INTO Association (accountId,name)
                                            VALUES (?,?);"""
                data_tuplet = (accountId, name)
                cursor.execute(sqlite_insert_with_param, data_tuplet)
                sqliteConnection.commit()
                print("Python Variable inserted successfully into Association table")
            else:
                print("Name is not a string")
        else:
            print("Please insert an integer for the account id")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def insertIntoFile(referenceNumber, statementNumber, sequenceDetail, availableBalance, forwardAvBalance, accountId):
    try:
        sqliteConnection = sqlite3.connect('quintor.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        if isinstance(referenceNumber, str):
            if len(referenceNumber) < 17:
                if isinstance(statementNumber, str):
                    if statementNumber:
                        if isinstance(sequenceDetail, str):
                            if sequenceDetail:
                                if isinstance(availableBalance, float) or isinstance(availableBalance, int):
                                    if availableBalance:
                                        if isinstance(forwardAvBalance, float) or isinstance(forwardAvBalance, int):
                                            if forwardAvBalance:
                                                if isinstance(accountId, str):
                                                    sqlite_insert_with_param = """ INSERT INTO File (referenceNumber, statementNumber, sequenceDetail, availableBalance, forwardAvBalance, accountId)
                                                                                VALUES (?,?,?,?,?,?);"""
                                                    data_tuplet = (
                                                        referenceNumber, statementNumber, sequenceDetail,
                                                        availableBalance,
                                                        forwardAvBalance, accountId)
                                                    cursor.execute(sqlite_insert_with_param, data_tuplet)
                                                    sqliteConnection.commit()
                                                    print(
                                                        "Python Variable inserted successfully into File table")
                                                else:
                                                    print("The Account Id need to be a string")
                                            else:
                                                print("The Forward Balance cannot be null!")
                                        else:
                                            print("The Forward Balance need to be a number")
                                    else:
                                        print("The available balance cannot be null!")
                                else:
                                    print("The Available Balance need to be a number!")
                            else:
                                print("The Sequence Detail cannot be null!")
                        else:
                            print("The sequence Detail need to be a string!")
                    else:
                        print("Statement number cannot be null")
                else:
                    print("Statement numberis not a string")
            else:
                print("The lenght of Reference number need to not exceed 16 characters")
        else:
            print("Please insert a String for the Reference Number")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def insertIntoTranssaction(referenceNumber, transactionDetail, description, amount, currency, transaction_date,
                           categoryID, memberID, typeTransaction):
    try:
        sqliteConnection = sqlite3.connect('quintor.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        if isinstance(referenceNumber, str):
            if len(referenceNumber) < 16:
                if isinstance(transactionDetail, str):
                    if isinstance(description, str):
                        if len(description) <= 128:
                            if isinstance(amount, float) or isinstance(amount, int):
                                if len(str(amount)) <= 15:
                                    if isinstance(currency, str):
                                        if len(currency) <= 3:
                                            if isinstance(transaction_date, str):
                                                if len(transaction_date) <= 10:
                                                    if isinstance(categoryID, int):
                                                        if isinstance(memberID, int):
                                                            if isinstance(typeTransaction, str):
                                                                sqlite_insert_with_param = """ INSERT INTO Transactions (referenceNumber, transactionDetail, description, amount, currency,transaction_date, categoryID, memberID, typeTransaction)
                                                                                            VALUES (?,?,?,?,?,?,?,?,?);"""
                                                                data_tuplet = (
                                                                    referenceNumber, transactionDetail, description,
                                                                    amount,
                                                                    currency, transaction_date, categoryID, memberID,
                                                                    typeTransaction)
                                                                cursor.execute(sqlite_insert_with_param, data_tuplet)
                                                                sqliteConnection.commit()
                                                                print(
                                                                    "Python Variable inserted successfully into Transaction table")
                                                            else:
                                                                print("Type Transaction need to be String")
                                                        else:
                                                            print("The Member ID need to be int!")
                                                    else:
                                                        print("Category ID need to be int!")
                                                else:
                                                    print("Date cannot exceed 10 characters!")
                                            else:
                                                print("Transaction Date need  to be a string")
                                        else:
                                            print("Currency cannot exceed 3 characters!")
                                    else:
                                        print("Currency  need to be a String")
                                else:
                                    print("The length of amount cannot exceed 15 characters.")
                            else:
                                print("Amount need to be a number!")
                        else:
                            print("The Sequence Detail cannot be null!")
                    else:
                        print("Description need to be a string!")
                else:
                    print("Transaction detail is not a string")
            else:
                print("The lenght of Reference number need to not exceed 16 characters")
        else:
            print(" Reference Number need to be a String!")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def insertIntoMember(name, email):
    try:
        sqliteConnection = sqlite3.connect('quintor.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        if isinstance(name, str):
            if len(name) <= 32:
                if isinstance(email, str):
                    if len(email) <= 254:
                        if check(email):
                            sqlite_insert_with_param = """ INSERT INTO Member (name,email)
                                                        VALUES (?,?);"""
                            data_tuplet = (name, email)
                            cursor.execute(sqlite_insert_with_param, data_tuplet)
                            sqliteConnection.commit()
                            print("Python Variable inserted successfully into Member table")
                        else:
                            print("The email is invalid")
                    else:
                        print("Email cannot exceed 254 characters")
                else:
                    print("Email need to be a String!")
            else:
                print("Name cannot exceed 32 characters")
        else:
            print("Name need to be a String")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def select_From_Category():
    category_list = {}
    try:
        sqliteConnection = sqlite3.connect('quintor.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        splite_select_query = """ SELECT * from Category"""
        cursor.execute(splite_select_query)
        records = cursor.fetchall()
        for row in records:
            category_list[str(row[0])] = str(row[1])
        return category_list
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def select_From_Member():
    member_list = {}
    try:
        sqliteConnection = sqlite3.connect('quintor.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        splite_select_query = """ SELECT * from Member"""
        cursor.execute(splite_select_query)
        records = cursor.fetchall()
        for row in records:
            member_list[str(row[0])] = str(row[1])
        return member_list
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def map_mt940_file(file_path):
    if not check_mt940_file(file_path):
        #Make a pop up
        return

    json_transactions = parse_mt940_file(file_path)
    try:
        # Db connection
        sqliteConnection = sqlite3.connect('quintor.db')
        cursor = sqliteConnection.cursor()

        # Get user's account ID from db
        splite_select_query = """ SELECT AccountID from Association"""
        cursor.execute(splite_select_query)
        records = cursor.fetchall()
        account_id = records[0][0]

        # Extract values from a JSON into varaibles
        reference_number = json_transactions["transaction_reference"]
        statement_number = json_transactions["statement_number"]
        sequence_detail = str(json_transactions["sequence_number"])
        available_balance = float(json_transactions["available_balance"]["amount"]["amount"])
        forward_available_balance = float(json_transactions["forward_available_balance"]["amount"]["amount"])

        # Map values into a realtional DB
        insertIntoFile(reference_number, statement_number, sequence_detail, available_balance, forward_available_balance, account_id)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")



# insertIntoAssociation("NL69INGB0123456789EUR", "Test")
map_mt940_file("C:/University/Semester_2/Project6.1/Project-6.1_Code/src/resources/mt940Example.sta")

