# n=int(input("enter the number:-"))

# sum=0
# count=0

# for i in range(1,n):
#     if n%i==0:
#         count=i
#         sum=sum+i
#     elif sum==n:
#         print("this is unique number")

#     elif count==2:
#         print("this is prime number")
# print(sum)

# a="vansh"

# print(a[::-1])
b=''

# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
 # print(b)


# print(dir(str))

# a=1

# while a<=30:
#     print(a)
#     a+=1

# a=int(input("enter the number"))
# copy=a
# rev=0

# while a>0:
#     rev=rev*10+a%10
#     a=a//10

# if copy==rev:
#     print("it is pallindromic number")

# else:
#     print(rev)

# import random

# num=random.randint(1,11)

# tries=0

# while True:
#     guess=int(input("please guess the number:-"))

#     if guess==num:
#         tries+=1
#         print(f"correct number and you guess the number in {tries} tries")
#         break
    
#     elif num<guess:
#         print("go a little lower")
#         tries+=1

#     elif num>guess:
#         print("go a little high")
#         tries+=1
#     else:
#         tries+=1
#         print("you are wrong")


# print(num)

# def vansh(): 
#     print("i am the best trader in the world")

# vansh()
# a=int(input("enter the number:-"))
# b=int(input("enter the number:-"))
# def sum(a,b):
#     print(f"sum of the number is {a+b}")
# sum(a,b)
 
# a=[34,13,14,15,16,17,18]

# 1st way using index

# for i in range(len(a)):
#     print(a[i])

# # 2st way using index

# for i in a:
#     print(i)

# print(dir(list))

# l=[2,1,3,7,4,5,6]
# l.append(69)
# l.insert(3,33)

# print(l)

# l=[-11,-9,-3,-2,1,3,5,6,8,9]

# print("positive elements are")
# for i in l:
#     if i>=0:
#         print(i)
# print("negitive elements are")

# for i in l:
#     if i<0:
#         print(i)

# l=[1,2,3,4,5,32,21,-23,43,-30]

# sum=0

# for i in l:
#     sum+=i
# print(sum/len(l))

# l=[12,43,65,34,76,45,66]
# largest=l[0]
# second_largest=l[0]

# for i in l:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif i>second_largest:
#         second_largest=i
# print(f"the second largest value is {second_largest} and the largest value is {largest}")

# d={1:"vansh",2:43,3:"shivansh"}

# d[2]='aryan'

# del d[3]

# print(d)

# d={10:100,20:200,30:300,40:400,50:500}

# for i in d.values():
#     print(i)

# d={10:100,20:200,30:300,40:400,50:500}

# d2=d.copy() shallow copy
# d2[10]=1000

# print(d)
# print(d2)

# d1={10:100,20:200,30:300,40:400,50:500}

# d2={60:600,70:700,80:800,90:900,10:1000}

# for i in d2:
#     d1[i]=d2[i]

# print(d1)

# d1={10:100,20:200,30:300,40:400,50:500}

# sum=0

# for i in d1.values():
#     sum+=i

# print(f"the sum of di is {sum}")


# l=[1,1,1,2,2,2,2,3,3,5,5,5,5,5,3,3,8,9,7,7]

# d={}

# for i in l:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# class factory:
#     a=12  #attribute

#     def hello(self):
#         print("hello how are you")

#     print("vansh")

# obj=factory()
# print(obj.a)
# obj.hello()

# class Factory:
#     def __init__(self,metarial,zips,pockets):
#         self.metarial=metarial
#         self.zips=zips
#         self.pockets=pockets
    
#     def show(self):
#         print(f"your object details are {self.metarial},{self.zips},{self.pockets}")

# reebok=Factory("leather",2,4)

# campus=Factory("nylon",1,2)

# # print(f"reebok metrial :-{reebok.metarial}")
# # print(f"campus zips:-{campus.zips}")

# reebok.show()

# class animal:
#     name="lion"

#     def __init__(self,age):
#         self.age=age

#     def show(self):
#         print(f"your age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print("how are you brother")
#     @staticmethod
#     def static():
#         print("how are you")

# obj=animal(12)

# obj.show()
# obj.hello()
# obj.static()

# class vehicle:
#     fuel="cng,petrol,desiel"
    
# class car(vehicle):
#     pass

# obj=car()
# print(obj.fuel)


# class Animal:

#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"hello your name is {self.name} ")
# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#     def show(self):
#         print(f"hello your name and age is {self.name},{self.age} ")
    
    


# animal_1=Animal("lion")
# person_1=Human("vansh",20)

# person_1.show()

# class Factory:
#     def __init__(self,meterial,zips):
#         self.meterial=meterial
#         self.zips=zips
   
# class HRfactory(Factory):
#     def __init__(self, meterial, zips,color):
#         super().__init__(meterial, zips)
#         self.color=color

# class DLfactory(HRfactory):
#     def __init__(self, meterial, zips, color,pockets):
#         super().__init__(meterial, zips, color)
#         self.pockets=pockets

# obj=DLfactory("leather",2,"white,5")


# class Animal:
#     def show(self):
#         print("hello i am tiger")

# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj=Human()
# obj.show()


    