# format specifiers = {value: flags} format a value based on what
#                         flags are intrested

# .(number)f = round to that many decimal places (fixed point)
# : (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
#:> = right justify
# :^ = center align
# use a plus sign to indicate positive value
# place sign to leftmost position
# = insert a space before positive numbers
#  :, = comma separator

price1=23.23456432
price2=534.345
price3=234.3879

print(f"price 1 is : {price1:.2f} ")

print(f"price 2 is : {price2:.2f} ")

print(f"price 3 is : {price3:.2f} ")