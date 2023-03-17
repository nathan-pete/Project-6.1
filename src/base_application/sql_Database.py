import sqlite3
from sqlite3 import Error



def create_connection(quintor):
    """ create a database connection to the SQLite database
        specified by db_file
    :param quintor: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(quintor)
        # enables the foreign keys
        conn.execute("PRAGMA foreign_keys = 1")

        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def table_create():
    database = "quintor.db"

    sql_create_association_table = """ CREATE TABLE IF NOT EXISTS Association (
            AccountID STRING(35) NOT NULL PRIMARY KEY ,
            name STRING(50) NOT NULL
        ); """

    sql_create_file_table = """ CREATE TABLE IF NOT EXISTS File (
            referenceNumber STRING(16) NOT NULL PRIMARY KEY ,
            statementNumber STRING NOT NULL,
            sequenceDetail STRING NOT NULL,
            availableBalance REAL NOT NULL,
            forwardAvBalance REAL NOT NULL,
            accountID STRING(35) NOT NULL,
            FOREIGN KEY (accountID) REFERENCES Association (AccountID)
        ); """

    sql_create_transaction_table = """ CREATE TABLE IF NOT EXISTS Transactions (
            transactionID INTEGER PRIMARY KEY AUTOINCREMENT,
            referenceNumber STRING(16),
            transactionDetail STRING ,
            description STRING(128),
            amount REAL(15) NOT NULL,
            currency STRING(3) NOT NULL,
            transaction_date STRING(10),
            categoryID INTEGER,
            memberID INTEGER,
            typeTransaction STRING,
            FOREIGN KEY (referenceNumber) REFERENCES File (referenceNumber),
            FOREIGN KEY (categoryID) REFERENCES Category (categoryID),
            FOREIGN KEY (memberID) REFERENCES Member (memberID)
            ); """

    sql_create_category_table = """ CREATE TABLE IF NOT EXISTS Category (
                categoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                name STRING(32)
                ); """

    sql_create_member_table = """ CREATE TABLE IF NOT EXISTS Member (
                    memberID INTEGER PRIMARY KEY AUTOINCREMENT,
                    name STRING(32) NOT NULL,
                    email STRING(254) NOT NULL
                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Association table
        create_table(conn, sql_create_association_table)

        # create File table
        create_table(conn, sql_create_file_table)

        # create Transactions table
        create_table(conn, sql_create_transaction_table)

        # create Category table
        create_table(conn, sql_create_category_table)

        # create Member table
        create_table(conn, sql_create_member_table)
    else:
        print("Error! cannot create the database connection.")

table_create()