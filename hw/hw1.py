idNumber1: str = input("enter yor id:");
lastName1: str = input("enter your last name:");
firstName1: str = input("enter your first name:");
height1: float = float(input("enter your height:"));
year1: int = int(input("enter birthday year:"));

idNumber2: str = input("enter your id:");
lastName2: str = input("enter your last name:");
firstName2: str = input("enter your first name:");
height2: float = float(input("enter your height:"));
year2: int = int(input("enter birthday year:"));

idNumber3: str = input("enter yor id:");
lastName3: str = input("enter your last name:");
firstName3: str = input("enter your first name:");
height3: float = float(input("enter your height:"));
year3: int = int(input("enter birthday year:"));

idWidth = 5
lastNameWidth = 10
firstNameWidth = 10
height_width = 10
year_width = 4

print(
    f"#id: {idNumber1:<9} name: {lastName1:<{lastNameWidth}}, {firstName1:<{firstNameWidth}} height: {height1:<{height_width}.2f} year-of-birth: {year1:>{year_width}}")
print(
    f"#id: {idNumber2:<9} name: {lastName2:<{lastNameWidth}}, {firstName2:<{firstNameWidth}} height: {height2:<{height_width}.2f} year-of-birth: {year2:>{year_width}}")
print(
    f"#id: {idNumber3:<9} name: {lastName3:<{lastNameWidth}}, {firstName3:<{firstNameWidth}} height: {height3:<{height_width}.2f} year-of-birth: {year3:>{year_width}}")
