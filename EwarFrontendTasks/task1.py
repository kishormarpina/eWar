
def PrintNnums(n):
    arr = []
    while(True):
        for i in range(1,n+1):
            arr.append(str(i))
        print("".join(arr), end="")

num = int(input())
print(PrintNnums(num))


