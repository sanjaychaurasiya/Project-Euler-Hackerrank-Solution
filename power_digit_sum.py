# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    num = int(input())
    sq_num = str(2 ** num)
    sum_of_digits = 0
    for i in sq_num:
        sum_of_digits += int(i)
    print(sum_of_digits)
