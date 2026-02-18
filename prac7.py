
N = int(input())



Swifts = input().split()


Sema = input().split()


semaCount = 0
swifCount = 0
count = 0
largest = 0
for i in range(N):

    semaCount += int(Sema[i])
    swifCount += int(Swifts[i])
    count += 1
    if semaCount == swifCount:
        largest = count




print(largest)
