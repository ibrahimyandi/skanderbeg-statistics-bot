import requests
from operator import attrgetter

def navalData(save, playerCount):
    response = requests.get('http://skanderbeg.pm/api.php?scope=getSaveDataDump&playersOnly=true&save={0}&type=battlesData'.format(save), verify=False)
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
                if x == 'heavy_ship' or x == 'light_ship' or x == 'galley' or x == 'transport':
                    attCount += int(data[i]['attacker'][x])
                if x == 'country':
                    attCountry = data[i]['attacker'][x]
                if x == 'losses':
                    attLose = data[i]['attacker'][x]
            for x in data[i]['defender']:
                if x == 'heavy_ship' or x == 'light_ship' or x == 'galley' or x == 'transport':
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
    content="`**Deniz Muharebe Listesi**\n"
    for i in battles[:int(playerCount)]:
        if i.result == 'yes':
            content = content + "Tarih: **{0}** Muharebe: **{1}** Toplam gemi: **{2}** Toplam kayıp: **{3}** Kazanan: **{4}** Kaybeden: **{5}**\n{4} gemi sayısı: **{6}**    {4} kaybettiği gemi sayısı: **{8}**\n{5} gemi sayısı: **{7}**    {5} kaybettiği gemi sayısı: **{9}**\n\n".format(i.date, i.name,i.totaltroops, i.totalLose, i.countryAtt, i.countryDef, i.countryAttCount, i.countryDefCount, i.countryAttLose, i.countryDefLose)
        else:
            content = content + "Tarih: **{0}** Muharebe: **{1}** Toplam gemi: **{2}** Toplam kayıp: **{3}** Kazanan: **{5}** Kaybeden: **{4}**\n{4} gemi sayısı: **{6}**    {4} kaybettiği gemi sayısı: **{8}**\n{5} gemi sayısı: **{7}**    {5} kaybettiği gemi sayısı: **{9}**\n\n".format(i.date, i.name,i.totaltroops, i.totalLose, i.countryAtt, i.countryDef, i.countryAttCount, i.countryDefCount, i.countryAttLose, i.countryDefLose)
    content= content+"`"
    return content