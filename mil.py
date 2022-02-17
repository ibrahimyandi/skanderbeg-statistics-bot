import requests
from operator import attrgetter

def military(save):
    response = requests.get('https://skanderbeg.pm/api.php?key=a6aeaf7782e8c5444b8e9f55cb5abc36&scope=getCountryData&playersOnly=true&save={0}&value=player;countryName;human;FL;max_manpower;army_tradition;total_navy;army_professionalism;total_casualties;battleCasualties;attritionCasualties;navalCasualties;total_mana_spent_on_reducing_we;spent_on_forts_building;&format=json'.format(save), verify=False)
    data = response.json()
    milList = []
    class Players:
        def __init__(self, player, country, value):
            self.player = player
            self.country = country
            self.value = value

    content="`**ASKERİ İSTATİSTİKLERİ**\n"

    for i in data:
        if 'FL' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['FL']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['FL']))))
              
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En büyük ordu(army): {0}-{1}(#)\n".format(milList[0].player,milList[0].country,milList[0].value)
    milList.clear()
    for i in data:
        if 'max_manpower' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['max_manpower']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['max_manpower']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En yüksek insan gücü(manpower): {0}-{1}(#)\n".format(milList[0].player,milList[0].country,milList[0].value)
    milList.clear()
    for i in data:
        if 'army_tradition' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['army_tradition']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['army_tradition']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En yüksek ordu geleneği(army tradition): {0}-{1}(#)\n".format(milList[0].player,milList[0].country,milList[0].value)
    milList.clear()
    for i in data:
        if 'total_navy' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],int(data.get(i)[0]['total_navy'])))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],int(data.get(i)[0]['total_navy'])))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En büyük donanma(navy): {0}-{1}(#)\n".format(milList[0].player,milList[0].country,milList[0].value)
    milList.clear()
    for i in data:
        if 'army_professionalism' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['army_professionalism']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['army_professionalism']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En yüksek ordu profesyonelliği(army professionalism): {0}-{1}(#)\n".format(milList[0].player,milList[0].country,milList[0].value)
    milList.clear()
    for i in data:
        if 'total_casualties' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['total_casualties']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['total_casualties']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En çok kayıp veren(total casualties): {0}-{1}({2})\n".format(milList[0].player,milList[0].country,f"{milList[0].value:,}")
    milList.clear()
    for i in data:
        if 'player' in data.get(i)[0] and 'battleCasualties' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['battleCasualties']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En çok muharebede asker kaybeden(battle casualties): {0}-{1}({2})\n".format(milList[0].player,milList[0].country,f"{milList[0].value:,}")
    milList.clear()
    for i in data:
        if 'attritionCasualties' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['attritionCasualties']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['attritionCasualties']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En çok yıpranan ordu(attrition casualties): {0}-{1}({2})\n".format(milList[0].player,milList[0].country,f"{milList[0].value:,}")
    milList.clear()
    for i in data:
        if 'navalCasualties' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['navalCasualties']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['navalCasualties']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En çok gemi kaybeden(naval casualties): {0}-{1}({2})\n".format(milList[0].player,milList[0].country,f"{milList[0].value:,}")
    milList.clear()
    for i in data:
        if 'total_mana_spent_on_reducing_we' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['total_mana_spent_on_reducing_we']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['total_mana_spent_on_reducing_we']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En çok savaş yorgunluğua puan harcayan(war exhaustion): {0}-{1}({2})\n".format(milList[0].player,milList[0].country,f"{milList[0].value:,}")
    milList.clear()
    for i in data:
        if 'spent_on_forts_building' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                milList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_forts_building']))))
            else:
                milList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_forts_building']))))
        milList = sorted(milList, key=attrgetter('value'), reverse=True)
    content = content + "En çok kaleye para harcayan(building forts): {0}-{1}({2})\n".format(milList[0].player,milList[0].country,f"{milList[0].value:,}")
    content = content + "`\n"
    return content