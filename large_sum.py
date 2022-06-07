# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums = []
sum_of_num = 0
for i in range(n):
    nums.append(int(input()))
for num in nums:
    sum_of_num += num
sum_of_num = str(sum_of_num)
print(sum_of_num[:10])
