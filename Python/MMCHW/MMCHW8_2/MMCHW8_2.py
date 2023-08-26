with open("MMCHW/MMCHW8_2/Players.txt","r",encoding = "utf-8") as file :

    Galatasaray = []
    Fenerbahce = []
    Besiktas = []

    for lines in file :

        lines = lines[:-1]

        pList = lines.split(",")

        if (pList[1] == "Galatasaray") :

            Galatasaray.append(lines + "\n")
        elif (pList[1] == "Fenerbahçe") :

            Fenerbahce.append(lines + "\n")
        else :

            Besiktas.append(lines + "\n")

with open("MMCHW/MMCHW8_2/pGalatasaray.txt","w",encoding = "utf-8") as file2 :

    for i in Galatasaray :

        file2.writelines(i)

with open("MMCHW/MMCHW8_2/pFenerbahçe.txt","w",encoding = "utf-8") as file3 :

    for i in Fenerbahce :

        file3.writelines(i)

with open("MMCHW/MMCHW8_2/pBeşiktaş.txt","w",encoding = "utf-8") as file4 :

    for i in Besiktas :

        file4.writelines(i)