# 在字符串环中查找子串。
# 输入两个字符串s1和s2，其中s1的长度大于s2。
# 将s1想象成为一个环，检查s1中是否包含s2。
# 例如，字符串”abcd”环中包含子串”abc”， 
# 字符串”abcdef” 环中包含子串”EFAB”， 
# 字符串”BCDE” 环中不包含子串”EC”， 
# 字符串”Challenge” 环中包含子串”GECH”。
s1, s2 = input("输入两个字符串s1和s2，其中s1的长度大于s2: ").split(" ")
n = s2.lower()
m = s1.lower()
if n in (m + m):
    print(f"{s1}环中包含子串{s2}")
else:
    print(f"{s1}环中不包含子串{s2}")
