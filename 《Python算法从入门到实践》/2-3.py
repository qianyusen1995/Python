class Solver:
    target = 10

def __init__(self, precise_mode = False):
    self.precise_mode = precise_mode

def solution(self, nums):
    result = []
    groups = self.dimensionality_reduction(self, format(nums)) #降维
    for group in groups:
        for op in self.ops:
            exp = self.assemble(group[0], group[1], op)['exp']
            if self.check(exp, self.target) and exp not in result:
                result.append(exp)
    return [exp + '=' + str(self.target) for exp in result]

def dimensionality_reduction(self, nums):
    result = []

#未完成
