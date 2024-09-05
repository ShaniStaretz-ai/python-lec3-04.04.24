grade: int = int(input("enter grade:\n"));

if 0 <= grade <= 40:
    print("try harder next time...")
elif 41 <= grade <= 60:
    print("you're getting there, need some more work")
elif 61 <= grade <= 80:
    print("good pretty")
elif 81 <= grade <= 95:
    print("!awesome");
elif 96 <= grade <= 100:
    print("excellent!!! You're a Star!");
else:
    print("grade illegal")

match grade:
    # case 10 | 11 | 12:
    case _ if 0 <= grade <= 40:
        print("try harder next time...")
    case _ if 41 <= grade <= 60:
        print("you're getting there, need some more work")
    case _ if 61 <= grade <= 80:
        print("good pretty")
    case _ if 81 <= grade <= 95:
        print("!awesome");
    case _ if 96 <= grade <= 100:
        print("excellent!!! You're a Star!");
    case _:
        print("grade illegal")
