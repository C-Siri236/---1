# 如果字符串s1的字符重排顺序后得到字符串s2，则称它们互为异序词。
# 输入两个字符串s1和s2，检查它们是否互为异序词
# 输入：otto tato，输出：False 
# 输入：mary army，输出：True
s1, s2 = input("输入两个字符串s1和s2: ").split(" ")
n = sorted(s2)
m = sorted(s1)
if m == n:
    print("True")
else:
    print("False")