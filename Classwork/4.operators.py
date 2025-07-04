#Arthmatic operators
a=20
b=10
print("Addition(+):",a+b)
print("Substraction(-):",a-b)
print("Multiplication(*):",a*b)
print("Division(/):",a/b)
print("floor division(//):",a//b)
print("Modulus(%):",a%b)
print("Exponentiation(**):",a**b)


#Comparision operators
a=20
b=10
print("Equal to(==):",a==b) #Equal to(==): False
print(" not Equal to(!=):",a!=b) #not Equal to(!=): True
print("Greater than(>):",a>b) #Greater than(>): True
print("Less than(<):",a<b)#Less than(<): False
print("Greater than or equal to(>=):",a>=b)#Greater than or equal to(>=): True
print("Less than or equal to(<=):",a<=b)#Less than or equal to(<=): False


#3.Assignment Operators
a=20
b=10
print("Assign(=):",a) #Assign(=): 20
a+=b 
print("Add & Assign(+=):",a) #Add & Assign(+=): 30
a-=b
print("Subtract & Assign(-=):",a) #Subtract & Assign(-=): 20
a*=b
print("Multiply & Assign(=):",a) #Multiply & Assign(=): 200
a/=b
print("Division & Assign(/=):",a) #Division & Assign(/=): 20.0
a//=b
print("Floor Divison & Assign(//=):",a) #Floor Divison & Assign(//=): 2.0
a%=b
print("Modulus & Assign(%=):",a) #Modulus & Assign(%=): 2.0
a**=b
print("Exponentiate & Assign(*=):",a) #Exponentiate & Assign(*=): 1024.0


#4.Logical Operators (Using Logic Gates)
print("AND operator:",a>b and b>a) #AND operator: False
print("OR operator:",a<b or b<a) #OR operator: True
print("NOT operator:",not a>b) #NOT operator: False


#5.Membership Operators
a = [1,2,3]
print("In operator:",1 in a) #In operator: True
print("Not In operator:",5 not in a) #Not In operator: True


#6.Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Is operator:",a is b) #In operator: True
print("Is Not operator:",a is not c) #Not In operator: True


#7.BitwiseOperators

x=4                                 #Binary= 0 1 0 0
y=6                                 #Binary= 0 1 1 0
                                             
print("AND(&):", x&y)               # 0 1 0 0 = 4
print("OR(|):", x|y)                # 0 1 1 0 = 6
print("XOR(^):", x^y)               # 0 0 1 0 = 2       Opposite reactions can be True
print("NOT(~):", ~x)                #  [~n = -(n + 1)]
print("NOT(~):", ~y)                #  [~n = -(n + 1)]
