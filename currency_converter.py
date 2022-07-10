#app_that
# IN: money in USD
# Out: money in EUR


# INPUT
dengi_USD = int(input("skolico usd imeetsea?!: "))
usd_eur_rate = 0.83 #sootnoshenie usd k eur

#calculation (obrabotka data)
dengi_EUR = dengi_USD * usd_eur_rate


# OUTPUT (vivod data)
print('tvoi evrodenigi bichara: ', dengi_EUR)