# python-lec3-09.04.24

in the lecture:

1) recap last lecture and solved hw2.
2) elif
3) if conditions-operators:

    1) "and" vs & : & =bitwise AND (working on the number in binary)
    2) short circuit in "and","or" operators: (condition1 **and** condition2 )=if the first condition is false, python
       will not check the other conditions in the if.
    3) and not balance==100_000 = balance!=100_000
    4) operators:
        1. and (&&): a <= 10 >= 12 / a >= 10 and a <= 12
        2. or (||)
        3. not (!=)
        4. is (==)
    5) match-case:
        1. match day=switch day
        2. without break-because the indentation
        3. case _: = default:
        4. merge cases: case 10 | 11| 12
4) print format: https://docs.python.org/3/tutorial/inputoutput.html

"your name is {x}, your age is {y}."

```    
print( **f**"your name is {x}, your age is {y}.")
```

### options:

1) to print only 2 digits after the '.':

         print(f"Pi:{pi:.2f}")

2) to align the string:
    1) to the left <:
    ```
        print(f"Name: {name1:<20} {age1}")
    ```
    2) to the right >:

    ```
    print(f"Name: {name1:>20} {age1}")
    ```

    3) to the center ^:
    ```
   print(f"Name: {name1:^20} {age1}")
    ```
    4) number to percentage: 0.5 to 50%:
       ```
       print(f"{prec:%}")
       ```
    5) percentage with 2 digits after the '.':

    ```
   print(f"percentage 2 digits after the .: {perc:.2%}")
   ```