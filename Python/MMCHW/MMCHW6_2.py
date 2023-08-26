
class Animal() :

    def __init__(self,aName = "None",isSleep = "yes") :

        self.aName = aName 
        self.isSleep = isSleep
    
    def wAnimal(self) :

        if (self.isSleep == "no") :

            print("The Animal is Already Awake.")
        else :

            self.isSleep = "no"
        
            print("The Animal is Waking Up.")

    def sAnimal(self) :

        if (self.isSleep == "yes") :

            print("The Animal is Already Asleep.")
        else :

            self.isSleep = "yes"

            print("The Animal is Sleeping.")

    def changeName(self,newName) :

        self.aName = newName

        print("New Name of The Animal is :",newName)

    def tAnimal(self) :

        print("The Animal is Talking Now!")

    def fAnimal(self) :

        print("You Giving a Food the Animal Now!")

#----------------------------------------------------------------------------------------------------------------------------------------    


class Dog(Animal) :

    def __init__(self,aName = "None",isSleep =  "yes") :
        super().__init__(aName,isSleep)

    def tAnimal(self) :

        super().tAnimal()

        print("Hav Hav Hav!!")

    def fAnimal(self) :

        super().fAnimal()

        print("Your Giving a Bone!")

#----------------------------------------------------------------------------------------------------------------------------------

class Bird(Animal) :
    
    def __init__(self,aName = "None",isSleep =  "yes",year = 10) :
        super().__init__(aName,isSleep)
        self.year = year
    
    def tAnimal(self) :

        super().tAnimal()

        print("Cik Cik Cik!!")

    def fAnimal(self) :

        super().fAnimal()

        print("Your Giving a Bird Food!")

#----------------------------------------------------------------------------------------------------------------------------------

class Horse(Animal) :

    def __init__(self,aName = "None",isSleep =  "yes") :
        super().__init__(aName,isSleep)

    def tAnimal(self) :

        super().tAnimal()

        print("EEEIIIGGHAAA!!")

    def fAnimal(self) :

        super().fAnimal()

        print("Your Giving an Apple!")

#----------------------------------------------------------------------------------------------------------------------------------
