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

# n = int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print("*",end=" ")
#         elif i<=n:
#             print("*",end=" ")
#     print()

# n = int(input())
# val = 1
# for i in range(n):
#     for j in range(n):
#         if i%2 == 0:
#             print("*",end=" ")
#         else:
#             print(val,end=" ")
#     print()
#     if i%2 != 0:
#         val +=1

# n = int(input(""))
# for i in range(n):
#     val = 1
#     for j in range(n):
#         if j%2 != 0:
#             print(val,end=" ")
#             val += 1
#         else:
#             print("*",end=" ")
#     print()

# n = int(input(""))
# for i in range(n):
#     val = 1
#     for j in range(n):
#         if i == j:
#             print("*",end=" ")
#         elif i>=j:
#             print(val,end=" ")
#             val +=1
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input(""))
# for i in range(n):
#     val1 = 1
#     val2 = 1
#     for j in range(n):
#         if i == j:
#             print("*",end=" ")
#         elif i>=j:
#             print(val1,end=" ")
#             val1 +=1
#         else:
#             print(val2,end=" ")
#             val2+=1
#     print()

# n = int(input(""))
# val = 1
# for i in range(n):
#     for j in range(n):
#         if i==j and (i%2==0 and j%2==0):
#             print("*",end=" ")
#         elif i==j and (i%2!=0 and j%2!=0):
#             print(val,end=" ")
#             val +=1 
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input("n: "))
# val = 1
# for i in range(n):
#     for j in range(n):
#         if (i+j) == n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val +=1

# n = int(input(""))   #S
# if n%2 == 0:
#     n1 = n+1
#     for i in range(n1):
#         for j in range(n1):
#             if i==0 or i==(n1)//2 or i==n:
#                 print("*",end=" ")
#             elif i<=n//2 and j==0:
#                 print("*",end=" ")
#             elif i>=n//2 and j==n1-1:
#                 print("*",end=" ")
#             elif i==n1-1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# else:
#     for i in range(n):
#         for j in range(n):
#             if i==0 or i==(n)//2 or i==n:
#                 print("*",end=" ")
#             elif i<=n//2 and j==0:
#                 print("*",end=" ")
#             elif i>=n//2 and j==n-1:
#                 print("*",end=" ")
#             elif i==n-1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()

# n = int(input(""))  //T
# if n%2 == 0:
#     n1 = n+1
#     for i in range(n1):
#         for j in range(n1):
#             if i==0 or j==n1//2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# else:
#     for i in range(n):
#         for j in range(n):
#             if i==0 or j==n//2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()


# n =int(input(""))  #I
# if n%2 != 0:
#     for i in range(n):
#         for j in range(n):
#             if i==0 or i==n-1 or j==n//2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# else: 
#     n1 = n+1
#     for i in range(n1):
#         for j in range(n1):
#             if i==0 or i==n1-1 or j==n1//2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()

# n=int(input(""))  #D
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input(""))  #D
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input(""))  #H
# if n%2 != 0:
#     for i in range(n):
#         for j in range(n):
#             if j==0 or j==n-1 or i==n//2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# else:
#     n1 = n+1
#     for i in range(n1):
#         for j in range(n1):
#             if j==0 or j==n1-1 or i==n1//2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()

# n = int(input(""))  #U
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=int(input(""))   #P
# for i in range(n):
#     for j in range(n-1):
#         if i==0 or j==0 or i==n//2:
#             print("*",end=" ")
#         elif i<=n//2 and j==n-2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input(""))  #R
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(1,n):
#     for j in range(n):
#         if j==0 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
