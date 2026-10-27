# 输入一个字符串，删除其中重复的字符，字母不区分大小写。
# 例如，输入bananas时输出bans，
# 输入AaBbcCdD时输出Abcd。
text = input("输入一个字符串:")
result = ""
seen = set()
for i in text:
    if i.lower() not in seen:
        result += i
        seen.add(i.lower())
print(result)      