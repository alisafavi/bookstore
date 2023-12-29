import sqlite3
import traceback

from models import Book


# class Database(object):
#     def __init__(self):
#         self.createDb()
#
#     def createDb(self):
#         self.executeQuery(
#             '''
#             CREATE TABLE IF NOT EXISTS books (
#                              id INTEGER PRIMARY KEY,
#                                 title TEXT,
#                                 author TEXT,
#                                 price REAL,
#                                 quantity INTEGER
#                             )
#                             ''')
#
#     def insert(self, book: Book):
#         self.executeQuery("INSERT INTO books VALUES (NULL,?,?,?,?)",
#                           (book.title, book.author, book.price, book.quantity))
#
#     def getAllBooks(self):
#         books = self.executeQuery("SELECT * FROM books")
#         for book in books:
#             print(book[0], book[1], book[2], book[3], book[4])
#
#         return books
#
#     def deleteBook(self, id):
#         query = "DELETE FROM books WHERE id = ?"
#         return self.executeQuery(query, id)
#
#     def getBook(self, id):
#         query = "SELECT * FROM books WHERE id = ?"
#         return self.executeQuery(query, id)[0]
#
#     def updateBook(self, book: Book):
#         query = "UPDATE books SET title = ?, author =? ,price =?,quantity=? WHERE id=?"
#         self.executeQuery(query, (book.title, book.author, book.price, book.quantity, book.id))
#
#     def sellBook(self, id, count):
#         getQuantityQuery = "SELECT quantity FROM books WHERE id =?"
#         quantity = self.executeQuery(getQuantityQuery, id)
#         if quantity: quantity = quantity[0][0]
#
#         if quantity < count:
#             print("Insufficient quantity.")
#             return False
#         updateQuery = "UPDATE books SET quantity =? WHERE id = ?"
#         return self.executeQuery(updateQuery, (quantity - count, id))
#
#     def searchBook(self, query):
#         searchQuery = "SELECT * FROM books WHERE title like ?"
#         return self.executeQuery(searchQuery,(query,))
#
#
#     def executeQuery(self, query, params=None):
#         conn = sqlite3.connect(DB_NAME)
#         cursor = conn.cursor()
#         try:
#             if params:
#                 cursor.execute(query, params)
#             else:
#                 cursor.execute(query)
#
#             if query.lower().startswith('select'):
#                 result = cursor.fetchall()
#                 return result
#
#             conn.commit()
#             return True  # for success operation
#         except sqlite3.Error as error:
#             print("Error executing query:", error)
#             return False
#         except Exception as error:
#             print("Error", error)
#             return False
#         finally:
#             cursor.close()
#             conn.close()


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

        self.__createTable()
        self.__connect()

    def __del__(self):
        self.__disconnect()

    def __connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def __disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def __execute_query(self, query, parameters=None):
        try:
            if not self.connection:
                self.__connect()

            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)

            self.connection.commit()

        except sqlite3.Error as error:
            print("Error", error)
            return False
        except Exception as error:
            print("Error", error)
            return False

    def __fetch_data(self, query, parameters=None):
        try:
            if not self.connection:
                self.__connect()

            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)

            return self.cursor.fetchall()

        except sqlite3.Error as error:
            print("Error", error)
            return False
        except Exception as error:
            print("Error", error)
            return False

    def __fetch_one(self, query, parameters=None):
        try:
            if not self.connection:
                self.__connect()

            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)

            return self.cursor.fetchone()

        except sqlite3.Error as error:
            print("Error : ", error)
            return False
        except Exception as error:
            print("Error", error)
            return False

    def __createTable(self):

        query = ("CREATE TABLE IF NOT EXISTS books"
                 "(id INTEGER PRIMARY key autoincrement,"
                 "title TEXT,"
                 "author TEXT,"
                 "price INTEGER not null ,"
                 "quantity INTEGER not null)")

        self.__execute_query(query)

    def getBookById(self, id):
        query = "SELECT * FROM books WHERE id = ?"
        return self.__fetch_one(query, (id,))

    def getAllBooks(self):
        query = "SELECT * FROM books"
        return self.__fetch_data(query)

    def searchBook(self, query):
        query = "%{}%".format(query)
        searchQuery = "SELECT * FROM books WHERE title like ? or author like ?"
        return self.__fetch_data(searchQuery, (query, query))

    def updateBook(self, book: Book):
        query = "UPDATE books SET title = ?, author =? ,price =?,quantity=? WHERE id=?"
        self.__execute_query(query, (book.title, book.author, book.price, book.quantity, book.id))

    def insertBook(self, book: Book):
        self.__execute_query("INSERT INTO books VALUES (NULL,?,?,?,?)",
                             (book.title, book.author, book.price, book.quantity))

    def deleteBook(self, bookId):
        query = "DELETE FROM books WHERE id =?"
        return self.__execute_query(query, (bookId,))
