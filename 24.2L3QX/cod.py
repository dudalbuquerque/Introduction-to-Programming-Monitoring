# Inicialização das mochilas e variáveis
mochila_Ash = []
mochila_Gary = []
Batalhas = []
vitorias_Ash = 0
vitorias_Gary = 0

# Entradas de pokémons
qnt_pokemon = input().split(" ")
for i in range(int(qnt_pokemon[0])):
    pokemon = input().split(", ")
    mochila_Ash.append(pokemon)

for i in range(int(qnt_pokemon[1])):
    pokemon = input().split(", ")
    mochila_Gary.append(pokemon)

mochila_Ash_inicio = len(mochila_Ash)
mochila_Gary_inicio = len(mochila_Gary)

# Começo das batalhas
print("QUE COMECEM AS BATALHAS")


while len(mochila_Ash) > 0 and len(mochila_Gary) > 0:
    # Receber par ou ímpar
    par_impar = input()
    if(par_impar != "FIM DAS BATALHAS"):
        # Determinar quem começa com base na soma dos números
        numeros = input().split()
        soma = sum(map(int, numeros))
        resultado = "ímpar" if soma % 2 != 0 else "par"
        if par_impar == resultado:
            vencedor_impoupar = "Ash"
            print("Ash começa atacando!")
        else:
            vencedor_impoupar = "Gary"
            print("Gary começa atacando!")

        # Receber escolha dos pokémons para a batalha
        pokemon_Ash = input().split(" eu escolho você!")[0]
        pokemon_Gary = input().split(" chegou a sua vez!")[0]


        # Buscar os pokémons na mochila
        for pokemon in mochila_Ash:
            if(pokemon[0] == pokemon_Ash):
                pokemon_Ash = pokemon
        for pokemon in mochila_Gary:
            if(pokemon[0] == pokemon_Gary):
                pokemon_Gary = pokemon

        # Convertendo os atributos para o formato correto
        pokemon_Ash[2] = int(pokemon_Ash[2])  # HP
        pokemon_Ash[3] = int(pokemon_Ash[3])  # Nível
        pokemon_Gary[2] = int(pokemon_Gary[2])  # HP
        pokemon_Gary[3] = int(pokemon_Gary[3])  # Nível

        # Começar a batalha até que um pokémon desmaie
        parar1 = False
        while pokemon_Ash[2] > 0 and pokemon_Gary[2] > 0:
            if vencedor_impoupar == "Ash":
                # Ash ataca primeiro
                pokemon_Gary[2] -= pokemon_Ash[3] * 2
                if pokemon_Gary[2] > 0:
                    pokemon_Ash[2] -= pokemon_Gary[3] * 2
            else:
                # Gary ataca primeiro
                pokemon_Ash[2] -= pokemon_Gary[3] * 2
                if pokemon_Ash[2] > 0:
                    pokemon_Gary[2] -= pokemon_Ash[3] * 2

        # Determinar o vencedor da luta
        if pokemon_Ash[2] > 0:
            print(f"{pokemon_Gary[0]} desmaiou e {pokemon_Ash[0]} venceu esta luta")
            vitorias_Ash += 1
            mochila_Gary.remove(pokemon_Gary)
            pokemon_Ash = pokemon_Ash[0].upper()
            pokemon_Gary = pokemon_Gary[0].lower()
        else:
            vitorias_Gary += 1
            print(f"{pokemon_Ash[0]} desmaiou e {pokemon_Gary[0]} venceu esta luta")
            mochila_Ash.remove(pokemon_Ash)
            pokemon_Ash = pokemon_Ash[0].lower()
            pokemon_Gary = pokemon_Gary[0].upper()

        # Armazenar a batalha
        Batalhas.append([pokemon_Ash, pokemon_Gary])
    else: 
        break

# Imprimir o resumo das batalhas
print("==================== ====================")

if (mochila_Ash_inicio == 0 or mochila_Gary_inicio== 0):
    if mochila_Ash_inicio == 0 and mochila_Gary_inicio== 0:
        print("Nenhuma batalha foi concluída.")
    elif mochila_Ash_inicio == 0:
        print("Ash deixou seus pokemons descansando!")
        vitorias_Gary+=1
    elif mochila_Gary_inicio == 0:
        print("Gary deixou seus pokemons descansando!")
        vitorias_Ash+=1

if mochila_Ash_inicio != 0 and mochila_Gary_inicio != 0:
    cont = 1
    for batalha in Batalhas:
        print(f"{cont}° Batalha: {batalha[0]} vs {batalha[1]}")
        cont += 1
    if vitorias_Ash == vitorias_Gary:
        print("Depois de todas as batalhas, ainda terminou em empate!")

# Determinar o vencedor final
if vitorias_Ash > vitorias_Gary:
    print("Ash é o grande vencedor!")
elif vitorias_Gary > vitorias_Ash:
    print("Gary é o grande vencedor!")
