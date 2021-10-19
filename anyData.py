import requests
from operator import attrgetter

def aData(save,dataId, playerCount):
    response = requests.get('https://skanderbeg.pm/api.php?key=a6aeaf7782e8c5444b8e9f55cb5abc36&scope=getCountryData&playersOnly=true&save={0}&value=player;countryName;human;{1}&format=json'.format(save,dataId), verify=False)
    data = response.json()
    dataList = []
    class Players:
        def __init__(self, player, country, value):
            self.player = player
            self.country = country
            self.value = value
    content = "`"
    for i in data:
        try:
            if 'deving_stats' in dataId or 'total_mana_spent' in dataId:
                try:
                    dataList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'], round(float(data.get(i)[0]['{0}'.format(dataId)]['s']))))
                except:
                    dataList.append(Players("?",data.get(i)[0]['countryName'], round(float(data.get(i)[0]['{0}'.format(dataId)]['s']))))
            elif 'deving_stats' in dataId or 'deving_ratios' in dataId:
                try:
                    dataList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'], data.get(i)[0]['{0}'.format(dataId)]['val'].replace("&lt;br&gt;","")))
                except:
                    dataList.append(Players("?",data.get(i)[0]['countryName'], data.get(i)[0]['{0}'.format(dataId)]['val'].replace("&lt;br&gt;","")))
            else:
                try:
                    dataList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'], round(float(data.get(i)[0]['{0}'.format(dataId)]))))
                except:
                    dataList.append(Players("?",data.get(i)[0]['countryName'], round(float(data.get(i)[0]['{0}'.format(dataId)]))))
        except:
            dataList.append(Players("?",data.get(i)[0]['countryName'], 0))
        dataList = sorted(dataList, key=attrgetter('value'), reverse=True)
    content += "**" + str(dataId.replace("_"," ").upper()) + "**"
    for i in range(len(dataList[:int(playerCount)])):
        try:
            content = content + "\n{0}. {1}({2}) - {3}".format(i+1, dataList[i].country, dataList[i].player,f"{dataList[i].value:,}")
        except:
            content = content + "\n{0}. {1}({2}) - {3}".format(i+1, dataList[i].country, dataList[i].player, dataList[i].value)

    content += "`\n"
    return content