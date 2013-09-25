"""
Coded by: Marcus Willock :)
"""

def my_version():
    """
    Converts binomial numbers to regular base 10 numbers.
    """
    num = raw_input("\nPlease enter a binomial number: ")
    
    # Will store the answer
    total = 0
    
    # logic for binomial conversion to base 10 numbers
    for index in range(len(num)):
        
        tempt = int(num[index])
        
        if tempt == 1:
            
            total += 2**index
            
    print "\nAnswer is: ", total, "\n"
    
if __name__ == "__main__":
    my_version()
