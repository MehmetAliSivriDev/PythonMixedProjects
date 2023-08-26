
import sqlite3

class Singer() :

    def __init__(self,song,singer,pCompany,time) :
        
        self.song = song
        self.singer = singer
        self.pCompany = pCompany
        self.time = time

    def __str__(self) :

        return "Song Name: {}\nSinger Name: {}\nProduction Company: {}\nSong Duration: {}\n".format(self.song,self.singer,self.pCompany,self.time)

class Singers() :

    def __init__ (self) :

        self.connect()

    def connect (self) :

        self.connection = sqlite3.connect("Singers.db")

        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS Singers (Song TEXT,Singer TEXT,pCompany TEXT,Duration INT)"

        self.cursor.execute(query)

        self.connection.commit()

    def showSongs (self) :

        query = "Select * From Singers"

        self.cursor.execute(query)

        songs = self.cursor.fetchall()

        if (len(songs) == 0) :

            print("There is no song in the table.")

        else :

            for i in songs :

                Song = Singer(i[0],i[1],i[2],i[3])

                print(Song)

    def addSong (self,singer) :

        query = "Insert into Singers Values(?,?,?,?)"

        self.cursor.execute(query,(singer.song,singer.singer,singer.pCompany,singer.time))

        self.connection.commit()

    def delSong (self,name) :

        query = "Delete From Singers where song = ? "

        self.cursor.execute(query,(name,)) 

        self.connection.commit()

    def sumTime (self) :

        query = "Select * From Singers"

        self.cursor.execute(query)

        sDurations  = self.cursor.fletchall()

        for i in sDurations :

            time = sDurations[3]

            allTime += time 

        print("Sum Time is :",allTime)

    
