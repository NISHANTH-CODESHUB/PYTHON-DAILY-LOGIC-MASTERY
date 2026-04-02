num=int(input("enter a number:"))
rev=0
org=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==org:
    print("the given number is palindrom")

else:
    print("the given number is not a palindrome")        