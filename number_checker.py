num = int(input('Enter the number:'))
result = 0

for i in range(1, num):
    if num % i == 0:
        result += i

if result == num:
    print(num, "is a perfect number")
elif result < num:
    print(num, "is a deficient number")
else:
    print(num, "is an abundant number")

# Note that you'll need to rerun the code to run the program again

