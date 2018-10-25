#Gabriel Harrison
#10/3/2018
#python password

#get user input and check for errors
def get_input(message):
    var_value=input(message)
    return var_value
    
    
def get_int_input(message):
    var_value=input(message)
    if var_value.isdigit():
        var_value=int(var_value)
        return var_value
    else:
        display_output("That was not a number")
        get_in_input(message)
    


#solve for addition,subtraction,division,multiplication
def add(num1,num2):
    sum_plus= num1 + num2
    return sum_plus
        
    

def subtract(num1,num2):
    difference= num1 - num2
    return difference


def multiply(num1,num2):
    product= num1 * num2
    
def divide(num1,num2):
    if num !=0:
        quotiant=num2/num1
        return quotiant
    else:
        return 0

    


#remainder
def remainder(num1,num2):
    if num1 !=0:
        remainder=num2 % num1
        return remainder
    else:
        return 0


#check math
def check_math(test_valuce, operator, num1, num2):
    if operator == "+":
        checked_value=num1 + num2
    elif operator == "-":
        checked_value= num1 - num2
    elif operator == "%":
        checked_value == num1 % num2
    elif operator == "/":
        checked_value= num1 / num2
    elif operator == "*":
        checked_value= num1 * num2
    return checked_value
    





#display answer
def display_output(message):
    print(message)
#main
def main():
    num1 = get_int_input("Please enter a number.")
    num2 = get_int_input("Please enter a number.")
    operator = get_input("What is your operation? Enter + - * / or % only.")

    if operator == "+":
        test_value=add(num1,num2)
    elif operator == "-":
        test_value=subtract(num1,num2)
    elif operator == "*":
        test_value=multiply(num1,num2)
    elif operator == "/":
        test_value=divide(num1,num2)
    elif operator == "%":
        test_value=remainder(num1,num2)
    else:
        display_output("This is not one of the correct operators")
        main()
    checkedvalue=check_math(test_value, operator, num1, num2)
    
    if test_value == checkedvalue:
        display_output("After a second check the correct answer is" +str(test_value)
    else:
        display_output("something in the calculation was wrong try it again")
        main()


main()                         
                         
                         
                        
