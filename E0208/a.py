# 输入三个字符串s1、s2和s3。将 s1的子字符串s2替换为s3。
# 输入：abcdbce bc 12，输出：a12d12e
s1, s2, s3= input("输入三个字符串s1和s2和s3: ").split(" ")
n = len(s2)
m = len(s1)
i = 0
result = ""
while i <= m - n:
    j = s1[i:i + n]
    if j == s2:
        result += s3
        i += n
    else:
        result += s1[i]
        i += 1
        
result += s1[i:]
print(result)


            