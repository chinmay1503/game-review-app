"""
A simple game review flask app.
"""
from datetime import date
from .GameReview import GameReview
import sqlite3
DB_FILE = 'game_reviews.db'    # file for our Database

class model(GameReview):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from game_reviews")
        except sqlite3.OperationalError:
            #cursor.execute("create table game_reviews (name text, genre text, image_url text, author text, review_date date, review_title text, review_message, overall_score INTEGER)")
            cursor.execute("CREATE TABLE game_reviews (id INTEGER, name TEXT NOT NULL, genre TEXT, image_url TEXT, author TEXT NOT NULL, review_date TEXT, review_title	TEXT NOT NULL, review_message TEXT NOT NULL, overall_score INTEGER, PRIMARY KEY(id))")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, genre, image_url, author, review_date, review_title, review_message, overall_score FROM game_reviews")
        return cursor.fetchall()

    def selectById(self, id):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        params = {'id': id}
        cursor.execute("SELECT id, name, genre, image_url, author, review_date, review_title, review_message, overall_score FROM game_reviews WHERE id = :id", params)
        return cursor.fetchone()

    def insert(self, name, genre, image_url, author, review_title, review_message, overall_score):
        """
        Inserts entry into database
        :param name: String
        :param genre: String
        :param image_url: String
        :param author: String
        :param review_title: String
        :param review_message: String
        :param overall_score: Integer
        :return: none
        :raises: Database errors on connection and insertion
        """
        params = {'name': name, 'genre': genre, 'image_url': image_url, 'author': author, 'review_date': date.today(), 
                  'review_title': review_title, 'review_message': review_message, 'overall_score': overall_score}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO game_reviews (name, genre, image_url, author, review_date, review_title, review_message, overall_score)" + 
                       "VALUES (:name, :genre, :image_url, :author, :review_date, :review_title, :review_message, :overall_score)", params)

        connection.commit()
        cursor.close()
        return True


    def update(self, review_id, name, genre, image_url, author, review_title, review_message, overall_score):
        """
        Updates the entry in database
        :param id: Integer
        :param name: String
        :param genre: String
        :param image_url: String
        :param author: String
        :param review_title: String
        :param review_message: String
        :param overall_score: Integer
        :return: none
        :raises: Database errors on connection and updation
        """
        params = {'name': name, 'genre': genre, 'image_url': image_url, 'author': author, 'review_date': date.today(), 
                  'review_title': review_title, 'review_message': review_message, 'review_id': review_id, 'overall_score': overall_score}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("UPDATE game_reviews SET name = :name, genre = :genre, image_url = :image_url, author = :author" + 
                       ", review_date = :review_date, review_title = :review_title, review_message = :review_message, overall_score = :overall_score WHERE id = :review_id", params)

        connection.commit()
        cursor.close()
        return True

    def delete(self, review_id):
        """
        Deletes entry from database
        :return: True
        :raises: Database errors on connection and deletion
        """
        params = {'review_id': review_id}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM game_reviews WHERE id = :review_id", params)

        connection.commit()
        cursor.close()
        return True
