# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    num = int(input())
    if num == 0:
        print(1)
        continue
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    factorial = str(factorial)
    sum_of_digits = 0
    for f in factorial:
        sum_of_digits += int(f)
    print(sum_of_digits)