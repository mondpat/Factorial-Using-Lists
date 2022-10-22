def ConvertIntToList(a: int) -> list[int]:
    a = str(a)
    b = 0
    out = []
    while(b < len(a)):
        out.append(int(a[b]))
        b += 1
    return out

def FlipList(arr: list[int]) -> list[int]:
    out = []
    a = len(arr)-1
    while(a >= 0):
        out.append(arr[a])
        a -= 1
    return out

def CalcAllNumbersInListToBeLowerThan10(arr: list[int]) -> list[int]:
    a = 0
    while(a < len(arr)):
        if(arr[a] > 9):
            b = arr[a] % 10
            c = int((arr[a] - b) / 10)
            if(a + 1 < len(arr)):
                arr[a + 1] += c
            else:
                arr.append(c)
            arr[a] = b
        a += 1
    return arr

def AddNumbersInTwoLists(x: list[int], y: list[int]) -> list[int]:
    out = []
    a = 0
    while(a < len(x) and a < len(y)):
        out.append(x[a] + y[a])
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
    return CalcAllNumbersInListToBeLowerThan10(out)

def MultiplyListByNumber(x: list[int], z: int) -> list[int]:
    a = 0
    x = FlipList(x)
    out = []
    while(a < len(x)):
        out.append(x[a] * z)
        a += 1
    return CalcAllNumbersInListToBeLowerThan10(FlipList(out))

def AddLeadingZeros(x: list[int], numberOfZeros: int) -> list[int]:
    x = FlipList(x)
    while(numberOfZeros > 0):
        x.append(0)
        numberOfZeros -= 1
    return FlipList(x)

def MultiplyByList(x: list[int], y: list[int]) -> list[int]:
    x = FlipList(x)
    y = FlipList(y)
    a = 0
    if(len(y) > len(x)):
        x, y = y, x
    add = []
    total = []
    while(a < len(y)):
        add = AddLeadingZeros(MultiplyListByNumber(x, y[a]), a)
        total = AddNumbersInTwoLists(total, add)
        a += 1
    return FlipList(CalcAllNumbersInListToBeLowerThan10(total))

def CalcFactorial(x: int) -> list[int]:
    TempFactorial = ConvertIntToList(1)
    multiplier = 2
    while(multiplier < x + 1):
        TempFactorial = MultiplyByList(TempFactorial, ConvertIntToList(multiplier))
        multiplier += 1
    return TempFactorial

def PrintList(x: list[int]) -> None:
    listLen = len(x)
    for a in range(0, len(x)):
        if listLen % 3 == 0:
            print(" ", end="")
        print(x[a], end = "")
        listLen -= 1

print("Welcome, please insert a number for calculating it's factorial: ", end="")
a = int(input())
b = CalcFactorial(a)
print(f"{a}! = ", end="")
PrintList(b)
print(f"\nThe length of the factorial is {len(b)} digits")