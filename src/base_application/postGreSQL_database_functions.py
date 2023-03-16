import psycopg2
import re
import hashlib
from utils import parse_mt940_file, check_mt940_file
from json import *

# Establishing the connection
conn = psycopg2.connect(
    database="Quintor", user='postgres', password='password', host='localhost', port='5432'
)


def hash_password(password):
    # Convert the password string to bytes and hash it using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


# def insertIntoAssociation(account_id, association_name, association_password):
#     try:
#         cursor = conn.cursor()
#         hashed_password = ""
#
#         print("Connected to SQLite")
#         if isinstance(account_id, str):
#             if isinstance(association_name, str):
#                 if isinstance(association_password, str):
#                     hashed_password = hash_password(association_password)
#
#                     postgres_insert_query = """ INSERT INTO Association (accountId,name, password) VALUES (%s,%s,%s)"""
#                     record_to_insert = (account_id, association_name, association_password)
#                     cursor.execute(postgres_insert_query, record_to_insert)
#                     conn.commit()
#                     count = cursor.rowcount
#                     print(count, "Python Variable inserted successfully into Association table")
#                 else:
#                     print("Please insert a password")
#             else:
#                 print("Name is not a string")
#         else:
#             print("Please insert an integer for the account id")
#     except (Exception, psycopg2.Error) as error:
#         print("Failed to insert record into mobile table", error)
#     finally:
#         # closing database connection.
#         if conn:
#             cursor.close()
#             conn.close()
#             print("PostgreSQL connection is closed")
#
#
# def insertIntoFile(reference_Number, statement_Number, sequence_Detail, available_Balance, forward_Av_Balance,
#                    account_Id):
#     try:
#         cursor = conn.cursor()
#         print("Connected to SQLite")
#         if isinstance(reference_Number, str):
#             if len(reference_Number) < 17:
#                 if isinstance(statement_Number, str):
#                     if statement_Number:
#                         if isinstance(sequence_Detail, str):
#                             if sequence_Detail:
#                                 if isinstance(available_Balance, float) or isinstance(available_Balance, int):
#                                     if available_Balance:
#                                         if isinstance(forward_Av_Balance, float) or isinstance(forward_Av_Balance, int):
#                                             if forward_Av_Balance:
#                                                 if isinstance(account_Id, str):
#                                                     postgres_insert_query = """ INSERT INTO File (referenceNumber, statementNumber, sequenceDetail, availableBalance, forwardAvBalance, accountId)
#                                                                                 VALUES (%s,%s,%s,%s,%s,%s)"""
#
#                                                     record_to_insert = (
#                                                     reference_Number, statement_Number, sequence_Detail,
#                                                     available_Balance, forward_Av_Balance, account_Id)
#                                                     cursor.execute(postgres_insert_query, record_to_insert)
#
#                                                     conn.commit()
#                                                     count = cursor.rowcount
#                                                     print(count,
#                                                           "Python Variable inserted successfully into File table")
#                                                 else:
#                                                     print("The Account Id need to be a string")
#                                             else:
#                                                 print("The Forward Balance cannot be null!")
#                                         else:
#                                             print("The Forward Balance need to be a number")
#                                     else:
#                                         print("The available balance cannot be null!")
#                                 else:
#                                     print("The Available Balance need to be a number!")
#                             else:
#                                 print("The Sequence Detail cannot be null!")
#                         else:
#                             print("The sequence Detail need to be a string!")
#                     else:
#                         print("Statement number cannot be null")
#                 else:
#                     print("Statement numberis not a string")
#             else:
#                 print("The lenght of Reference number need to not exceed 16 characters")
#         else:
#             print("Please insert a String for the Reference Number")
#     except (Exception, psycopg2.Error) as error:
#         print("Failed to insert record into File table", error)
#     finally:
#         # closing database connection.
#         if conn:
#             cursor.close()
#             conn.close()
#             print("PostgreSQL connection is closed")
#
# # insertIntoFile("test","test","test",1232,23232,"32424")

def insert_into_association(accountId, name, password):
    try:
        cursor = conn.cursor()
        hashed_password = hash_password(password)

        # call a stored procedure
        cursor.execute('CALL insert_into_association(%s,%s,%s)', (accountId, name, hashed_password))

        # commit the transaction
        conn.commit()

        # close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_into_file(referenceNumber, statementNumber, sequenceDetail, availableBalance, forwardAvBalance, accountID):
    try:
        cursor = conn.cursor()

        # call a stored procedure
        cursor.execute('CALL insert_into_file(%s,%s,%s,%s,%s,%s)', (
            referenceNumber, statementNumber, sequenceDetail, availableBalance, forwardAvBalance, accountID))

        # commit the transaction
        conn.commit()

        # close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_into_transaction(referenceNumber, transactionDetail, description, amount, currency, transaction_date,
                            categoryID, memberID, typeTransaction):
    try:
        cursor = conn.cursor()

        # call a stored procedure
        cursor.execute('CALL insert_into_transaction(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
            referenceNumber, transactionDetail, description, amount, currency, transaction_date, categoryID, memberID,
            typeTransaction))

        # commit the transaction
        conn.commit()

        # close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_into_Member(name, email):
    try:
        cursor = conn.cursor()

        # call a stored procedure
        cursor.execute('CALL insert_into_member(%s,%s)', (name, email))

        # commit the transaction
        conn.commit()

        # close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# insert_into_Member("Alin", "bosull2002@gmail.com")

def update_transaction(transactionID, referenceNumber, transactionDetail, description, amount, currency,
                       transaction_date,
                       categoryID, memberID, typeTransaction):
    try:
        cursor = conn.cursor()

        # call a stored procedure
        cursor.execute('CALL update_transaction(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
            transactionID, referenceNumber, transactionDetail, description, amount, currency, transaction_date,
            categoryID, memberID,
            typeTransaction))

        # commit the transaction
        conn.commit()

        # close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# update_transaction(1,"123","update","update",69.69,"USD","23-02-2023",1,2,"CASH")

def delete_member(memberID):
    try:
        cursor = conn.cursor()

        # call a stored procedure
        cursor.execute('CALL delete_member(%s)', (memberID,))

        # commit the transaction
        conn.commit()

        # close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# delete_member(3)

def get_Association():
    try:
        cursor = conn.cursor()

        # call a stored procedure
        cursor.execute('CALL get_association();')

        # commit the transaction
        conn.commit()

        # close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

get_Association()