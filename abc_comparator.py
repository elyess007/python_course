x=input("set your id of the verification: \n")
if(int(x)==12345):  # cast string to int
    print("Correct")
    a=input("set your number here--->")
    b=input("set your second number here--->")
    c=input ("1 and 2 and 3 and 4 are + - * / here--->")
    d="a is greater than b and c"
    e="b is greater than c and a"
    f="c is greater than a and b"
    g="they are all equal"
    h=( str(a)+" and "+ str(b) +" are equal and greater than "+ str(c))  # concaténation 
    i=( str(b)+" and "+ str(c) +" are equal and greater than "+ str(a))
    j=( str(c)+" and "+ str(a) +" are equal and greater than "+ str(b))
    if(a>b>c):
        print(d)
    if(b>c>a):
        print(e)
    if(c>a>b):
        print(f)
    if(a==b and b==c):
        print(g)
    if(a==b and c>a):
        print(h)
    if(b==c and c>a):
        print(i)
    if(c==a and a>b):
        print(j)
else:
    print("Incorrect")