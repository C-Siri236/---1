# 输出字符串中元音字母的个数。
# 例如，字符串hello中元音的个数是2。
text = input("输入一个字符串:")
a = 0
for i in text:
    if i in "a,e,i,o,u":
        a += 1
print(f"字符串{text}中元音的个数是{a}")
