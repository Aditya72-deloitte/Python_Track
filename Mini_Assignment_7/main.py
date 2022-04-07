while True:
    # Taking input in Form of String
    Input = input("Enter the formula : ")

    # splitting the input string on spaces
    input_list = Input.split()

    # printing the input list
    print(input_list)

    try:
        # if User wants to quit While being inside a program
        if Input == 'leave':
            break

        # taking the operator into diffrent variable
        operator = input_list[1]

        # Converting each Str number into float
        float_num1 = float(input_list[0])
        float_num2 = float(input_list[2])

        if len(input_list) == 3 and type(float_num1) == float and type(float_num2) == float:
            #logics
            if operator == '+':
                res = float_num1 + float_num2
                print(res)

            elif operator == '-':
                diff = float_num1 - float_num2
                print(diff)

            # Else case exception
            else:
                raise Exception

# if the length of input is not equal to 3
        elif len(input_list) != 3:
            raise Exception

    # if INput is not in proper or without any operator
    except Exception:
        print("FormulaError")

    except ValueError:
        print("Operation cannot be performed")
