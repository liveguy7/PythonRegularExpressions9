import re
from socket import CAPI

def vowelBE(txt):
    tmp = bool(re.findall('[/^[aeiou]$|^([aeiou]).*\1$/]', txt))
    return tmp

def test(txt):
    tmp1 = bool(re.findall('[AEIOUaeiou] [AEIOUaeiou]', txt))
    return tmp1

str1 = "a red white purple f"
str2 = "ared white orangeu"
print(vowelBE(str1))
print(vowelBE(str2))
print(test(str1))
print(test(str2))

def longestItem(*args):
    return max(args, key=len)

print(longestItem('One','Two','Three'))
print(longestItem([1,2,3],[1,2,3,4],'1'))
print(longestItem([1],{1,2,3},'90'))
print(longestItem([1,2,90],'90','Jello Store'))

str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
str2 = "Enter at 1 20 Kearny Street. The security desk 1 6. Other 90 09 90"
removeLower = lambda txt : re.sub('[a-z]','',txt)
result = removeLower(str1)
print(result)

newTxt = re.sub(r'(?<=\d)\s(?=\d)','',str2)
print(newTxt)

print("Input number of data sets:")
class C(int):
    def __add__(self,n):
        return C(int(self)+int(n))
    def __sub__(self,n):
        return C(int(self)-int(n))
    def __mul__(self,n):
        return C(int(self)*int(n))
    def __truediv__(self,n):
        return C(int(int(self)/int(n)))
   
for _ in range(int(input())):
  print("Input an expression:")
  print(eval(re.sub(r'(\d+)',r'C(\1)',input()[:-1])))

def capitalWordsSpaces(str1):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', str1)

print(capitalWordsSpaces('Python'))
print(capitalWordsSpaces('PythonExercises'))
print(capitalWordsSpaces('JelloStoreFoodDrinkArea'))

items = ["jello (tmp)", "store (test)", "hello (gell)", "cave (man)"]
for item in items:
    print(re.sub(r' ?\([^)]+\)','',item))

text = "The quick brown fox jumps over the lazy dog in the store near the jello aisle"
shortword = re.compile(r'\W*\b\w{1,3}\b')
print(shortword.sub('',text))

def isDecimal(num):
    tmp = re.compile(r'^[0-9]+(\.[0-9]{1,2})?$')
    result = tmp.search(num)
    return bool(result)

print(isDecimal('23.23'))
print(isDecimal('34.23299'))
print(isDecimal('90.9'))
print(isDecimal('90'))











