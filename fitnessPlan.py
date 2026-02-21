
class User:
    def __init__(self, name, time, budget, commitment, conditions, weight, wellbeing, body, fitnessPlan):
        self.name = name
        self.time = time
        self.budget = budget
        self.commitment = commitment
        self.conditions = conditions
        self.weight = weight
        self.wellbeing = wellbeing
        self.body = body
        self.fitnessPlan = None #will not be defined until final plan is called

def finalPlan(user):
    category = 0
    #category = km.predict(user) 
    # this is still under development, function will find users category by kmode predict function
    return category

def main():
    sampleData = [     # training data here, values will be filled in later
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
]
    #km.fit(sampleData)
    #this part will be where the machine learning clustering happens
