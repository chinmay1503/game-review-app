class GameReview():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, genre, image_url, author, review_title, review_message):
        """
        Inserts entry into database
        :param name: String
        :param genre: String
        :param image_url: String
        :param author: String
        :param review_title: String
        :param review_message: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

    def update(self, review_id, name, genre, image_url, author, review_title, review_message):
        """
        Updates the entry in database
        :param review_id: Integer
        :param name: String
        :param genre: String
        :param image_url: String
        :param author: String
        :param review_title: String
        :param review_message: String
        :return: none
        :raises: Database errors on connection and updation
        """
        pass

    def delete(self, review_id):
        """
        Deletes entry from database
        :param review_id: Integer
        :return: none
        :raises: Database errors on connection and deletion
        """
        pass
