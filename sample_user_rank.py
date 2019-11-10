
import numpy as np

"""
Class that simulates a sample user
User has an alpha value and tolerance value
"""
class Sample_User:

    #Notes: introduce tolerance(noise) and figure out best user_decision data structure

    alpha = 0.30
    tolerance = 0.05

    user_objective_values = {}
    user_rank_indices = {} #for ranks 0...n, n designates the best rank, 

    def __init__(self, alpha, tolerance):
        self.alpha = alpha
        self.tolerance = tolerance
    
    def get_user_objective_values(self):
        return self.user_objective_values
    
    def get_user_rank_indices(self):
        return self.user_rank_indices

    def get_rankings(self):
        objective_values = []
        for item in self.user_objective_values:
            input = item
            output = self.user_objective_values[item]
            objective_values.append((input, output))
        
        objective_values.sort(key = lambda x: x[1])  
        num_items = len(objective_values)

        for pair in self.user_objective_values:
            rank_index = 0.0
            for item in objective_values:
                if pair != item[0]:
                    rank_index += 1
                else:
                    self.user_rank_indices[pair] = rank_index

    #Note: how should we model fluctuation? uniform? normal?
    def user_decision(self, objective_value_pair_1):
        
        np.random.seed(101) 
        trial_alpha = np.random.uniform(self.alpha - self.tolerance, self.alpha + self.tolerance)
        multi_objective_value_1 = trial_alpha*objective_value_pair_1[0] + (1-trial_alpha)*objective_value_pair_1[1]
        self.user_objective_values[objective_value_pair_1] = multi_objective_value_1



    


    