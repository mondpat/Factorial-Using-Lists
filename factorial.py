def ToString(a):
    a = str(a)
    b = 0
    out = []
    while(b < len(a)):
        out.append(int(a[b]))
        b += 1
    return out

def Turn(pole):
    out = []
    a = len(pole)-1
    while(a >= 0):
        out.append(pole[a])
        a -= 1
    return out

def CalcAllNumbsInListToBeLowerThan10(arr):
    a = 0
    while(a < len(arr)):
        if(arr[a] > 9):
            b = arr[a] % 10
            c = int((arr[a]-b)/10)
            if(a+1 < len(arr)):
                arr[a+1] += c
            else:
                arr.append(c)
            arr[a] = b
        a += 1
    return arr

def Add(x, y):
    out = []
    a = 0
    while(a < len(x) and a < len(y)):
        out.append(x[a]+y[a])
        a += 1
    if(a != len(x) or a != len(y)):
        if(a != len(x)):
            while(a < len(x)):
                out.append(x[a])
                a += 1
        else:
            while(a < len(y)):
                out.append(y[a])
                a += 1
    return CalcAllNumbsInListToBeLowerThan10(out)

def MultiplyListByNumber(x, z):
    a = 0
    x = Turn(x)
    out = []
    while(a < len(x)):
        out.append(x[a]*z)
        a += 1
    return CalcAllNumbsInListToBeLowerThan10(Turn(out))

def AddLeadingZeros(x, z):
    a = 0
    x = Turn(x)
    while(a < z):
        x.append(0)
        a += 1
    return Turn(x)

def MultiplyByList(x, y):
    x = Turn(x)
    y = Turn(y)
    a = 0
    if(len(y) > len(x)):
        x, y = y, x
    add = []
    total = []
    while(a < len(y)):
        add = AddLeadingZeros(MultiplyListByNumber(x, y[a]), a)
        total = Add(total, add)
        a += 1
    return Turn(CalcAllNumbsInListToBeLowerThan10(total))

def CalcFactorial(x):
    TempFactorial = ToString(1)
    multiplier = 2
    while(multiplier < x+1):
        TempFactorial = MultiplyByList(TempFactorial, ToString(multiplier))
        multiplier += 1
    return TempFactorial

def PrintList(x):
    for a in range(0, len(x)):
        print(x[a], end="")

print("Welcome, please insert a number for calculating it's factorial: ", end="")
a = int(input())
b = CalcFactorial(a)
print(f"{a}! = ", end='')
PrintList(b)
print()
print(f"The lenght of the factorial is {len(b)}")