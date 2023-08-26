#Q1
from multiprocessing.managers import DictProxy


def q1() :

    sntc = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

    dWord = dict()

    for i in sntc :

        if (i in dWord) :

            dWord[i] += 1
        
        else :

            dWord[i] = 1

    for w,c in dWord.items() :

        print("{} Character Occur {} times.".format(w,c))

#Q2
def q2() :

    sntc = str()

    with open("MMCHW/MMCHW10/şiir.txt","r",encoding= "utf8") as file :


        for i in file :

            sntc  += i[0]

    print(sntc)

#Q3
def q3() :

    with open("MMCHW/MMCHW10/mailler.txt","r",encoding= "utf-8") as file :

        cMails = list()

        for mail in file :

            mail = mail[:-1]

            if (mail.endswith(".com") and mail.find("@") != -1) :

                cMails.append(mail)

        print("The Correct Mails Are :",cMails)

#Q4 
def q4 () :

    fName = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
    lName = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

    for fN,lN in zip(fName,lName) :

        print(fN, " " , lN)
        