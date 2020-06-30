#Vending candy Machine
#available candy =5
#break
av=5
x=int(input("How many Candies do you want?"))
i=1
while i<=x:
    if i>av:
        print("Out of stock")
        break
    print("Candy")
    i+=1
#Values from 1-100 excluding those divisible by 3
#continue
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

#To print odd numbers
#pass
#osascript -e 'quit app "Calendar"'b=int(input("Enter your number:"))
for i in range(1,101):
    if i%2==0:
        pass
    else:
        print(i)
