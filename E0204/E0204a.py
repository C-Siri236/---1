# 回文字符串从左向右和从右向左读都是一样的。
# 例如，“aba”是回文字符串，而“abc”不是。
# 输入一个字符串，检查它是不是回文字符串。
# 测试： 
# 输入：aba，输出：aba是回文字符串 
# 输入：abc，输出：abc不是回文字符串
text = input("输入一个字符串:")
new_text = text[::-1]
if new_text == text:
    print(f"{text}是回文字符串")
else:
    print(f"{text}不是回文字符串")
