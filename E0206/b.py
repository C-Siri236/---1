text = input("输入一个字符串:")
if len(text) != len(set(text)):
    print("True")
else:
    print("False")