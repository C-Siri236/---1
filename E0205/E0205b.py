# 将字符串中的大写字母转换为小写字母、小写字母转换成大写字母。
# 例如Abc123转换成aBC123。
text = input("输入一个字符串:")
result = ""
for i in text:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i
print(result)