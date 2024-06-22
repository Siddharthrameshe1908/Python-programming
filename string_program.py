# s = input("Enter the string: ")
# res = ""
# count = 0
# for char in s:
#     if char not in 'AEIOUaeiou' and char not in res:
#         res = res + char
# print(res)

# s = input("Enter the string: ")
# res = ""
# res2 = ""
# count = 0
# for char in s:
#     if char in 'AEIOUaeiou':
#         res = res + char
#     elif char not in 'AEIOUaeiou':
#         res2 = res2 + char
# print(res)
# print(res2)

# s = input("Enter the string: ")
# res = ""
# count = 0
# for char in s:
#     if char in 'AEIOUaeiou':
#         res = res + char
# print(res)
#
#
# s = input("Enter the string: ")
# res = ""
# count = 0
# for char in s:
#     if char not in 'AEIOUaeiou':
#         res = res + char
# print(res)

# def onlyvowels(string):
#     res = ''
#     for char in string:
#         if char in 'AEIOUaeiou':
#             res = res + char
#     return res
# def onlyconsonents(string):
#     res = ''
#     for char in string:
#         if char not in 'AEIOUseiou':
#             res = res + char
#     return res
# s = input("Enter the string: ")
# print(onlyvowels(s))
# print(onlyconsonents(s))

# s = 'abcdABCD 12@'
# res = ''
# for char in s:
#     if 'A' <= char <= 'Z':
#         res += chr(ord(char)+32)
#     elif 'a' <= char <= 'z':
#         res += chr(ord(char)-32)
#     else:
#         res += char
# print(res)
#
# s = 'pYthon PrograMMing'
# res = ''
# for i in range(0,1):
#     if 'a' <= s[i] <= 'z':
#         res += chr(ord(s[i])-32)
#     else:
#         res += s[i]
# for i in range(1,len(s)):
#     if 'A' <= s[i] <= 'Z':
#         res += chr(ord(s[i])+32)
#     else:
#         res += s[i]
# print(res)

# s = 'LiFe is Beautiful'
# res = ''
# c = 0
# for char in s:
#     if 'A' <= char <= 'Z':
#         res += chr(ord(char)+32)
#     else:
#         res += char
# for i in res:
#     if res.count(i) == 1:
#         c += 1
# print(c)

# s = 'PYTHON'
# d = {}
# for i in range(len(s)):
#     d[s[i]] = i
# print(d)

# def factorial(num):
#     fres = 0
#     while(num != 0):
#         rem = num % 10
#         res = 1
#         for f in range(1, rem+1):
#             res *= f
#         fres += res
#         num //=10
#     return fres
# num = int(input("Enter the number: "))
# print('Strong num' if factorial(num) == num else 'Not a strong num')

# s = 'WE ARE WHAT WE ARE AND WE ARE AMAZING'
# words = s.split()
# print(words)
# c = 0
# res = []
# for i in range(len(words)):
#     if words.count(words[i]) > c:
#         c = words.count(words[i])
# print(c)
# for j in range(len(words)):
#     if words.count(words[j]) == c and words[j] not in res:
#         print(words[j],end = ' ')
#         res.append(words[j]) 


# s = "WE ARE LEARNING PYTHON AND NOT LEARNING JAVA"

# d = {}
# words = s.split()
# for word in words:
#     d[word] = len(word)
    
# print(d)
# max_length = min(d.values())
# for item in d:
#     if d[item] == max_length:
#         print(item)  

# s = "WE ARE LEARNING PYTHON AND NOT LEARNING JAVA"
# max_length = 0
# store = []
# words = s.split()

# for word in words:
#     if len(word)> max_length:
#         max_length = len(word)

# for item in words:
#     if len(item) < max_length and item not in store:
#         store.append(item)
# print(store)
