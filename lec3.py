# x: float = float(input("enter x:\n"));
# if x > 0:
#     # yes
#     print(x, "is positive")
# elif x == 0:
#     # yes
#     print(x, "is zero")
# else:
#     # everything was no
#     print(x, "is negative")
#
# x=0;
# y=100
# if not x==0 and y>100_000:
#     print("something")
pi: float = 3.14159
print(f"Pi: {pi}")
print(f"Pi: {pi:.2f}")
name1: str = "Alice"
#             12345
age1: int = 30
name2: str = "Laura Croft"
#             12345678901
age2: int = 31

print(f"Name: {name1:<20} {age1}")
print(f"Name: {name1:>20} {age1}")
print(f"Name: {name1:^20} {age1}")
print(f"Name: {name2:^20} {age2}")