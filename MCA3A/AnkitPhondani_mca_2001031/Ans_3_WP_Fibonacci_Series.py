n = int(input("Enter the value of 'n': "))
 a = 0
 b = 1
sum = 0
count = 1
while(count <= n):
    a = b
    b = sum
    sum = a + b
    count += 1
    print(sum)


