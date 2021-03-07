import requests
from operator import attrgetter

def greatPowers(save, playerCount):
    response = requests.get('https://skanderbeg.pm/api.php?key=a6aeaf7782e8c5444b8e9f55cb5abc36&scope=getCountryData&save={0}&value=gp_score;player&format=json'.format(save))
    data = response.json()
    class Employee:
        def __init__(self, tag, player, gp_score):
            self.tag = tag
            self.player = player
            self.gp_score = gp_score

        def __repr__(self):
            return '{' + self.player + ', ' + self.tag + ', ' + self.gp_score + '}'
    playerList = []
    for i in data:
        if 'player' in data.get(i)[0] and 'gp_score' in data.get(i)[0]:
            playerList.append(Employee(i,data.get(i)[0]['player'],int(data.get(i)[0]['gp_score'])))
    gpList = sorted(playerList, key=attrgetter('gp_score'), reverse=True)
    playerCount = int(playerCount)
    text="**```GREAT POWERS LIST\n"
    for i in range(len(gpList[:playerCount])):
        text = text + "{0} - {1} ({2})\n".format(i+1, gpList[i].player, gpList[i].gp_score)
    text = text + "```**"
    return text