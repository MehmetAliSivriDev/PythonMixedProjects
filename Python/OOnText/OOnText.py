class oOnFile() :

    def __init__(self) :

        with open("OOnText/metin.txt","r",encoding= "utf-8") as file :

            fContents = file.read()

            words = fContents.split()
            self.jWords = list()

            for i in words :

                i = i.strip("\n")
                i = i.strip("")
                i = i.strip(".")
                i = i.strip(",")

                self.jWords.append(i)

    def allWords(self) :

        setWords = set()

        for i in self.jWords :

            setWords.add(i)

        print("All Words :") 

        for i in setWords :

            print(i)

    def wFrequency (self) :

        dWord = dict()

        for i in self.jWords :

            if (i in dWord) :

                dWord[i] += 1

            else :

                dWord[i] = 1

        for w,c in dWord.items() :

            print("{} Word Occur {} times.".format(w,c))

f = oOnFile()

f.wFrequency()