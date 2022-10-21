class Player:
    teamName = 'Leaverpool'
    def __init__(self,name):
        self.name = name
        self.formerTeam = []
p1 =Player('Samir')
p2 = Player("Mark")
p1.formerTeam.append('Berselona')
p2.formerTeam.append('Chelsea')
print(p1.name)
print(p1.formerTeam)
print(p1.teamName)
print("******************")
print(p2.name)
print(p2.formerTeam)
print(p2.teamName)
