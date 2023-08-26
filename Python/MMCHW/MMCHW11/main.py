from mylib.singerProject import *

print("""

Welcome to Songs Project

Transactions :

1-Show Songs
2-Add a Song
3-Delete a Song
4-Show Sum Time 

If you want to exit press 'q'
*****************************
""")

s = Singers()


while True :

    process = input("Enter Your Operation :")

    if (process == "q") :

        print("The System is Shutting Down.")
        break

    elif (process == "1") :

        s.showSongs()

    elif (process == "2") :

        song = input("Enter the Name of The Song :")
        singer = input("Enter the Name of The Singer :")
        pCompany = input("Enter the Name of The Production Company :")
        time = int(input("Enter The Duration of The Song :"))

        newSong = Singer(song,singer,pCompany,time)

        s.addSong(singer)

    elif (process == "3") :

        name = input("Enter The Name of The Song which You Want to Delete :") 

        s.delSong(name)

    elif (process == "4") :

        s.sumTime()    
