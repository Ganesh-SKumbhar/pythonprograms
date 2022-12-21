
num = int(input("Enter number: "))

l = 1
r = num//2 + 1
while l <= r:
    mid = (l+r) // 2
    if mid * mid == num:
        print(mid)
    if mid * mid > num:
        r = mid - 1
    else:
         l = mid +1
print(r)



