myStr="Python-cool!"
print(myStr[1:3]) #yt
print(myStr[-5:-2]) #coo
print(myStr[-5:11]) #cool
print(myStr[:6]) #Python
print(myStr[:-1]) #Python-cool
print(myStr[6:]) #-cool!
print(myStr[-5:]) #cool!
myStr="1234567890"
print(myStr[2:8:2]) #357
print(myStr[8:2:-2]) #975
print(myStr[::-1]) #0987654321
print(myStr[5::2]) #680
print(myStr[-1::-2]) #08642
print(myStr[:len(myStr):3]) #1470
normalText='''Python Arithmetic Operators:\n
 Arithmetic operators are used to perform
 mathematical operations like addition,
 subtraction, multiplication and division.\n
 \tThere are 7 arithmetic operators in Python:
 \t\tAddition +\n
 \t\tSubtraction -\n
 \t\tDivision /\n
 \t\tModulus %\n
 \t\tExponentiation **\n
 \t\tFloor division //\n'''
rawText=r'''Python Arithmetic Operators:\n
 Arithmetic operators are used to perform
 mathematical operations like addition,
 subtraction, multiplication and division.\n
 \tThere are 7 arithmetic operators in Python:
 \t\tAddition +\n
 \t\tSubtraction -\n
 \t\tDivision /\n
 \t\tModulus %\n
 \t\tExponentiation **\n
 \t\tFloor division //\n
 '''
print(normalText)
print(rawText)
myList =["user", 12, 200.34, False, True]
print(myList [1]) #12
print(myList [-1]) #True
print(myList [-2]) #False
