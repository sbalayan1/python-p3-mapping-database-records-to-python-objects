#this lab covers a small problem. Python and our database do not speak the same language. So how can we get these two to communicate? When we query the database, we need to translate the raw data from our database into Python objects!

import sqlite3

CONN = sqlite3.connect()
CURSOR = CONN.cursor()

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        pass

    @classmethod
    def drop_table(cls):
        pass

    @classmethod
    def create(cls, name, album):
        pass


    #this class method converts what the database gives us into a python object. 
    @classmethod
    def new_from_db(cls, row):
        pass
        #it's important to note that sqlite3 will give us back an array of data for each row [1, Billie Jean, Thriller]

        #we don't need to use the create() method here because we are not saving to the database. we are just creating a new instance. 
        
        song = cls(row[1], row[2]) #row[1] refers to the name and row[2] to the album. 
        song.id = row[0] #after we create the new class, we save the id held in row[0] to the song's id attribute.
