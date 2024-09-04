a: int = int(input("enter the age:\n"));
# if a == 10 or a == 11 or a == 12:
# if 10> = a <= 12:
#     print("young")
# elif a == 13 or a == 14 or a == 15:
#     print("teenager")
# elif a == 16 or a == 17 or a == 18:
#     print("almost adult")
# elif a == 19 or a == 20 :
#     print("adult")
# else:
#     print("no in range")


match a:
    # case 10 | 11 | 12:
    case a if  a>=10 and a<=12:
        print("young");
    case 13 | 14 | 15:
        print("teenager")
    case 16 | 17 | 18:
        print("almost adult")
    case 19 | 20:
        print("adult")
    case _:
        print("no in range")
