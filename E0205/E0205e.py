# 删除字符串中字母以外的字符。
# 例如，删除字符串a+b=c中字母以外的字符得到abc
text = input("输入一个字符串:")
result = ""
for i in text:
    if i.isalpha():
        result += i
    else:
        result += ""
print(result)