# 输入三个字符串s1、s2和s3。将 s1的子字符串s2替换为s3。
# 输入：abcdbce bc 12，输出：a12d12e
s1, s2, s3= input("输入三个字符串s1和s2和s3: ").split(" ")
print(s1.replace(s2,s3))