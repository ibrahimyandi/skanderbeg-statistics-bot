import requests
from operator import attrgetter

def aScored(save):
    response = requests.get('https://skanderbeg.pm/api.php?key=a6aeaf7782e8c5444b8e9f55cb5abc36&scope=getCountryData&playersOnly=true&save={0}&value=player;countryName;human;overall_strength;monthly_income;&format=json'.format(save), verify=False)
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
    content = content + "**SKORLAR(ORANLI)**\n"
    for i in data:
        if 'player' in data.get(i)[0]:
            if float(incomeAverage) < float(data.get(i)[0]['monthly_income']):
                incomeAverage = float(data.get(i)[0]['monthly_income'])
        if 'player' in data.get(i)[0]:
            if float(oStrengthAverage) < float(data.get(i)[0]['overall_strength']):
                oStrengthAverage = float(data.get(i)[0]['overall_strength'])
    incomeAverage = incomeAverage/30
    oStrengthAverage = oStrengthAverage/70
    for i in data:
        if 'player' in data.get(i)[0] and 'monthly_income' in data.get(i)[0]:
            scoreList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],float(data.get(i)[0]['monthly_income']),float(data.get(i)[0]['overall_strength']),0))
    for i in range(len(scoreList)):
        scoreList[i] = Players(scoreList[i].country, scoreList[i].player, float(scoreList[i].income)/incomeAverage, float(scoreList[i].oStrength)/oStrengthAverage,float(scoreList[i].income)/incomeAverage + float(scoreList[i].oStrength)/oStrengthAverage)
    scoreList = sorted(scoreList, key=attrgetter('total'), reverse=True)
    for i in range(len(scoreList)):
        content = content + "{0}.{1}({2}) {3}+{4} = {5}\n".format(i+1, scoreList[i].country, scoreList[i].player,f"{scoreList[i].income:.0f}",f"{scoreList[i].oStrength:.0f}",f"{scoreList[i].total:.2f}")
    content = content + "`\n"
    return content