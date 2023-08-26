def letterCalculation(lines) :

    lines = lines[:-1]

    lList = lines.split(",")

    name = lList[0] 
    grade1 = int(lList[1])
    grade2 = int(lList[2])
    grade3 = int(lList[3])

    lGrade = (grade1 * 30) / 100 + (grade2 * 30) / 100 + (grade3 * 40) / 100

    if(lGrade >= 90) :
        letter = "AA"
    elif(lGrade >= 85) :
        letter = "BA"
    elif(lGrade >= 80) :
        letter = "BB"   
    elif(lGrade >= 75) :
        letter = "CB"
    elif(lGrade >= 70) :
        letter = "CC"
    elif(lGrade >= 65) :
        letter = "DC"
    elif(lGrade >= 60) :
        letter = "DD"
    elif(lGrade >= 55) :
        letter = "FD"
    elif(lGrade < 55) :
        letter = "FF"

    return name,"---------->",letter,"\n"

with open("GradeCalculation/dosya.txt","r",encoding = "utf-8") as file :

    aletterGrade = []

    for i in file :

        aletterGrade.append(letterCalculation(i))

with open("GradeCalculation/grades.txt","w",encoding = "utf-8") as file2 :

    for i in aletterGrade :

        file2.writelines(i)
    