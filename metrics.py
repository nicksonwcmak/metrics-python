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

# class HammingDist
# class LpNorm
# class TaxicabMetric
# class PAdicDist

'''
test = DiscreteMetric()
print(test.dist(0,1))
print(test.dist(0,0))
test1 = 1
test11 = 1
print(test.dist(test1,test11))
'''
