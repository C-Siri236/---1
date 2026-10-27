# 将字符串中每个单词的第一个字母和最后一个字母转为大写，
# 假设字符串只包含字母和空格。
# 例如，输入字符串“How are you“，输出字符串“HoW ArE YoU“，
text = input("输入一个字符串:")
new_text = text.split(" ")
result = ""
for i in new_text:
    a = 0
    n = len(i)
    for j in i:
        a += 1
        if a == 1 or a == n:
            result += j.upper() 
        else:
            result += j 
    result += " "
print(result.strip())
     




    


