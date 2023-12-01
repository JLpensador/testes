pessoa = ("João Luiz")


print( f" bem-vindo {pessoa}")
a = input("começar novo jogo? s|n")

if a == "n":
    print("Fim de Jogo")

if a == "s":
   b = input("você está numa sala branca, porem não sabe como foi parar lá, você percebe que está deitado numa cama, perto dessa cama tem uma gaveta, você quer examiná-la? s|n")

if b == "s":
   c = input("Você abre a gaveta, parece que la no fundo tem algo, você encontra um papel, você quer ler? s|n")

if b == "n":
   c = input("bem, parece que não tem nada... mas sente algo perto se aproximando, você olha para uma porta. Verificar? s|n") 

if c == "s":
   print("você se aproxima da porta, está muito escuro, você não consegue enxergar nada, apenas outras celas, como se fosse uma prisão, alguém passa bem na mesma hora e diz: ei! Um dos prisoneiros acordou! soltem o gás na sala 306! Um gas sai pelo duto de ar nas paredes, você não consegue resistir e em poucos minutos você cai ao chão. Fim de jogo")     

if d == "s":
   e = input("No papel está escrito 'TRATAMENTO PSICOLÓGICO PARA A HUMANIDADE! ATENDEMOS AQUELES QUE NÃO SE AGUENTAM MAIS E PRECISAM DE CONSOLO PARA VIVER. SIM VOCÊ, SE VOCÊ É UM DOS NOSSOS VENHA NÓS VISITAR, PRECISAMOS DE VOCÊ...' Analisando com cuidado parece que o papel é algum tipo de panfleto, talvez algo relacionado com esse lugar? você não sabe, você sente algo se aproximando, você olha para uma porta. Verificar? s|n ")

if e == "s":
    print("você se aproxima da porta, está muito escuro, você não consegue enxergar nada, apenas outras celas, como se fosse uma prisão, alguém passa bem na mesma hora e diz: ei! Um dos prisoneiros acordou! soltem o gás na sala 306! Um gas sai pelo duto de ar nas paredes, você não consegue resistir e em poucos minutos você cai ao chão. Fim de jogo")