from __future__ import division


answer = str ("Yes")

while answer == "Yes" :

    print ("Addition : 1 | Subtraction : 2 | Multiplication : 3 | Division : 4 | Quit : 5")
    operation = int(input("Desired operation: "))

    if operation == 1 :
        additionfirstnumber = int(input("Input First Number: "))
        additionsecondnumber = int(input("Input Second Numbe: "))
        additionoutput = additionfirstnumber + additionsecondnumber
        print (additionoutput)
    if operation == 2 :
        subtractionfirstnumber = int(input("Input First Number: "))
        subtractionsecondnumber = int(input("Input Second Number: "))
        subtractionoutput = subtractionfirstnumber - subtractionsecondnumber
        print (subtractionoutput)

    if operation == 3 :
        multiplicationfirstnumber = int(input("Input First Number: "))
        multiplicationsecondnumber = int(input("Input Second Number: "))
        multiplicationoutput = multiplicationfirstnumber * multiplicationsecondnumber
        print (multiplicationoutput)

    if operation == 4 :
        divisionfirstnumber = int(input("Input First Number: "))
        divisionsecondnumber = int(input("Input Second Number: "))
        divisionoutput = divisionfirstnumber / divisionsecondnumber
        print (divisionoutput)
   
    if operation == 5 :
        print ("Goodbye")
        break
   # print ("Would you like to go again or exit?")
    #answer = str (input("Yes or No: "))
    
   # if answer == ("No") :
    #exit
