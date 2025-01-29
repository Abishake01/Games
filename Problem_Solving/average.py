#How to find the average of N numbers in python
n = int(input())#Get the number of inputs
tot=0
for i in range (n):
    num=float(input())
    tot+=num # Add total number of inputs
    
avg=tot/n  # Total number / number of inputs
print(avg)