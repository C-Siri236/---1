# 输入一个字符串，删除字符串中的空格。
# 测试： 
# 输入：␣␣a␣b␣␣c␣，输出：abc
text = input("输入一个字符串:")
result = ""
for i in text:
    if i == " ":
        result += ""
    else:
        result += i        
print(result)
