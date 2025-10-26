import csv
import os

class Passenger:
  def __init__(self, row: dict[str, str]):
    self.PassengerId = int(row["PassengerId"])
    self.Survived = int(row["Survived"])
    self.Pclass = int(row["Pclass"])
    self.Name = row["Name"]
    self.Sex = row["Sex"]
    self.Age = float(row["Age"]) if row["Age"] else None
    self.SibSp = int(row["SibSp"])
    self.Parch = int(row["Parch"])
    self.Ticket = row["Ticket"]
    self.Fare = float(row["Fare"]) if row["Fare"] else None
    self.Cabin = row["Cabin"]
    self.Embarked = row["Embarked"]

passengers: list[Passenger] = []

path = os.path.join(os.path.dirname(__file__), "titanic.csv")
with open(path, newline='', encoding='utf-8') as f:
  reader = csv.DictReader(f)
  for row in reader:
    passengers.append(Passenger(row))
