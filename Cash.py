Quarters = 0
Nickels = 0
Dimes = 0
pennies = 0
Change = 0
while True:
    try:
        IntialAmount = float(input("Change: "))
        if 0 <= IntialAmount:
            break
    except ValueError:
        pass

IntialAmount = round(IntialAmount * 100)


if IntialAmount / 25 >= 1:
    Quarters += ( int(IntialAmount ) // 25 )
    IntialAmount -= Quarters * 25
if IntialAmount / 10 >= 1:
    Dimes += ( int(IntialAmount ) // 10 )
    IntialAmount -= Dimes * 10
if IntialAmount / 5 >= 1:
    Nickels += ( int(IntialAmount ) // 5 )
    IntialAmount -= Nickels * 5
if IntialAmount / 1 >= 1:
    pennies += ( int(IntialAmount ) // 1 )
    IntialAmount -= pennies * 1

Change = Quarters + Dimes + Nickels + pennies
print(int(Change))
