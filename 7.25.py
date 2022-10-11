# Pawan Kumar
# ID: 2046222
def exact_change(_input):
    dime = _input % 100 % 25 // 10
    nickel = _input % 100 % 25 % 10 // 5
    pennie = _input % 100 % 25 % 10 % 5 // 1
    dollar = _input // 100
    quarter = _input % 100 // 25
    return dollar,quarter,dime,nickel,pennie

if __name__ == '__main__':
    _input = int(input())

    dollar,quarter,dime,nickel,pennie = exact_change(_input)

    if _input <= 0:
        print("no change")
    else:
        if dollar > 1:
            print(str(dollar) + " dollars")
        elif dollar == 1:
            print(str(dollar) + " dollar")
        else:
            pass
        if quarter > 1:
            print(str(quarter) + " quarters")
        elif quarter == 1:
            print(str(quarter) + " quarter")
        else:
            pass
        if dime > 1:
            print(str(dime) + " dimes")
        elif dime == 1:
            print(str(dime) + " dime")
        else:
            pass
        if nickel > 1:
            print(str(nickel) + " nickels")
        elif nickel == 1:
            print(str(nickel) + " nickel")
        else:
            pass
        if pennie > 1:
            print(str(pennie) + " pennies")
        elif pennie == 1:
            print(str(pennie) + " penny")