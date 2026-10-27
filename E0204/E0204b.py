# 求字符串的最长回文子串。
# 例如，字符串“1223“的最长回文子串是“22“，
# 字符串“121312“的最长回文子串是“21312“
text = input("输入一个字符串:")
result = []
d = {}
n = len(text)
for a in range(n):
    for j in range(a + 2,n + 1):
        new_text = text[a:j]
        reverse_text = new_text[::-1]
        if reverse_text == new_text:
            d[new_text] = len(new_text)
longest = max(d, key=lambda x: d[x])
print(f"字符串{text}的最长回文子串是{longest}")
 
