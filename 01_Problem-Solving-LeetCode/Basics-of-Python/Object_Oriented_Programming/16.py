class Player:
    teamName = 'leaverpool'
    teamMember = []
    def __init__(self,name):
        self.name = name
        self.teamMember.append(self.name)
        self.formerTeamName = []

p1 = Player("Samir")
p1.formerTeamName.append("Berselona")
p2 = Player("Mark")
p2.formerTeamName.append("Chelsea")


print(p1.name)
print(p1.formerTeamName)
print(p1.teamMember)

print(p2.name)
print(p2.formerTeamName)
print(p2.teamMember)
