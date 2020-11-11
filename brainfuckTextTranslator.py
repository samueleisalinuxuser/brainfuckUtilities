import argparse
parser = argparse.ArgumentParser(description="A small utility that translates texts in brainfuck.")
parser.add_argument("-t", help="text to be translated")
args = parser.parse_args()

sentence,ordChars,program = args.t,list(),""

for char in sentence: ordChars.append(ord(char))
del char

previousOrdChar = 0

for ordCharIndex in range(len(ordChars)):
    ordChars[ordCharIndex] = [ordChars[ordCharIndex],ordChars[ordCharIndex]-previousOrdChar,list()]
    currentOrdChar,currentDivisors = ordChars[ordCharIndex][1:3]

    """

    this part of the program puts in ordChars[2] all the current difference dividers

    for possibleDivisor in range(2,abs(currentOrdChar)+1):
        if abs(currentOrdChar)%possibleDivisor == 0:
            while abs(currentOrdChar)%possibleDivisor == 0:
                currentOrdChar = int(abs(currentOrdChar)/possibleDivisor)
                currentDivisors.append(possibleDivisor)
    """

    """
    this part of the program is the same as the one in the docstrings above, but unlike the
    latter it puts in ordChars[2] the products of all equal dividers 
    """
    
    if abs(currentOrdChar) == 1: currentDivisors.append(1)

    else:

        for possibleDivisor in range(2,abs(currentOrdChar)+1):
            if abs(currentOrdChar)%possibleDivisor == 0:
                productOfEqualDivisors = 1
                while abs(currentOrdChar)%possibleDivisor == 0:
                    currentOrdChar = int(abs(currentOrdChar)/possibleDivisor)
                    productOfEqualDivisors*=possibleDivisor
            
                currentDivisors.append(productOfEqualDivisors)

    previousOrdChar = ordChars[ordCharIndex][0]

"""

this part of the programme finds the major divider and multiplies the minor ones
among them in order to obtain two factors that can be used in a loop in the brainfuck program

for productDifferenceDivisors in ordChars:
    productDivisors = productDifferenceDivisors[2]

    if len(productDivisors) > 2:
        maxProduct = max(productDivisors)
        productDivisors.remove(maxProduct)
        minProduct = 1
        
        for minDivisorsProducts in productDivisors: minProduct*=minDivisorsProducts

        productDifferenceDivisors[2] = [minProduct,maxProduct]
"""

"""
this part of the program is the same as the one in the docstrings above, but unlike the
latter it also takes care of generating the code in brainfuck
"""
for productDifferenceDivisors in ordChars:
    productDivisors,maxProduct,minProduct = productDifferenceDivisors[2],0,1

    if productDifferenceDivisors[1] > 0: sign0,sign1 = "+","-"
    elif productDifferenceDivisors[1] < 0: sign0,sign1 = "-","+"

    if len(productDivisors) >= 2:
        
        if len(productDivisors) > 2:
            maxProduct = max(productDivisors)
            productDivisors.remove(maxProduct)
            minProduct = 1
        
            for minDivisorsProducts in productDivisors: minProduct*=minDivisorsProducts

            productDifferenceDivisors[2] = [minProduct,maxProduct]
    
        elif len(productDivisors) == 2: maxProduct,minProduct = max(productDivisors),min(productDivisors)

        program += ">" + sign0*maxProduct + "[<" + sign0*minProduct + ">" + sign1 + "]<."

    elif len(productDivisors) == 1:
        divisor = productDivisors[0]
        program += sign0*divisor + "."

    elif len(productDivisors) == 0: program += "."

print(program)