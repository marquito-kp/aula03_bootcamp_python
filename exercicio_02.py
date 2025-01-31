### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

import random
import time


print("Classificação de dados de sensor")

data = False

while data is not True:
    temperature = round(random.uniform(0,50),1)

    if temperature < 18.0:
        print(f"{temperature}º C")
        print("A temperatura está baixa!")
    elif temperature >= 18 and temperature <= 26:
        print(f"{temperature}º C")
        print("Temperatura está normal!")
    elif temperature > 26:
        print(f"{temperature}º C")
        print("A temperatura está alta!")
    
    time.sleep(15)