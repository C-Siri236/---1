# 删除字符串中的元音字母。
# 例如，删除字符串hello中的元音得到hll
text = input("输入一个字符串:")
result = ""
for i in text:
    if i in "a,e,i,o,u":
       result += ""
    else:
        result += i
print(result)
