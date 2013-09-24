"""
The Goal is to write binary adding, subtraction, multiplication, and division.
"""

"""
Convert numbers to binary
"""

def find_starting_power(number):
    
    """
    Finds the largest power of 2 such that number - 2^power > 0
    """
    power_of_2 = 1
    
    while number > power_of_2:
        power_of_2 *= 2
        
    answer = power_of_2/2
    
    #print answer
    return answer

#find_starting_power(13)

def divisors_of_number(number, divisor):
    
    """
    This function returns a list of all the powers of 2
    that divide the current number.
    
    Return a list of those divisors
    """
    
    results = []
    
    while number > 0:
        
        #print number
        if number >= divisor:
            
            number = number - divisor
            results.append(divisor)
        
        else: 
            divisor = divisor /2
            
    #print results
    return results

#divisors_of_number(13,8)
        
def convert_to_binary(numbers):
    
    """
    Takes a list of numbers that are powers of 2 and returns the
    binary form of each number in the list of strings
    """
    
    results = []
    
    for num in numbers:
        
        #num/2 == number of zeros needed for binary form
        zeros = "0"
        
        tempt = num
        count = 0
        while tempt >1:
            tempt = tempt/2
            count +=1
        
        num_of_zeros = count    
        
        binary_num = zeros * num_of_zeros + "1"
        #print binary_num
        results.append(binary_num)
        
    #print results
    return results


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

#list = ["0001", "001", "1"]        
#adding_binomials(list)       
    
"""
Need a Main function!
"""
def main_binomial_conversion():
    
    number = int(raw_input("\nEnter a number that you want to convert to a "+
 "binomial number: "))
    
    power_of_2 = find_starting_power(number)
    
    divisors_list = divisors_of_number(number, power_of_2)
    
    binary_form_of_divisors = convert_to_binary(divisors_list) 
    
    answer = adding_binomials(binary_form_of_divisors)
    
    print "\nFirst answer: ",answer
    
    answer = str(answer)
    
    while answer[-1]=="0":
        answer = answer[:-1]
        
    print "\nSecond answer: ",answer
    
main_binomial_conversion()
        
               
        

    