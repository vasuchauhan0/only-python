# nested loop =  a loop within another loop (outer , inner)
#                outer loop:
#                    inner loop:


rows=int(input("enter the # of rows : "))
columns=int(input("enter the # of columns : "))
symbol=int(input("enter the symbol to use : "))

for i in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()