import sqlite3
import traceback

from models import Book


DB_NAME = "books.db"
__connection = None
__cursor = None

print("ddd")


def __connect():
    global __connection
    global __cursor
    __connection = sqlite3.connect(DB_NAME)
    __cursor = __connection.cursor()


def __execute_query(query, parameters=None):
    try:
        if not __connection:
            __connect()

        if parameters:
            __cursor.execute(query, parameters)
        else:
            __cursor.execute(query)

        __connection.commit()

    except sqlite3.Error as error:
        print("Error", error)
        return False
    except Exception as error:
        print("Error", error)
        return False


def __fetch_data(query, parameters=None):
    try:
        if not __connection:
            __connect()

        if parameters:
            __cursor.execute(query, parameters)
        else:
            __cursor.execute(query)

        return __cursor.fetchall()

    except sqlite3.Error as error:
        print("Error", error)
        return False
    except Exception as error:
        print("Error", error)
        return False


def __fetch_one(query, parameters=None):
    try:
        if not __connection:
            __connect()

        if parameters:
            __cursor.execute(query, parameters)
        else:
            __cursor.execute(query)

        return __cursor.fetchone()

    except sqlite3.Error as error:
        print("Error : ", error)
        return False
    except Exception as error:
        print("Error", error)
        return False


def __createTable():
    query = '''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY autoincrement,
            title TEXT,
            author TEXT,
            price INTEGER,
            quantity INTEGER
        )
    '''
    __execute_query(query)


__createTable()
__connect()


def getBookById(id):
    query = "SELECT * FROM books WHERE id = ?"
    return __fetch_one(query, (id,))


def getAllBooks():
    query = "SELECT * FROM books"
    return __fetch_data(query)


def searchBook(query):
    query = "%{}%".format(query)
    searchQuery = "SELECT * FROM books WHERE title like ? or author like ?"
    return __fetch_data(searchQuery, (query, query))
