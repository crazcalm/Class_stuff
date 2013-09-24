"""
Binomial multiplication
"""
from adding_binomials import adding_binomials


def multiplication(numbers):
    """
    Converts multiplication problems into their addition counterparts,
    and then sends them to the adding_binomials function.

    input: list of strings
    ouput: list of strings
    """

    results = "Where is the answer?"
    if len(numbers) == 1: 
        """
        When there is only one item left in the list, that item should be the
        final answer.
        """
        pass
    
    elif len(numbers) > 1:
        
        num1 = numbers[0]
        num2 = numbers[1]
        
        #logic for converting from multiplication to adding
        adding_list = []

        for index in range(len(num2)):
            if num2[index] == "0":
                pass
                
            elif num2[index] == "1":
                
                # figuring out how many zeros I need.
                tempt = "0" * index
                # adding number to list
                adding_list.append(tempt + num1)
            
            #print "test: adding list",adding_list 
        # the answer for num1 * num2
        answer = adding_binomials(adding_list)

        # Modifying the original list
        del numbers[0]
        numbers[0] = answer

        # Running this function again
        multiplication(numbers)
    #returns final answer
    results = numbers[0]
    #print results, "Are you being printed?"
    return results

"""
code from adding_binomials
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
"""
end of code from adding_binomials
"""

def main():
    """
    Takes the user input and controls the flow of the
    program
    """

    print ("\nPlease enter the binomial numbers that you would like to" +
    " multiply")

    print "Note: Seperate the numbers by a comma (ex. 101, 111, ...)"

    user = raw_input("\nEnter numbers here: ").split(",")
    user = formatting_user_input(user)

    answer = multiplication(user)

    while answer[-1]=="0":
        answer = answer[:-1]

    print "\nThe answer is: ",answer, "\n"
    

main()