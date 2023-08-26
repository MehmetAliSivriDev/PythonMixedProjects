class computer() :

    def __init__(self,uName = "Admin",uPass = 1234,pcSituation = "off",pcVolume = 0,apps = ["Trash","MyComputer","Microsoft Edge"],wifi = "Off") :

        self.uName = uName
        self.uPass = uPass
        self.pcSituation = pcSituation
        self.pcVolume = pcVolume
        self.apps = apps
        self.wifi = wifi
    
    def pcOpen(self) :

        if (self.pcSituation == "on") :

            print("The Computer Situation is 'ON' already.")
        else : 

            self.pcSituation = "on"

            print("The Computer Situation is 'ON' now.")

    def pcOff(self) :

        if (self.pcSituation == "off") :

            print("The Computer Situation is 'OFF' already.")
        else :

            self.pcSituation = "off"

            print("The Computer Situation is 'OFF' now.")

    def vSettings(self) :

        while True :

            choice = input("Volume Up = '>' , Volume Down = '<' , Exit = 'q' : ")

            if (choice == ">") :

                if(self.pcVolume == 100) :
                    print("You cant up the volume!")
                    print("Current Volume Situation :",self.pcVolume)
                else :
                    self.pcVolume += 2
                    print("Current Volume Situation :",self.pcVolume)

            elif (choice == "<") :

                if(self.pcVolume != 0) :
                    self.pcVolume -= 2
                    print("Current Volume Situation :",self.pcVolume)
                else :
                    print("You cant down the volume!")
                    print("Current Volume Situation :",self.pcVolume)

            elif (choice == "q") :

                print("Exiting Volume Settings.")
                break

    def downloadApp(self,appName) :

        print("The App is Downloading :",appName)

        self.apps.append(appName)

        print("Current Apps :",self.apps)

    def delApp(self,appName) :

        print("The App is Deleting :",appName)

        self.apps.remove(appName)

        print("Current Apps :",self.apps)

    def wOpen(self) :

        if (self.wifi == "on") :

            print("The Wifi Situation is 'ON' already.")
        else : 

            self.wifi = "on"

            print("The Wifi Situation is 'ON' now.")

    def wOff(self) :

        if (self.wifi == "off") :

            print("The Wifi Situation is 'OFF' already.")
        else :

            self.wifi = "off"

            print("The Wifi Situation is 'OFF' now.")

    def __len__(self) :

        return len(self.apps)

    def __str__(self) :

        return "User Name : {}\nUser Password : {}\nComputer Volume : {}\nWifi Situation : {}\nApps : {}".format(self.uName,self.uPass,self.pcVolume,self.wifi,self.apps)

#--------------------------------------------------------------------------------------------------------------------------------------------------

c = computer()

while True :

    if (c.pcSituation == "off") :

        cSit = input("The Computer Situation is Off.\nFor Opening press 1 :")

        if(cSit == "1") :

            c.pcOpen()
            break

        else : 
            continue
      
while True :

    print("Current User Name and Password is Default : 'Admin' '1234'")

    uChoice = input("Do You Want to Change Them ? Press (Yes : 1, No : 2) :")

    if (uChoice == "1") :

        newName = input("Enter Your New User Name :")
        newPass = input("Enter Your New Password :")

        c.uName = newName
        c.uPass = newPass

        print("The Process is Completed.Welcome!")
        break
    
    elif (uChoice == "2") :

        print("User Name and Password is Still Same Then.Welcome!")
        break
    
    else :

        print("Please Press Correctly!")

while True :

    print("""
    
    1-Open The Volume Settings
    2-Download an App
    3-Delete an App
    4-Open the Wifi
    5-Close the Wifi
    6-Show the Count of Apps 
    7-Show the Current Situation of Computer
    q-Close the Computer


    """)

    uChoice = input("Enter Your Process :")

    if (uChoice == "1") :

        c.vSettings()
    
    elif (uChoice == "2") :

        appName = input("Enter the App Name which You Want to Download :") 

        c.downloadApp(appName)

    elif (uChoice == "3") :

        appName = input("Enter the App Name Which You Want to Delete :")

        c.delApp(appName)

    elif (uChoice == "4") :

        c.wOpen()

    elif (uChoice == "5") :

        c.wOff()

    elif (uChoice == "6") :

        print("There are",len(c)," Apps")

    elif (uChoice == "7") :

        print(c)

    elif (uChoice == "q") :

        print("The Computer is Shutting Down.")

        c.pcOff()

        break
    
    else :

        print("Please Press Correctly!")


