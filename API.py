import requests, time
#from Email import email
#variaveis
finite = int(0)
x = int(1)
mortos_antes = int(0)
time_past = int(0)
count = 0
while x >= finite:
    result = requests.get("https://covid19-brazil-api.now.sh/api/report/v1/brazil")
    error = result.status_code
    if error != 200:
        print(error)
    result_json = result.json()
    time_now = (result_json['data']['updated_at'])
    if time_now != time_past:
        print(time_now)
        mortos = (result_json['data']['deaths'])
        print("Foi atualizado: ", mortos)
        print("Mortes antes: ", mortos_antes)
        #info = ('O numero foi atualizado. Numero anterior: ', mortos_antes, 'numero atual', mortos)
       # email(info)
        time_past = time_now
        if mortos != mortos_antes:
            mortos_antes = mortos
        count += 1
        time.sleep(150)
 #   if mortos_momento == mortos:
  #      print("O numero permanece o mesmo")
   # else:
    #    print("Mortos aumentaram:", mortos_momento)
     #   mortos_momento = mortos