# 组合。
# 输入一个字符串s和一个整数n，求从字符串s中任取n个字符形成的组合。
# 例如，从字符串abc中任取2个字符构成的组合是ab、ac、bc。
def get_combinations(s, n, current, result):
    
    if n == 0:
        result.append(current)
        return 
        
    if len(s) == 0 and n > 0:
        return 
        
   
    char = s[0]      
    rest = s[1::]      
  
    get_combinations(rest, n - 1, current + char, result)
    
   
    get_combinations(rest, n, current, result)


s = input("请输入字符串: ")
n = int(input("请输入要取几个: "))
result = [] 


get_combinations(s, n, "", result)
print(" ".join(result))