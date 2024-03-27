# EJERCICIO 11
segundos_inicial = 200000
remanente_segundos_dias = segundos_inicial %(24*60*60)
remanente_segundos_dias2 = segundos_inicial - remanente_segundos_dias
dias = remanente_segundos_dias2 / (24*60*60)
print(str(dias) + ' dias')
remanente_segundos_horas = remanente_segundos_dias % (60*60)
remanente_segundos_horas2 = remanente_segundos_dias - remanente_segundos_horas
horas = remanente_segundos_horas2 / (60*60)
print(str(horas) + ' horas')
remanente_segundos_minutos = remanente_segundos_horas % 60
remanente_segundos_minutos2 = remanente_segundos_horas - remanente_segundos_minutos
minutos = remanente_segundos_minutos2 / 60
print(str(minutos) + ' minutos')
remanente_segundos_minutos = remanente_segundos_horas % 60
remanente_segundos_minutos2 = remanente_segundos_horas - remanente_segundos_minutos
minutos = remanente_segundos_minutos2 / 60
print(str(remanente_segundos_minutos) + ' segundos')