
N = int(input())

Swifts = input().split()

Sema = input().split()

Swifts.append(4)
Sema.append(6)

semaCount = 0
swifCount = 0
count = 0

for i in range(N):

    semaCount += int(Sema[i])
    swifCount += int(Swifts[i])

    count += 1

    if semaCount == swifCount:
        
        if N == 1:
            print(count)
            break
        elif count < N-1 or Sema[i+1] != Swifts[i+1]:
            print(count)
            break
        else:
            continue
        
    elif semaCount != swifCount and count >= N:
        count = 0
        print(count)
        break

