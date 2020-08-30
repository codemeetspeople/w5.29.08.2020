from books.db import (
    get_connection,
    CREATE_BOOK_STATEMENT,
    UPDATE_BOOK_STATEMENT,
    SELECT_BOOK_STATEMENT
)


class ObjectNotFound(Exception):
    pass


class Book:
    connection = get_connection()

    def __init__(self, _id=None):
        self._id = None
        self._author = None
        self._title = None
        self.__changed = False

        if _id:
            self.__load(_id)

    @property
    def id(self):
        return self._id

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @author.setter
    def author(self, value):
        self._author = value
        self.__changed = True

    @title.setter
    def title(self, value):
        self._title = value
        self.__changed = True

    def save(self):
        if self.__changed:
            cursor = self.connection.cursor()

            if not self.id:
                cursor.execute(CREATE_BOOK_STATEMENT, (self.author, self.title))
                self._id = cursor.lastrowid
            else:
                cursor.execute(UPDATE_BOOK_STATEMENT, (self.author, self.title, self.id))

            self.connection.commit()

    def __load(self, _id):
        cursor = self.connection.cursor()
        objects = cursor.execute(SELECT_BOOK_STATEMENT, (_id,))
        result = objects.fetchone()

        if not result:
            raise ObjectNotFound()

        self._id = result[0]
        self._title = result[1]
        self._author = result[2]
