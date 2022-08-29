"""    Arithmetic Operators """
# a=float(input("Enter the value of a:"))
# b=float(input("Enter the value of b:"))
# a,b=[int(x) for x in input('Enter the value of a and b: ').split()]
# print(f"The value of {a} + {b} is {a+b}")
# print(f"The value of {a} - {b} is {a-b}")
# print(f"The value of {a} * {b} is {a*b}")
# print(f"The value of {a} / {b} is {a/b}")
# print(f"The value of {a} % {b} is {a%b}")
# print(f"The value of {a} ** {b} is {a**b}")

""" Floor Division """
# c=4//2
# print(c) 
# d=4//2.0
# print(d) 
# e=5//2
# print(e)
# f=5.0//2
# print(f) 
# g=5.0/2
# print(g) 

""" Assignment Operator  """
# a=2 ; b=3
# a=a+b
# print(a) # a=2+3  a=5
# a=a+a
# print(a) # a=5+5 a=10


# a=5
# a+=3
# print(a) # a=a+3 a=5+3 a=8
# a-=2
# print(a) # a=a-2  a=8-2  a=6
# a*=4
# print(a) # a=a*4 a=6*4  a=24
# a/=2
# print(a) # a=a/2  a=24/2  a=12.0
# a**=2
# print(a) # a=a**2  a=12.0**2  a=144.0

# p=int(input("Enter the value of p:"))
# print(f"The value of p is {p}")
# p+=2   
# print("The value of p after p+=2 is {}".format(p))
# p-=4 
# print("The value of p after p-=4 is {}".format(p))
# p*=6 
# print("The value of p after p*=6 is {}".format(p))
# p**=2 
# print("The value of p after p**=2 is {}".format(p))
# p/=2 
# print("The value of p after p/=2 is {}".format(p))

"""     Relational/Comparision Operators   """
# a=int(input("Enter the Value of a:"))
# b=int(input("Enter the Value of b:"))
# print(f"The value of {a} < {b} is {a<b}")
# print(f"The value of {a} > {b} is {a>b}")
# print(f"The value of {a} <= {b} is {a<=b}")
# print(f"The value of {a} >= {b} is {a>=b}")
# print(f"The value of {a} == {b} is {a==b}")
# print(f"The value of {a} != {b} is {a!=b}")

# a=int(input("Enter the Value of a:"))
# b=int(input("Enter the Value of b:"))
# print("The value of %d<%d=%d"%(a,b,a<b))
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a<b))
# print("The value of a=%d , b=%d and a>b=%d"%(a,b,a>b))
# print("The value of a=%d , b=%d and a<=b=%d"%(a,b,a<=b))
# print("The value of a=%d , b=%d and a>=b=%d"%(a,b,a>=b))
# print("The value of a=%d , b=%d and a==b=%d"%(a,b,a==b))
# print("The value of a=%d , b=%d and a!=b=%d"%(a,b,a!=b))

""" Logical Operator  """
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# print("The value of a<b and b>a is {}".format(a<b and b>a)) 
# print("The value of a>b and a<b is {}".format(a>b and a<b)) 
# print("The value of a!=b and a==b is {}".format(a!=b and a==b)) 
# print("The value of a==b or a>b is {}".format(a==b or a>b)) 
# print("The value of a!=b or a<b is {}".format(a!=b or a<b)) 
# print("The opposite of {}=={} is {}".format(a,b,not a==b)) 
# print("The opposite of {}!={} is {}".format(a,b,not a!=b))

""" Bitwise Operator  """
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# c=int(input("Enter the value of c:"))
# print("The value of {} & {} is {}".format(a,b,a&b))
# print("The value of {} | {} is {}".format(a,b,a|b))
# """Note: The formula for Negation (~) is -(value+1)    """
# print("The value of ~{} is {}".format(a,~a))
# print("The value of ~{} is {}".format(c,~c))



""" Identity Operator   """
# a = 20
# b = 20

# if ( a is b ):
#    print ("a and b have same identity")
# else:
#    print ("a and b do not have same identity")

# if ( id(a) == id(b) ):
#    print ("a and b have same identity")
# else:
#    print ("a and b do not have same identity")


# x = 5
# print(type(x) is int)
# print(type(x) is not float)
# print(type(x) is  float)
# y = 3.23
# print(type(y) is not float)
# print(type(y) is int)
# print(type(y) is float)


"""   Membership Operator  """
# name=['Thilo','Prav','Ani','Azi','Vam','pav','Sandy','Sari',
#        'mune','ram','Chait','lah','udayi','nar','liki']
# print('Thilo' in name)
# print('pav' in name)
# print('pune' in name)
# print('srav' in name)
# print('Azi' in name)
# print('brahma' in name)
# print('Anu' not in name) 
# print('Preti' not in name) 
# print('Ravi' not in name) 
# print('lah' not in name)
# name.sort()
# print(name)
# name=['p','n','Y','t','o','H']
# name.sort()
# print(*name) 
# name.sort(reverse=True)
# print(name) #  t p o n Y H
# for i in name:
#     print(i)

""" Shift Operator (>>Right /2  and << Left *2) """
# a=20
# print(a>>1)
# print(a>>2)
# print(a>>3)
# print(a>>4)
# b=4
# print(b<<1)
# print(b<<2)
# print(b<<3)