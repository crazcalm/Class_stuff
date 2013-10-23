import dfa

print dfa.parity2.check_integrity()
print dfa.parity.check_integrity()

print "\n\n\n"

print "dfa 1: ",dfa.parity.accepts([0,0,0,0,0,0,0])
print "dfa 2: ",dfa.parity2.accepts([0,0,0,0,0,0,0])

class Mine:
    
    def __init__(self, m1, m2):
        """
        This function takes to arugements that are either
        DFAs or NFAs
        """
        
        self.m1 = m1
        self.m2 = m2
        
    def __repr__(self):
        """
        Created for debugging purposes.
        """
        
        m1 = self.m1.__str__()
        m2 = self.m2.__str__()
        
        return m1 + "\n\n" + m2
    
    def sequence_test(self, sequence):
        """
        Takes a sequences and run it through machine 1 and machine 2
        """
        
        if self.m1.accepts(sequence) & self.m2.accepts(sequence):
            print "\nBoth machine 1 and 2 end in an accepting state!"
            return True
        
        else:
            print "\nAt least one of the machines does not end in an accepting state!"
            return False

"""
test = Mine(dfa.parity, dfa.parity2)

print test.sequence_test([0,0,0,0,0,0,0])
"""
