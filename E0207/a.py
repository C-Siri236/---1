# 输入两个字符串s1和s2，其中s1的长度大于s2。计算s2在s1中出现的次数。
# 测试： 
# 输入：xhixhixhi x，输出：3 
# 输入：haha ho，输出：0 
# 输入：xxxxyz  xx，输出：2
s1, s2 = input("输入两个字符串s1和s2，其中s1的长度大于s2: ").split(" ")
n = len(s2)
m = len(s1)
count = 0
i = 0
while i <= m - n:
    j = s1[i:i + n]
    if j == s2:
        count += 1
        i += n
    else:
        i += 1
print(count)
