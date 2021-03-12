import requests
from operator import attrgetter

def battlesData(save, playerCount):
    response = requests.get('http://skanderbeg.pm/api.php?scope=getSaveDataDump&save={0}&type=battlesData'.format(save))
    data = response.json()
    battles = []
    class Players:
        def __init__(self, date, name, result, types, countryAtt, countryAttCount, countryAttLose, countryDef, countryDefCount, countryDefLose, totaltroops, totalLose):
            self.date = date
            self.name = name
            self.result = result
            self.types = types
            self.countryAtt = countryAtt
            self.countryAttCount = countryAttCount
            self.countryAttLose = countryAttLose
            self.countryDef = countryDef
            self.countryDefCount = countryDefCount
            self.countryDefLose = countryDefLose
            self.totaltroops = totaltroops
            self.totalLose = totalLose
    attCount = 0
    defCount = 0
    attCountry = ""
    defCountry = ""
    attLose = 0
    defLose = 0
    for i in range(len(data)):
        if 'attacker' in data[i] and 'defender' in data[i] and 'date' in data[i] and 'type' in data[i] and 'country' in data[i]['attacker'] and 'country' in data[i]['defender']:
            for x in data[i]['attacker']:
                if x == 'infantry' or x == 'cavalry' or x == 'artillery':
                    attCount += int(data[i]['attacker'][x])
                if x == 'country':
                    attCountry = data[i]['attacker'][x]
                if x == 'losses':
                    attLose = data[i]['attacker'][x]
            for x in data[i]['defender']:
                if x == 'infantry' or x == 'cavalry' or x == 'artillery':
                    defCount += int(data[i]['defender'][x])
                if x == 'country':
                    defCountry = data[i]['defender'][x]
                if x == 'losses':
                    defLose = data[i]['defender'][x]
        if(attCount+defCount) != 0:
            battles.append(Players(data[i]['date'], data[i]['name'], data[i]['result'], data[i]['type'], attCountry, attCount, attLose, defCountry, defCount, defLose,(attCount + defCount), (attLose + defLose)))
            battles = sorted(battles, key=attrgetter('totaltroops'), reverse=True)
            attCount = 0
            defCount = 0
            attCountry = ""
            defCountry = ""
            attLose = 0
            defLose = 0
    content="**```Muharebe Listesi\nTarih Şehir Ordu/Kayıp Saldıran/Savunan SalSayısı/SavSayısı SalKayıp/SavKayıp\n"
    for i in battles[:int(playerCount)]:
        if i.result == 'yes':
            content = content + "{0} {1} Ordu({2})/({3})Kayıp (G){4}/{5}(M) {6}/{7} {8}/{9}\n".format(i.date, i.name,i.totaltroops, i.totalLose, i.countryAtt, i.countryDef, i.countryAttCount, i.countryDefCount, i.countryAttLose, i.countryDefLose)
        else:
            content = content + "{0} {1} Ordu({2})/({3})Kayıp (M){4}/{5}(G) {6}/{7} {8}/{9}\n".format(i.date, i.name,i.totaltroops, i.totalLose, i.countryAtt, i.countryDef, i.countryAttCount, i.countryDefCount, i.countryAttLose, i.countryDefLose)
    content = content + "```**"
    return content