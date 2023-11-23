def calculateAbsoluteValue(x):
    absoluteValue = abs(x)
    print("Absolute value of", x, "is", absoluteValue)
    return absoluteValue

def raiseToPower(base, exponent):
    power = pow(base, exponent)
    print(base, "raised to the power of", exponent, "is", power)
    return power

def roundToSpecifiedDecimalPlaces(number, decimalPlaces):
    roundedNumber = round(number, decimalPlaces)
    print("Rounding", number, "to", decimalPlaces, "decimal places:", roundedNumber)
    return roundedNumber

def findQuotientAndRemainder(dividend, divisor):
    quotient, remainder = divmod(dividend, divisor)
    print("The quotient of", dividend, "divided by", divisor, "is", quotient, ", with a remainder of", remainder)
    return quotient, remainder

if __name__ == "__main__":
    calculateAbsoluteValue(-5)

    raiseToPower(2, 3)

    roundToSpecifiedDecimalPlaces(3.14159, 2)

    findQuotientAndRemainder(10, 3)
