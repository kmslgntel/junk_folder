import time


sangduk = "상둑이상둑이상둑"
length = len(sangduk)

for i in range(length):
    print(sangduk[i:].rjust(length + i))

for i in range(1, length):
    print(sangduk[:i].rjust(length + (length - i)))



    
num = int(input('거슬러줄 돈을 입력: '))
coin = [10, 7, 1]
c = []

coin = [10, 7, 1]

for i in range(len(coin)):
    temp = num//coin[i]
    num = num % coin[i]

    c.append(temp)

print(c)