import random as r

class controller() :

    def __init__(self,tvSituation = "off",tvVolume = 0,channelList = ["TRT"], pChannel= "TRT") :

        self.tvSituation = tvSituation
        self.tvVolume = tvVolume
        self.channelList = channelList
        self.pChannel = pChannel

    def tvOn(self) :

        if (self.tvSituation == "on") :
            print("Television situation is 'open' already.")
        else :
            print("Current Situation of Television is 'open'")

            self.tvSituation = "open"   

    def tvOff (self) :

        if (self.tvSituation == "off") :
            print("Television situation is 'off' already.")
        else : 
            print("Current Situation of Television is 'off'")

            self.tvSituation = "off"

    def vSettings (self) :

        while True :

            choice = input("Volume Up = '>' , Volume Down = '<' , Exit = 'q' : ")

            if (choice == ">") :

                if(self.tvVolume == 31) :
                    print("You cant up the volume!")
                    print("Current Volume Situation :",self.tvVolume)
                else :
                    self.tvVolume += 1
                    print("Current Volume Situation :",self.tvVolume)

            elif (choice == "<") :

                if(self.tvVolume != 0) :
                    self.tvVolume -= 1
                    print("Current Volume Situation :",self.tvVolume)
                else :
                    print("You cant down the volume!")
                    print("Current Volume Situation :",self.tvVolume)

            elif (choice == "q") :

                print("Exiting Volume Settings.")
                break

    def addChannel (self,cName) :

        print("The Channel is Adding :",cName)

        self.channelList.append(cName)

        print("Current Channel List :",self.channelList)

    def rChannel (self) :

        random = r.randint(0,len(self.channelList) - 1)

        self.pChannel = self.channelList[random]

        print("Current Channel is :",self.pChannel)

    def __len__ (self) :

        return len(self.channelList)

    def __str__(self) :

        return "Situation of Television is : {}\nVolume of Television : {}\nChannel List : {}\nChannel : {}".format(self.tvSituation,self.tvVolume,self.channelList,self.pChannel)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

c = controller()

print("""

1-Turn on the TV
2-Turn off the TV
3-Turn the Volume Settings
4-Add Channel
5-Open the Random Channel
6-Show Number of the Channels 
7-Show the Current Situation of TV
q-Exit

""")

while True :

    choice = input("Enter Your Choice :")

    if (choice == "1") :

        c.tvOn()
    
    elif (choice == "2") :

        c.tvOff()
    
    elif (choice == "3") :

        c.vSettings()

    elif (choice == "4") :

        nChannel = input("Enter the Name of the Channel which You Want to Add :")

        c.addChannel(nChannel)

    elif (choice == "5") :

        c.rChannel()

    elif (choice == "6") :

        print("There are ",len(c),"Channels")

    elif (choice == "7") :

        print(c)

    elif (choice == "q") :

        break