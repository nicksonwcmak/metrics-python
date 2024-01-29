import numpy as np

'''
Refactoring "Metrics" in Python
Each Metric object represents a metric space
Each must implement dist(), which returns some measure of distance between objects
'''

class Metric:
    '''
    Generic class for encapsulating a Metric over a particular metric space
    '''
    def dist(self,obj1,obj2):
        '''
        Measures the distance between obj1 and obj2
        Returns a number satisfying the following 3 conditions:
        1) Positive definite:
            dist(obj1,obj2) >= 0; dist(obj1,obj2) == 0 iff obj1 == obj2
        2) Symmetric:
            dist(obj1,obj2) == dist(obj2,obj1)
        3) Triangle inequality:
            for any objects obj1,obj2,obj3 in the metric space,
            dist(obj1,obj2) <= dist(obj1,obj3) + dist(obj3,obj2)
        '''
        raise NotImplementedError

class DiscreteMetric(Metric):
    # implements the discrete metric over an arbitrary metric space

    def dist(self,obj1,obj2):
        # returns 0 if the objects have the same value, 0 otherwise
        return 0 if obj1 == obj2 else 1

class HammingDist(Metric):
    # implements the Hamming distance over the space of strings

    def dist(self, obj1, obj2):
        # returns the number of characters that are different between strings
        # two strings MUST be the same length
        dist = 0
        list1 = ([*obj1]) # using unpack operator
        list2 = ([*obj2]) # TODO: test that this works correctly
        for i in range(len(list1)):
            if list1[i] != list2[i]: dist+=1
        return dist 
        
class LpNorm(Metric):
    # implements the Lp norm over a vector space

    # initialization
    # self.p should be an integer greater than 1, or np.inf for the max norm
    def __init__(self,p):
        self.p = p
        super().__init__()

    def dist(self,obj1, obj2):
        if self.p == np.inf: # max norm
            return np.max(np.abs(obj1 - obj2))
        else: # normal Lp norm
            return np.sum(np.abs(obj1 - obj2)**self.p)**(1.0/self.p)

# TaxicabMetric is same as L1 norm
# class PAdicDist

'''
test = DiscreteMetric()
print(test.dist(0,1))
print(test.dist(0,0))
test1 = 1
test11 = 1
print(test.dist(test1,test11))
'''
