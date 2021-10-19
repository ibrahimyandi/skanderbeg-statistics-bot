import requests
from operator import attrgetter

def scored(save):
    response = requests.get('https://skanderbeg.pm/api.php?key=a6aeaf7782e8c5444b8e9f55cb5abc36&playersOnly=true&scope=getCountryData&save={0}&value=player;countryName;human;overall_strength;provinces;monthly_income;&format=json'.format(save), verify=False)
    data = response.json()
    scoreList = []
    class Players:
        def __init__(self, player, country, income, oStrength, total):
            self.country = country
            self.player = player
            self.income = income
            self.oStrength = oStrength
            self.total = total

    incomeAverage = 1.0
    oStrengthAverage = 1.0
    content = "`"
    content = content + "**SKORLAR**\n"
    countPlayers = 0
    for i in data:
        countPlayers += 1
        if float(incomeAverage) < float(data.get(i)[0]['monthly_income']):
            incomeAverage = float(data.get(i)[0]['monthly_income'])
    
        if float(oStrengthAverage) < float(data.get(i)[0]['overall_strength']):
            oStrengthAverage = float(data.get(i)[0]['overall_strength'])
    incomeAverage = 30/countPlayers
    oStrengthAverage = 70/countPlayers
    for i in data:
        if 'monthly_income' in data.get(i)[0] and 'provinces' in data.get(i)[0]:
            if float(data.get(i)[0]['provinces']) >= 1:
                try:
                    scoreList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],float(data.get(i)[0]['monthly_income']),float(data.get(i)[0]['overall_strength']),0))
                except:
                    scoreList.append(Players("?",data.get(i)[0]['countryName'],float(data.get(i)[0]['monthly_income']),float(data.get(i)[0]['overall_strength']),0))
    scoreList = sorted(scoreList, key=attrgetter('oStrength'), reverse=True)
    for i in range(len(scoreList)):
        scoreList[i] = Players(scoreList[i].country, scoreList[i].player, float(scoreList[i].income), float((len(scoreList)-i)*(70/len(scoreList))),0)
    scoreList = sorted(scoreList, key=attrgetter('income'), reverse=True)
    for i in range(len(scoreList)):
        scoreList[i] = Players(scoreList[i].country, scoreList[i].player, (len(scoreList)-i)*(30/len(scoreList)), scoreList[i].oStrength,float((len(scoreList)-i)*(30/len(scoreList)))+float(scoreList[i].oStrength))
    scoreList = sorted(scoreList, key=attrgetter('total'), reverse=True)
    for i in range(len(scoreList)):
        content = content + "{0}.{1}({2}) {3}+{4} = {5}\n".format(i+1, scoreList[i].country, scoreList[i].player,f"{scoreList[i].income:.1f}", f"{scoreList[i].oStrength:.1f}", f"{scoreList[i].total:.1f}")

    content = content + "`"
    return content