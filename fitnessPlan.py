class User:
    def __init__(self, name, time, budget, equipment, commitmentLevel, commitmentLength, conditions, mobility, wellbeing, improvement, body, fitnessPlan):
        self.name = name
        self.time = time
        self.budget = budget
        self.equipment = equipment
        self.commitmentLevel = commitmentLevel
        self.commitmentLength = commitmentLength
        self.conditions = conditions
        self.mobility = mobility
        self.wellbeing = wellbeing
        self.improvement = improvement
        self.body = body
        self.fitnessPlan = None #will not be defined until final plan is called

def finalPlan(user):
    category = 0
    #category = km.predict(user) 
    # this is still under development, function will find users category by kmode predict function
    return category

def main():
    sampleData = [     
    ("45-60", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("60-above", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("30-40", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("60-above", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("45-60", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("30-40", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("30-40", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("30-40", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("45-60", 0, 0, 0, 0, 0, 0, 0, 0, 0),
    ("30-40", 0, 0, 0, 0, 0, 0, 0, 0, 0),
]
    #km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=1, random_state=42)
    #clusters = km.fit_predict(sampleData)
    #this part will be where the machine learning clustering happens
