# Logical operators = evaluate multiple conditions(or,and, not)
#                     or=at least one condition must be True
#                     and=both conditions must be True
#                     not =inverts the conditions(not False,not True)



temp=int(input("enter the temperature :- "))
is_sunny=True

if temp>=28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY ")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY ")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is cloudy ")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside") 
    print("It is cloudy")





# temp=int(input("enter the temprature :- "))
# is_raining=False

# if temp>35 or temp<0 or is_raining:
#     print("the outdoor event is cancelled")
# else:
#     print("outdoor event is still scheduled 😂"