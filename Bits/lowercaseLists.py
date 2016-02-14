#!/usr/bin/env python

docs = ["The Corporation", "Valentino: The Last Emperor", "Kings of Patsry"]
movies = ["The Talented Mr. Ripley", "The Network", "Silence of the Lambs", "Wall Street", "Marie Antoinette", "My Mana Godfrey", "Rope", "Sleuth"]

films = [[docs], [movies]]
movies[5] = "My Man Godfrey"
docs[-1] = "Kings of Pastry"


y = [x.lower() for x in ["A","B","C"]]

print(y)

newFilmsList = [x.lower() for x in docs] + [x.lower() for x in movies] 
print(newFilmsList)
