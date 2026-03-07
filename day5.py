# evensum = 0
# oddsum=0
# for i in range(1,100,1):
#     if i%2==0:
#         evensum = evensum + i
#     else:
#         oddsum=oddsum+i
# print(evensum)
# print(oddsum)
n= int(input("enter the number - "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if  sum==n:
    print("perfect number")

    