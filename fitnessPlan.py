import numpy as np
from kmodes.kmodes import KModes

class User:
    def __init__(self, name, time, budget, equipment, level, schedule, conditions, mobility, body, stress, improvement, fitnessPlan):
        self.time = time
        self.budget = budget
        self.equipment = equipment
        self.level = level
        self.schedule = schedule
        self.conditions = conditions
        self.mobility = mobility
        self.body = body
        self.stress = stress
        self.improvement = improvement
        self.fitnessPlan = None #will not be defined until final plan is called

def finalPlan(user, km):
    category = km.predict(user)
    #function will find users category by kmode predict function
    return category


sampleData = [     
    
    ("Lose", "None", "Limitation", "Beginner"), # P1 2->Cardio
    ("Lose", "None", "Limitation", "Beginner"), # P2
    ("Lose", "None", "Limitation", "Beginner"),# P3
    ("Lose", "None", "Limitation", "Beginner"), # P4
    ("Lose", "Home", "No Limitation", "Beginner"),# P5
    ("Lose", "None", "Limitation", "Beginner"),# P6

    ("Gain", "Gym", "No Limitation", "Advanced"), # P7 0->strength
    ("Gain", "Gym", "No Limitation", "Advanced"), # P8
    ("Gain", "Gym", "No Limitation", "Advanced"), # P9
    ("Gain", "Gym", "No Limitation", "Advanced"), # P10
    ("Gain", "Gym", "No Limitation", "Beginner"), # P11
    ("Gain", "Home", "No Limitation", "Advanced"), # P12

    ("Maintain", "Home", "No Limitation", "Beginner"), # P13 1->Y/S
    ("Maintain", "Home", "No Limitation", "Beginner"),  # P14
    ("Maintain", "Home", "No Limitation", "Beginner"),  # P15
    ("Maintain", "Home", "No Limitation", "Beginner"),  # P16
    ("Maintain", "Gym", "No Limitation", "Beginner"), # P17
    ("Maintain", "Home", "Limitation", "Beginner"),  # P18

]    

X = np.array(sampleData)
km = KModes(n_clusters=3, init='Huang', n_init=5, verbose=1, random_state=42)
km.fit(X)    

#these print statements are for testing purposes to see the data and the clusters that were formed
print(X.shape)
print(type(X))    
clusters = km.fit_predict(X)
print(clusters)
print(km.cluster_centroids_)
#this part will be where the machine learning clustering happens
