## natural numbers sum  diiference###

# def solve(num):
#     count = 0
#     for i in range(1,num+1):
#         count += i*i
#     return count

def difference(n):
    val = n*(n+1)//2
    squareOfsum = val*val
    sumOfSquares = n*(n+1)*(2*n+1)/6
    ans = int(squareOfsum - sumOfSquares)
    return ans

print(difference(10))