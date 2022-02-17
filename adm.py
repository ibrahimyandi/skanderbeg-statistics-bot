import requests
from operator import attrgetter

def administrative(save):
    response = requests.get('https://skanderbeg.pm/api.php?key=a6aeaf7782e8c5444b8e9f55cb5abc36&scope=getCountryData&playersOnly=true&save={0}&value=player;countryName;human;total_development;provinces;technology;total_ideas;monthly_income;innovativeness;total_mana_spent;total_mana_spent_on_stabbing_up;real_development_ratio;deving_stats;weighted_avg_monarch;spent_total;spent_on_advisors;spent_on_subsidies;spent_on_gifts;spent_on_buildings;spent_on_loans;spent_on_interest;dev_clicks;&format=json'.format(save), verify=False)
    data = response.json()
    admList = []
    class Players:
        def __init__(self, player, country, value):
            self.player = player
            self.country = country
            self.value = value

    content="`**YÖNETİM İSTATİSTİKLERİ**\n"

    for i in data:
        if 'total_development' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],int(data.get(i)[0]['total_development'])))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],int(data.get(i)[0]['total_development'])))

    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Büyük Ülke (development): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En Büyük Ülke (development): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'provinces' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],int(data.get(i)[0]['provinces'])))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],int(data.get(i)[0]['provinces'])))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Büyük Ülke(provinces): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En Büyük Ülke(provinces): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'technology' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],int(data.get(i)[0]['technology']['adm'])+int(data.get(i)[0]['technology']['dip'])+int(data.get(i)[0]['technology']['mil'])))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],int(data.get(i)[0]['technology']['adm'])+int(data.get(i)[0]['technology']['dip'])+int(data.get(i)[0]['technology']['mil'])))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En İleri Ülke(technology): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En İleri Ülke(technology): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'total_ideas' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],int(data.get(i)[0]['total_ideas'])))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],int(data.get(i)[0]['total_ideas'])))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En İleri Ülke(idea): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En İleri Ülke(idea): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'monthly_income' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],float(data.get(i)[0]['monthly_income'])))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],float(data.get(i)[0]['monthly_income'])))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Yüksek Gelir(income): {0}-{1}(#)\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En Yüksek Gelir(income): {0}-{1}(#)\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'innovativeness' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],float(data.get(i)[0]['innovativeness'])))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],float(data.get(i)[0]['innovativeness'])))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Yenilikçi(innovativnes): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En Yenilikçi(innovativnes): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'total_mana_spent' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],int(data.get(i)[0]['total_mana_spent']['s'])))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],int(data.get(i)[0]['total_mana_spent']['s'])))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En çok puan harcayan(monarch power): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En çok puan harcayan(monarch power): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'total_mana_spent_on_stabbing_up' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['total_mana_spent_on_stabbing_up']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['total_mana_spent_on_stabbing_up']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Çok İstikrara puan harcayan(stability): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En Çok İstikrara puan harcayan(stability): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'real_development_ratio' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['real_development_ratio']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['real_development_ratio']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En İyi Şehir Başına Development Oranı(average dev): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En İyi Şehir Başına Development Oranı(average dev): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'deving_stats' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['deving_stats']['s']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['deving_stats']['s']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En çok geliştirme puanı kullanan(deving): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En çok geliştirme puanı kullanan(deving): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'dev_clicks' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                try:
                    admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],float(data.get(i)[0]['dev_clicks'])))
                except:
                    admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],"null"))
            else:
                try:
                    admList.append(Players("?",data.get(i)[0]['countryName'],float(data.get(i)[0]['dev_clicks'])))
                except:
                    admList.append(Players("?",data.get(i)[0]['countryName'],"null"))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En çok geliştirme düğmesine basan(dev clicks): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En çok geliştirme düğmesine basan(dev clicks): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'weighted_avg_monarch' in data.get(i)[0] and 'human' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['weighted_avg_monarch']['s']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['weighted_avg_monarch']['s']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En iyi hanedan(weighted average monarch): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En iyi hanedan(weighted average monarch): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'weighted_avg_monarch' in data.get(i)[0] and 'human' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['weighted_avg_monarch']['s']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['weighted_avg_monarch']['s']))))
    admList = sorted(admList, key=attrgetter('value'))
    try:
        content = content + "En kötü hanedan(weighted average monarch): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,admList[0].value)
    except:
        content = content + "En kötü hanedan(weighted average monarch): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'spent_total' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_total']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_total']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En çok para harcayan(spend in total money): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En çok para harcayan(spend in total money): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'spent_on_advisors' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_advisors']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_advisors']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Pahalı Kabine(advisors): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En Pahalı Kabine(advisors): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'spent_on_subsidies' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_subsidies']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_subsidies']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Cömert(subsidies): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En Cömert(subsidies): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'spent_on_gifts' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_gifts']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_gifts']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Cömert(gift): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En Cömert(gift): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'spent_on_buildings' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_buildings']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_buildings']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En çok yatırım yapan(buildings): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En çok yatırım yapan(buildings): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'spent_on_loans' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_loans']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_loans']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Çok Borç Ödemiş(repaying loans): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En Çok Borç Ödemiş(repaying loans): {0}-{1}({2})\n".format("null","null","null")
    admList.clear()
    for i in data:
        if 'spent_on_interest' in data.get(i)[0]:
            if 'player' in data.get(i)[0]:
                admList.append(Players(data.get(i)[0]['player'],data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_interest']))))
            else:
                admList.append(Players("?",data.get(i)[0]['countryName'],round(float(data.get(i)[0]['spent_on_interest']))))
    admList = sorted(admList, key=attrgetter('value'), reverse=True)
    try:
        content = content + "En Çok Faiz Ödeyen(interest): {0}-{1}({2})\n".format(admList[0].player,admList[0].country,f"{admList[0].value:,}")
    except:
        content = content + "En Çok Faiz Ödeyen(interest): {0}-{1}({2})\n".format("null","null","null")
    content = content + "`\n"
    return content