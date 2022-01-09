print ("Addition : 1 | Subtraction : 2 |")
operation = int (input("Desired operation: "))

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