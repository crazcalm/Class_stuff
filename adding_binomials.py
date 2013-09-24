"""
Adding binomial numbers
"""


"""
code from binomial_number_conversion
"""
"""
The code from my orginal attempt to add binomials
"""
def same_length(num1, num2): #works
    
    #Adding an extra zero to the end to make adding easier.
    num1 += "0"
    num2 += "0"
    
    if len(num1)<= len(num2):
        
        while len(num1) < len(num2):
            num1+= "0"
        
    else: #the case of len(num1)> len(num2)
        
        while len(num2) < len(num1):
            num2 += "0"
    #print "testing same_length function: \n", num1, "\n", num2, "\n"       
    return num1, num2


def add_one(num1, index): #works
    """
    Adds one to binomial string num1 when needed
    """
    
    if num1[index] == 0:
        
        num1[index] = 1
        
    elif num1[index] == 1:
        
        num1[index] = 2
        
    elif num1[index] == 2:
        
        num1[index] = 3
        
    return num1

#print add_one([2,1,0,1,0,1,2,1], 4)

def create_list(number): #works
    """
    makes the user number into a list of numbers
    """
    
    results = []
    
    for num in number:
        results.append(int(num))
        
    return results

"""
Back to the new code
"""

def adding_binomials(numbers, current_total = "0"):
    """
    Needs to take a list of binomials numbers in the form of a string and add 
    them.
    """
    
    if len(numbers)==1:
        #print numbers[0], "This answer is being returned?"
        pass
        
    else:
        num1 = numbers[0]
        num2 = numbers[1]
        
        num1, num2 = same_length(num1, num2)
    
        num1 = create_list(num1)
        num2 = create_list(num2)
    
        #print "\n\nnum1: ", num1
        #print "num2: ", num2
        
        #will hold answer
        total = []
    
        for index in range(len(num1)):
        
            tempt = num1[index] + num2[index]
        
            if tempt > 1: #cases tempt == 2, or 3
                num1 = add_one(num1, index +1)
            
                tempt = tempt % 2
            
            else:
                pass
        
            total.append(tempt)
            
        #Need to make the answer into a string
        tempt_str = ""
        
        for num in total:
            
            tempt_str += str(num)
            
        """
        I want to delete the first item in the numbers(list)
        and replace numbers[0] with tempt_str
        """
        
        del numbers[0]
        
        numbers[0] = tempt_str
        
        adding_binomials(numbers)
        
    return numbers[0]

"""
End of Binomial_number_converstion code
"""

def formatting_user_input(user):
    """
    Takes the leading spaces out of the user's input:
    """
    
    for index in range(len(user)):
        """
        Converting the number from string to integer and then back to
        string will get rid of the leading space.
        """
        tempt = int(user[index])
        tempt = str(tempt)
        user[index] = tempt
    
    #print user
    return user


def main():
    """
    Takes the users input and send it to the adding_binomials function
    """

    print "\nPlease enter the binomial numbers that you would like to add."
    print "Note: seperate the binomial number by a comma (ex. 111, 101, ...)"

    user = raw_input("\nEnter numbers here: ").split(",")
    user = formatting_user_input(user)
    results = adding_binomials(user)

    print "\nThe answer is:", results, "\n"

