# Assignment 3: RPN Calculator

# Calculator taking an expression in Reverse Polish Notation (RPN) and returning the result of calculation
# This calculator assumes that Input values only have the required format specified in assignment requirements
def rpn_calculator(expression):
    # Converting expression to list, ignoring spaces, making it easier to iterate
    incoming_list = expression.split()
    # Initiating stack (represented as list)
    calculating_stack = []
    # Loop iterating over input, making calculations when necessary
    for i in range(len(incoming_list)):
        # Perform calculation if iteration is operator
        if incoming_list[i] in ["+", "-", "*", "/"]:
            # Store result in temporary Variable so that calculation elements can be popped first
            tmp = perform_calc(incoming_list[i], calculating_stack.pop(), calculating_stack.pop())
            # Pushing result to Stack
            calculating_stack.append(tmp)
        else:
            # Pushing element to Stack if no operator
            calculating_stack.append(int(incoming_list[i]))
    # Returning remaining value
    return calculating_stack[0]

# Auxiliary Function to perform single calculations
def perform_calc(op, nr2, nr1):
    if op == "+":
        return nr1 + nr2
    elif op == "-":
        return nr1 - nr2
    elif op == "*":
        return nr1 * nr2
    elif op == "/" and nr2 == 0:
        return "Error: Division by zero"
    elif op == "/":
        return nr1 / nr2


# Testing
print(rpn_calculator("2 3 +")) # 5
print(rpn_calculator("3 4 + 2 *")) # 14
print(rpn_calculator("5 1 2 + 4 * + 3 -")) # 14
print(rpn_calculator("15 7 1 - 1 - /")) # 3
print(rpn_calculator("4 0 /")) # Error