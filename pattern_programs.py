# n = 1
# sp = 0
# for row in range(4, 0, -1):
#     print(str('  ') * sp, end="")
#     for i in range(0, row):
#         print(n, end=' ')
#         n += 1
#     sp += 1
#     print()

# n = 1
# sp = 0
# for row in range(4, 0, -1):
#     #print('  ' * sp, end='')
#     for i in range(0, row):
#         print((' '*sp+str(n)),end = '')
#         #print(str(n), end=' ')
#         n += 1
#     sp += 1
#     print()

# sp = 2
# for upstar in range(1, 4):
#     #print(' '.join(' ' * sp+'*'*upstar))
#     print(('  ' * sp) + ('* ' * upstar))
#     sp -= 1

# s = "PYTHON"

# res =""
# for i in range(len(s)):  # 0, 1, 2, 3, 4, 5
#   res = res+s[i]
#   print(res)

# for i in range(len(s)):
#   print(s[ : i+1])

# n=9
# for row in range(1,4): # 1 2 3
#     L=[]
#     for i in range(3):
#         L.append(str(n))
#         n-=1
#     if(row % 2 == 0):
#             print(' '.join(L[::-1]))
#     else:
#             print(' '.join(L))


# n=1
# for row in range(1,5):
#     L=[]
#     for i in range(3):
#         L.append(str(n))
#         n+=1
#     if(row % 2 != 0):
#         print(' '.join(L[::-1]))
#     else:
#         print(' '.join(L))

# n = 1
# sp = 0
# for row in range(4, 0, -1):
#     print(sp*"  ",end='')
#     for i in range(0, row):
#         print(n,end=' ')
#         n += 1
#     print()
#     sp += 1    
 

# L = ('PYTHON',)
# s = L[0][::-1]
# print(s)
# for ei in range(4,0,-1):
#     print(s[0:ei:1])

# sp =4
# for row in range(1,6):
#     left = '*' * row + ' ' * sp
#     right = ' ' * sp + '*' * row
#     print(left, right)
#     sp-=1

# sp = 0
# for row in range(5,1,-1):  # 6,5,4,3,2
#   left = " ".join("*"* row + " "*sp)
#   right = " ".join(" "*sp + "*"* row)
#   print(left, right)
#   sp += 1
# sp = 4
# for row in range(1, 6):  # 1, 2, 3, 4, 5
#   left = " ".join("*"* row + " "*sp)
#   right = " ".join(" "*sp + "*"* row)
#   print(left, right)
#   sp -= 1


# sp = 4
# n = 1
# for row in range(1,6):
#     # print(' '*sp, end='')
#     # print(' '.join(str(n)*row))
#     print(' '*sp + (str(n)+' ')*row)
#     n+=1
#     sp-=1

# n = 5
# sp = 0
# for row in range(1,6):
#     print('  '*sp + (str(n)+' ')*n)
#     sp+=1
#     n-=1
#
# n = 5
# for row in range(1,6):
#     print(f"{(str(n)+' ')*n:>10}")
#     n-=1