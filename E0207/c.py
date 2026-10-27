# 求最长公共子串。
# 输入两个字符串s1和s2，输出它们的最长公共子串。
# 例如，
# 字符串“1AB2345CD”和字符串”12345EF”的最长公共子串是”2345”
s1, s2 = input("输入两个字符串s1和s2，其中s1的长度大于s2: ").split(" ")
n = len(s2)
m = len(s1)
d = {}
for i in range(n):
    for j in range(i + 1,n + 1):
        text = s2[i:j]
        if text in s1:
            d[text] = len(text)
if d:
    longest = max(d, key=lambda x: d[x])
    print(f"最长公共子串是{longest}")
else:
    print("没有公共子串")
