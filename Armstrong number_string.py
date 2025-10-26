num = 153
num2 = str(num)
n = len(num2)
sum1 = 0

for digit in num2:
    sum1 += int(digit) ** n

if sum1 == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
