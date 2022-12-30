#this lab covers a small problem. Python and our database do not speak the same language. So how can we get these two to communicate? When we query the database, we need to translate the raw data from our database into Python objects!

from . import CURSOR

class Song:
    all = []

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        pass
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY, 
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

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

    @classmethod
    def get_all(cls):
        pass
        all = CURSOR.execute("SELECT * FROM songs").fetchall()

        #we can't just return all! at this point the variable 'all' is an array of rows like this [1,"billie jean", "michael jackson"]. These rows need to be converted into instances of the Song class. We can use the new_from_db class method

        #here we assign the 'all' CLASS VARIABLE, not the all variable above, to an array of Song instances
        cls.all = [cls.new_from_db(row) for row in all]
        return cls.all

    #the fetchall() method will return the returned rows of a sql query sequentially in a tuple. 

    @classmethod
    def find_by_name(cls, name):
        pass
        #you need to include LIMIT 1 so you only get 1 row back 
        sql = """
            SELECT * FROM songs WHERE name = ? LIMIT 1
        """

        #the name is passed below because bound parameters need to be passed as sequence data types to the execute() method. This is typically done with tuple. A single argument tuple is interpreted as a grouped statement. 
        song = CURSOR.execute(sql, (name,)).fetchone()
        #fetchone returns the first element returned from fetchall().

