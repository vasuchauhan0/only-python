# Do some code only IF some condition is true
# else do something else

age=int(input("Enter your age :-"))

if age>=100:
    print("You are too old to sign up")
elif age>=18:
    print("You are signed up!")
elif age<0:
    print("you haven't born yet!")

else:
    print("you must be 18+ to sign up!")