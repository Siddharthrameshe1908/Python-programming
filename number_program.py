# num = int(input("Enter the number: "))
# temp = num
# sum = 0
# power = len(str(num))
# while num != 0:
#     digit = num % 10
#     sum = sum + digit**power
#     num = num // 10
#     power-=1
# print("Disarium" if temp == sum else "Not disarium")

# num = 123
# temp = num
# add = 0
# prod = 1
# while num != 0:
#      digit = num % 10 #3 2 1
#      add = add + digit #0+3  3+2  5+1 = 6
#      prod = prod * digit #1*3  3*2  6*1 = 6
#      num = num // 10 #12 #1
# print("Spy number" if add == prod else "Not a Spy number")

# num = 8
# add = 0
# for i in range(1,num//2):
#      if(num % i == 0):
#           add = add + i
# if add == num:
#      print("Perfect number")
# else:
#      print("Not a perfect number")

# num = 1221
# temp = num
# rev = 0
# while num != 0:
#      digit = num % 10
#      rev = rev * 10 + digit
#      num //=10
# if temp == rev:
#      print("It is palindrom")
# else:
#      print("It is not palindrom")

# num = 1221
# temp = num
# rev = 0
# while num != 0:
#      digit = num % 10
#      rev = rev * 10 + digit
#      num //=10
#


# num = 11
# temp = num
# count = 0
# rev = 0
# for i in range(2,(num//2)+1):
#     if num % 2 == 0:
#         count +=1
# while temp != 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp = temp // 10
# if (count == 0) and (rev==num):
#     print("Paliprime number")
# else:
#     print("Not a Paliprime number")

# num = 131
# temp = num
# count = 0
# rev = 0
# while temp != 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     for i in range(2, (num // 2) + 1):
#         if num % 2 == 0:
#             count += 1
#     else:
#         temp = temp // 10
# if (count == 0) and (rev==num):
#     print("Paliprime number")
# else:
#     print("Not a Paliprime number")

#
# num = 131
# temp = num
# count = 0
# rev = 0
# for i in range(2, (num // 2) + 1):
#     if num % 2 == 0:
#         count += 1
#     else:
#         while temp != 0:
#             digit = temp % 10
#             rev = rev * 10 + digit
#             temp = temp // 10
# if (count == 0) and (rev==num):
#     print("Paliprime number")
# else:
#     print("Not a Paliprime number")
#
#
# num = 170
# temp = num
# rev = 0
# while temp != 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp = temp // 10
# print("palindrome" if rev == num else "Not palindrome")

# num = 170
# temp = num
# count = 0
# rev = 0
# for i in range(2, (num // 2) + 1):
#     if num % 2 == 0:
#         count += 1
#     while temp != 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp = temp // 10
# if (count == 0) and (rev==num):
#     print("Paliprime number")
# else:
#     print("Not a Paliprime number")


# num = 1101
# count = 0
# while num != 0:
#     d = num % 10
#     if (d == 1):
#         count +=1
#     num //= 10
# if count %2 == 0:
#     print("EVil number")
# else:
#     print("Not a Evil number")

# num = 145
# temp = num
# fres =0
# while num != 0:
#     digit = num % 10
#     res = 1
#     for i in range(1, digit+1):
#         res = res*i
#     fres = fres+res
#     num//=10
# if temp == fres:
#     print("Strong number")
# else:
#     print("Not a strong number"


# if __name__ == '__main__':
#     n = int(input().strip())
#     if(n % 2 != 0):
#         print("Weird")
#     elif((n % 2 == 0 and 2>=n<=5)or n>20):
#         print("Not Weird")


# def isnotPalidrone(num):
#     rev = 0
#     temp = num
#     while num != 0 :
#         rev = (rev*10)+(num%10)
#         num=num//10
#     return rev
# def isPrime(num):
#     if(num<=1):
#         return False
#     for i in range(2,(num//2)+1):
#         if num % i == 0:
#             return False
#     return True
# def RevisPrime(num):
#     Revs = 0
#     while num != 0 :
#         Revs = (Revs*10)+(num%10)
#         num=num//10
#     if Revs <= 1:
#         return False
#     for j in range(2,(Revs//2)+1):
#         if Revs % j == 0:
#             return False
#     return True
# def EMIRPchecker(value):
#     if rev == value and isPrime(value) and isPrime(isnotPalidrone(value)):
#         return print(f"{value} is a EMIRP number")
#     return "It is not a EMIRP number"
# value= int(input("Enter the number: "))
# EMIRPchecker(value)

# def checker(num):
#     while num > 9 or num == 7:
#         add = 0 
#         while num != 0:
#             sp = (num % 10)**2
#             add += sp
#             num //=10
#         num = add
#     if num == 1:
#         return True 
#     else: 
#         return False
# num = 76
# if checker(num):
#     print("It is automorphic number")
# else:
#     print("It is not automorphic number")
