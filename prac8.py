sides = input().split()
length = []
width = []
width1 = 0
length1 = 0

for i in range(len(sides)):
    if i%2 == 0:
        width.append(sides[i])
    else:
        length.append(sides[i])

if int(width[0]) > int(width[1]):
    width1 = int(width[0])
else:
    width1 = int(width[1])

length1 = int(length[1]) + int(length[0])

print(2*width1 + 2*length1)