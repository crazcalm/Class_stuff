"""
I need to create a calculator like app that deals with 
+, -, *, /.

The plan is to use the eval() function. I would also like to make all
division into float division. 
"""
import sys


def whitespace(stack): #works
    """
    Gets rid of the white space in the list by mapping all the items
    in the list (with the exception of white space) to a list called
    tempt.
    
    input: String or list
    """
    
    tempt = []
    
    for char in stack:
        if char != " ":
            tempt.append(char)
            
    #print tempt        
    return tempt

#stack = ["1"," ", "3", " "]
#stack = "1 2 333 4 5 555"
#whitespace(stack)


def group_nums(stack): #works
    """
    This will take all the numbers that are next to each other in the 
    list and place them in the same index. 
    
    note: All items in this list are strings.
    """
    
    for index in range(len(stack)):
        """
        I needed a try clause because, when the last item in the stack
        is a digit, I do not want to check index +1, which doesn't exit.
        """
        try:
            if stack[index].isdigit() and stack[index + 1].isdigit(): # checks for digits
                stack[index] += stack[index + 1] # combines numbers
                del stack[index + 1] # deletes that copy of the number that was moved
                group_nums(stack) # Repeats the function with modified list
        except:
            pass
    
    #print stack
    return stack

#stack = ["1","2","3","*","4","5"]
#group_nums(stack)


def decimal_nums(stack): # works
    """
    Groups decimal numbers
    """
    
    for index in range(len(stack)):
        """
        I first check for decimals. If a decimal exist, I then check to
        see if the items before it and after it are numbers. If so, I combined
        those three elements to make a float.
        """
        try:
            if stack[index]== ".":
                if stack[index -1].isdigit() and stack[index +1].isdigit():
                    stack[index -1] += stack[index] + stack[index +1]
                    del stack[index] # deletes the decimal
                    del stack[index] # deletes the other number
                    
                    decimal_nums(stack)
        except:
            pass
        
    #print stack
    return stack

#stack = ["1",".","5","+", "4", ".", "9"]
#decimal_nums(stack)

def divide_by_float(stack): # works
    """
    Checks to see if the number after the division sign is a float.
    If not, we make it a float.
    """
    for index in range(len(stack)):
        """
        I use eval() to turn the item into python code so that
        it can its type can be checked.
        """
        if stack[index] == "/":
            if type(eval(stack[index +1])) == float: 
                pass
            
            elif type(eval(stack[index +1])) == int:
                stack[index +1] += ".0"
                
            else:
                print "What are you?!"
                
    #print stack
    return stack

#stack = ["1.5", "/", "2", "+", "5", "/", "5.0"]
#test = divide_by_float(stack)


def make_string(stack): # works
    """
    Transforms the list into a string so that it can be
    eval() in the future.
    """
    tempt = ""
    
    for char in stack:
        tempt += char
    
    #print tempt
    return tempt  

def input_test(user):
    """
    Test whether or not the input can be eval()
    """
    try:
        eval(user)
        
    except:
        
        print "This statement cannot be evaluated by my calculator."
        sys.exit()

def main():
    """
    Controls the flow of the program
    """             
    
    user = raw_input("\nPlease enter a mathematical sentance: ")
    
    input_test(user)
    
    user = whitespace(user)
    user = group_nums(user)
    user = decimal_nums(user)
    user = divide_by_float(user)
    user = make_string(user)
    
    #answer
    print "\nAnswer: ",eval(user)
    
if __name__ == "__main__":
    main()
     


