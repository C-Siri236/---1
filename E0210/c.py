# 排列。
# 输入一个字符串s和一个整数n，求从字符串s中任取n个字符形成的排列。
# 例如，从字符串abc中任取2个字符构成的排列是ab、ba、ac、ca、bc、cb。
def f(s, n, current, result):

    if n == 0:
        result.add(current)
        return 

    
    for i in range(len(s)):
        char = s[i]
        rest = s[:i] + s[i + 1:]

        f(rest, n - 1, current + char, result)


s = input("输入一个字符串: ")
n = int(input("输入一个整数: "))
result = set()

f(s, n, "", result)
print(" ".join(result))