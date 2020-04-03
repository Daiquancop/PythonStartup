def sumFunction(a, b):
    return a + b

def intTryParse(str):
    try:
        return int(str)
    except ValueError:
        return 0

x = input('Nhap x: ')
x = intTryParse(x)
y = input('Nhap y: ')
y = intTryParse(y)

print(sumFunction(x, y))