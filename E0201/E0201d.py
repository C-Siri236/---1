# 检查输入的字符是否是字母
char = input("输入一个字符:")
if "a" <= char <= "z" or "A" <= char <= "Z":
    print("是字母")
else:
    print("不是字母")