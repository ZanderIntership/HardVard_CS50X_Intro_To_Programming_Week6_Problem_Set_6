
symbol = "#"
space = " "


while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        pass


for i in range(1, height + 1):
   
    print(space * (height - i), end="")

    print(symbol * i)
