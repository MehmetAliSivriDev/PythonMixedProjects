def failed(lines) :

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

    if(lGrade < 55) :

        return name,"---------->",letter,"---------->","Failed to Pass!","\n"
    
    else :
        
        return ""

def passed(lines) :

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

    if(lGrade > 55) :

        return name,"---------->",letter,"---------->","Passed!","\n"   

    else :
        
        return ""

with open("MMCHW/MMCHW8_1/dosya.txt","r",encoding = "utf-8") as file :

    failedSt = []
    passedSt = []

    for i in file :

        failedSt.append(failed(i))

    file.seek(0)

    for i in file :

        passedSt.append(passed(i))

with open("MMCHW/MMCHW8_1/failed.txt","w",encoding = "utf-8") as file2 :

    for i in failedSt :

        file2.writelines(i)
    
with open("MMCHW/MMCHW8_1/passed.txt","w",encoding = "utf-8") as file3 :

    for i in passedSt :

        file3.writelines(i)