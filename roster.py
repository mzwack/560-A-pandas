#https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {
    "Last Name": ["Bacot", "Davis", "Cadeau", "Claude", "Brown", "Tyson", "Johnson", "Lee", "Walker", "Hall"],
    "First Name": ["Armando", "RJ", "Elliot", "Ty", "James", "Cade", "Alex", "Ryan", "Kevin", "Sam"], 
    "height": [83, 72, 73, 79, 82, 79, 77, 82, 70, 74],  
    "weight": [240, 180, 180, 230, 215, 200, 195, 250, 175, 190]  
}
data = pd.DataFrame(player)

data ["bmi"] = ((data["weight"]/2.205)/((data["height"]/39.37)**2)).round(2)
print(data)

data.to_csv("bmi.csv")