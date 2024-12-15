from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, "index.html")

def calc(operator, operand1, operand2 = None):

    if(operator not in ['+', '-', '*', '/', '^', '%', "add", "sub", "mul", "div", "mod"]):
        return "Invalid operator \"{}\"".format(operator)
    if(type(operand1) not in [int, float]):
        try:
            raise Exception("Invalid number \"{}\"".format(operand1))
        except Exception as e:
            return e.__str__() 
    if(operand2 == None):
        if(operator in ["+", "add"]):
            return operand1
        elif(operator in ["-","sub"]):
            return 0-operand1
    if(type(operand2) not in [int, float]):
        try:
            raise Exception("Invalid number \"{}\"".format(operand2))
        except Exception as e:
            return e.__str__() 
    if(operator == '+' or operator == "add"):
        return operand1 + operand2
    elif(operator == '-' or operator == "sub"):
        return operand1-operand2
    elif(operator == '*' or operator == "mul"):
        return operand1*operand2
    elif(operator == '/' or operator == "div"):
        try:
            res = operand1/operand2
            return "{0:.1f}".format(res)
        except ZeroDivisionError as err:
            return "Division by zero"
    elif(operator == '%' or operator == "mod"):
        try:
            res = operand1%operand2
            return res
        except ZeroDivisionError as err:
            return "Division by zero"
    elif(operator == '^' or operator == "pow"):
        return operand1**operand2

def eval(expression_list):
    if(isinstance(expression_list, list) and len(expression_list) in (3, 2)):
        try:
            x1, x2, x3 = expression_list
        except ValueError as err:
            x1, x2 = expression_list
            x3 = None
        if(isinstance(x2, list)):
            x2 = eval(x2)
        if(isinstance(x3, list)):
            x3 = eval(x3)
        return calc(x1, x2, x3)
    else:
        try:   
            raise Exception("Failed to evaluate \"{}\"".format(expression_list))
        except Exception as err:
            return err.__str__()

def struct(unformatted_list):
    new_list = list()
    for i in range(len(unformatted_list)):
        if len(new_list) == 3:
            new_list = [new_list]
        if unformatted_list[i] in ('+', '-', "add", "sub"):
            new_list.insert(0, unformatted_list[i])
        else:
            new_list.append(unformatted_list[i])

    return eval(new_list)

def basic_calci(request):
    
    # Initialize display and result
    display = ""
    result = None

    # Handle POST request (when buttons are clicked)
    if request.method == "POST":
        # Get the current display value and the clicked button value
        display = request.POST.get("display", "")
        button = request.POST.get("button", "")

        # Check button behavior
        if button == "=":  # Evaluate the expression
            try:
            # Split display into a list of numbers and operators
                # For example, "6+9-8+7" -> ['6', '+', '9', '-', '8', '+', '7']
                tokens = []
                temp = ""
                for char in display:
                    if char.isdigit() or char == '.':  # Part of a number
                        temp += char
                    else:  # An operator
                        if temp:
                            tokens.append(temp)  # Add the number
                            temp = ""
                        tokens.append(char)  # Add the operator
                if temp:  # Add the last number
                    tokens.append(temp)

                # Convert string numbers to integers/floats
                for i in range(len(tokens)):
                    if tokens[i].isdigit():
                        tokens[i] = int(tokens[i])
                    elif '.' in tokens[i]:
                        tokens[i] = float(tokens[i])

                # Pass the list to struct for evaluation
                result = struct(tokens)  # Evaluate the structured expression
                display = str(result)  # Update display with result
            except Exception as e:
                result = "Error"
                display = ""
        elif button == "c":  # Clear display
            display = ""
        else:  # Append the button value to the display
            display += button

    # Render the page with updated display
    return render(request, "basic_calci.html", {"display": display, "result": result})

def scientific_calci(request):
    return render_to_string("<p>Scientific calculator under construction!</p>")