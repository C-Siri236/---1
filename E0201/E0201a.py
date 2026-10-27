# 英文字母一共26个，其中的a、e、i、o、u是元音字母。
# 输入一个字符，判断它是不是元音。
# 输入A，输出A是元音 
# 输入e，输出e是元音 
# 输入b，输出b不是元音 
# 输入5，输出5不是元音
char = input("输入一个字符:")
new_char = char.lower()
if new_char in ["a","e","i","o","u"]:
    print(f"{char}是元音")
else:
    print(f"{char}不是元音")