"""
Converts binomial numbers to regular base 10 form numbers
"""

def my_version():
    
    num = raw_input("\nPlease enter a binomial number: ")
    
    total = 0
    
    for index in range(len(num)):
        
        tempt = int(num[index])
        
        if tempt == 1:
            
            total += 2**index
            
    print "\nanswer is: ", total
    
my_version()
