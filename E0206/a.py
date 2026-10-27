# 输入一个字符串，检查其中是否包含重复的字符，字母不区分大小写。
# 测试： 
# 输入：Ada，输出：True 
# 输入：ABCDEFG，输出：False
text = input("输入一个字符串:")
my_list = list(text)
l = len(text)
a = 0
result = []
for i in text:
    j = i.lower()
    a += 1
    for m in my_list[a:l + 1]:
        n = m.lower()
        if n == j:
            print("True")
            result.append(i)
            break
if result == []:
    print("False")        