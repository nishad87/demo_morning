'''
Python 1st assignment
'''
def range_check_or(number):
    if number < -10 or number > 10:
        return True
    return False


def odd_number_check_with_and(number):
    if number % 2 == 1 and number % 3 == 1:
        return True
    return False


def divisibleBy4Or6(number):
    if number % 4 == 0 or number % 6 == 0:
        return True
    return False


def eligibleToVoteOrDrive(age):
    if age >= 18 or age >= 16:
        return True
    return False


def multipleRangeCheck(number):
    if (1 <= number <= 10) or (20 <= number <= 30):
        return True
    return False


def negativeAndOdd(number):
    if number < 0 and abs(number % 2) == 1:
        return True
    return False


def checkSeniorOrStudent(age):
    if age > 60 or age < 25:
        return True
    return False


def checkDivisibleBy5And7(number):
    if number % 5 == 0 and number % 7 == 0:
        return True
    return False


def checkNonNegativeOrEven(number):
    if number % 2 == 0 or number > 0:
        return True
    return False


def checkOdd(number):
    if number % 2 == 1:
        return True
    return False


def checkEven(number):
    if number % 2 == 0:
        return True
    return False


def checkPositive(number):
    if number > 0:
        return True
    return False


def checkNonPositiveAndEvenNumber(number):
    if not checkPositive(number) and (checkEven(number)):
        return True
    return False


def checkPrime(number):
    checkVal = int(number / 2)
    i = 2
    isPrime = True
    while i <= checkVal:
        if number % i == 0:
            isPrime = False
            break
        i = i + 1
    return isPrime


def checkPrimeAndOddNumber(number):
    if checkPrime(number) and checkOdd(number):
        return True
    return False


def eligibleForDiscountOrFreeShipping(purchaseAmount):
    if purchaseAmount > 150:
        print('Eligible for discount')
    elif purchaseAmount > 100:
        print('Eligible for free shipping')
    else:
        print('Not eligible')


def checkDivisibleBy3Or8(number):
    if (number % 3 == 0 or number % 8 == 0):
        return True
    return False


def checkDivisibleBy2Or5(number):
    if number % 2 == 0 or number % 5 == 0:
        return True
    return False


def ageGroupClassification(age):
    if age < 13:
        print('Child')
    elif age >= 13 and age <= 19:
        print('Teenager')
    elif age >= 20:
        print('Adult')


def checkSeniorAndStudent(age):
    '''Dead question'''
    if (age > 60 and age < 25):
        return True
    return False


def checkMultipleOf3And7(number):
    if number % 3 == 0 and number % 7 == 0:
        return True
    return False


def checkDivisbleBy5Or9(number):
    if number % 5 == 0 or number % 9 == 0:
        return True
    return False


def checkDivisibleBy3And5(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    return False


def checkOddAndNotDivisibleBy4(number):
    if checkOdd(number) and number % 4 == 1:
        return True
    return False


'''/*
def eligibleForDiscountOrMemberShipBenefits(purchaseAmount,loyaltyCardAvailable):
  if(purchaseAmount>200 or loyaltyCardAvailable)

    return True

  return False
}
'''


def checkDivisibleBy2Or3(num):
    if num % 2 == 0 or num % 3 == 0:
        return True
    return False


def checkPositiveAndNotDivBy3(num):
    if checkPositive(num) and num % 3 == 1:
        return True
    return False


def eligibleForSeniorDiscountAndNotNewCustomer(age, newCustomer):
    if age > 65 or not newCustomer:
        return True
    return False


def checkPrimeOrOddNumber(number):
    if checkPrime(number) or checkOdd(number):
        return True
    return False


def eligibleForDiscountOrMemberShipBenefits(purchaseAmount, loyaltyCardAvailable):
    if (purchaseAmount > 200):
        print('Qualifies for Discount')
    elif (loyaltyCardAvailable):
        print('Qualifies for Membership')
    else:
        print('Not eligible')


def eligibleForDiscountAndFreeShipping(purchaseAmount):
    if purchaseAmount > 150:
        print('Eligible for discount and free shipping')
    elif purchaseAmount > 100:
        print('Eligible for free shipping')
    else:
        print('Not eligible')


def checkNonNegativeAndNotDivBy7(num):
    if checkPositive(num) and num % 7 == 1:
        return True
    return False


def eligibleForStudentDiscountOrFreeTrial(age, freeTrial):
    if age < 25 or freeTrial:
        return True
    return False


def checkDivisibleBy4Or6(num):
    if num % 4 == 0 or num % 3 == 6:
        return True
    return False

def check_even_positive(num):
    if num>0 and num%2==0 :
        return True
    return False
def main():
    print('What about you?')
    print(check_even_positive(2));
    print(check_even_positive(-2));
    print(check_even_positive(0));
    print(check_even_positive(3));
    print(check_even_positive(-3));
    print(check_even_positive(10));
    print("########Output2#######");
    print(range_check_or(2));
    print(range_check_or(-2));
    print(range_check_or(0));
    print(range_check_or(3));
    print(range_check_or(-3));
    print(range_check_or(10));
    print(range_check_or(11));
    print(range_check_or(-10));
    print(range_check_or(-11));
    print("########Output3#######");
    print(odd_number_check_with_and(27));
    print(odd_number_check_with_and(31));
    print("########Output4#######");
    print(divisibleBy4Or6(44));
    print(divisibleBy4Or6(42));
    print(divisibleBy4Or6(46));
    print("########Output5#######");
    print(eligibleToVoteOrDrive(15));
    print(eligibleToVoteOrDrive(20));
    print("########Output6#######");
    print(multipleRangeCheck(11));
    print(multipleRangeCheck(2));
    print(multipleRangeCheck(20));
    print("########Output7#######");
    print(negativeAndOdd(-7));
    print("########Output9#######");
    print(checkDivisibleBy5And7(35));
    print(checkDivisibleBy5And7(30));
    print("########Output11#######");
    print(checkPrimeAndOddNumber(17));
    print(checkPrimeAndOddNumber(61));
    print(checkPrimeAndOddNumber(117));
    print(checkPrimeAndOddNumber(200));
    print("########Output12#######");
    print(eligibleForDiscountOrFreeShipping(151));


if __name__ == '__main__':
    main()
