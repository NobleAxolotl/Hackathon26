class Plan:
    def __init__(self, time, budget, commitment, conditions, weight, wellbeing, body, outcome):
        self.time = time
        self.budget = budget
        self.commitment = commitment
        self.conditions = conditions
        self.weight = weight
        self.wellbeing = wellbeing
        self.body = body
        #self.outcome = outcome(time, buget, other, other)
        self.outcome = outcome

class User:
    def __init__(self, name, gender, Plan):
        self.name = name
        self.name = gender
        self.Plan = Plan
