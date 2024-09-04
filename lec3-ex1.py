a: int = int(input("enter the first number:\n"));
b: int = int(input("enter the second number:\n"));
c: int = int(input("enter the third number:\n"));
if a > b and a > c:
    # yes
    print(a)
elif b > c:
    # yes
    print(b)
else:
    # everything was no
    print(c)
