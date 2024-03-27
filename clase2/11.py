# EJERCICIO 11
# segundos_inicial = 200000 # caso random remanente
# segundos_inicial = 200040 # caso segundos 0  remanente
# segundos_inicial = 200000 + 1600 # caso minutos 0 remanente
segundos_inicial = 200000 + 16000 + 57600 - 14400 # caso horas 0 remanente
print("segundos iniciales {}".format(segundos_inicial))
resultados = {
  'dias': 0,
  'horas': 0,
  'minutos': 0,
  'segundos': 0
}
remanente_segundos_dias = segundos_inicial %(24*60*60)
remanente_segundos_dias2 = segundos_inicial - remanente_segundos_dias
resultados['dias'] = int(remanente_segundos_dias2 / (24*60*60))

remanente_segundos_horas = remanente_segundos_dias % (60*60)
remanente_segundos_horas2 = remanente_segundos_dias - remanente_segundos_horas
resultados['horas'] = int(remanente_segundos_horas2 / (60*60))

remanente_segundos_minutos = remanente_segundos_horas % 60
remanente_segundos_minutos2 = remanente_segundos_horas - remanente_segundos_minutos

resultados['minutos'] = int(remanente_segundos_minutos2 / 60)
resultados['segundos'] = remanente_segundos_minutos

print(resultados)
print("{} {}, {} {}, {} {}, {} {}".format(resultados['dias'], 'dias', resultados['horas'], 'horas', resultados['minutos'], 'minutos', resultados['segundos'], 'segundos', ))