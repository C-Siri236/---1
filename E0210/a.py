# 输入一个字符串，输出该字符串字符的全排列。
# 测试： 
# 输入：ab，输出：ab ba 
# 输入：abc，输出：abc acb bac bca cab cba 
# 输入：aac，输出：aac aca caa
def f(rest, n, current, result):
    
    if n == 0:
        result.add(current)
        return
    
    for i in range(n):   
           new_current = current + rest[i] 
           new_rest = rest[:i] + rest[i + 1:]
           f(new_rest, n - 1, new_current, result)

text = input("输入一个字符串: ")
n = len(text)
result = []
result = set()

f(text, n, "", result)
print(" ".join(result))


       
           
    



# text = input("输入一个字符串:")
