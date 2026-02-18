s = input()
k = int(input())

# Parse RLE
pairs = []
i = 0

while i < len(s):
    char = s[i]
    i += 1
    print(s[i])
    num = ""
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    
    pairs.append((char, int(num)))

# Compute total pattern length
total_length = sum(count for _, count in pairs)

# Reduce k into one cycle
k = (k - 1) % total_length + 1

# Find the character
current = 0
for char, count in pairs:
    current += count
    if k <= current:
        print(char)
        break
