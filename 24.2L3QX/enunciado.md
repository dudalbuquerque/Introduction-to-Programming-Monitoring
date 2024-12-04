**Ash enfrenta Gary: uma batalha épica!**

Ash terá que enfrentar novamente um de seus maiores rivais, Gary. Para isso, ele contará com seus pokémons  de confiança. O mesmo vale para Gary, que não deixará barato e entrará com seus Pokémons mais poderosos. Eles decidirão quem começa a batalha com um "par ou ímpar", e cada confronto será resolvido até que um dos Pokémons desmaie!

![Ahs](https://media1.tenor.com/m/7-tMnBp6KJoAAAAd/pokemon-pocket-monsters.gif)



Seu desafio será criar um programa que simule a batalha entre Ash e Gary. Cada um deles poderá escolher entre os pokémons que estão em suas mochilas, para levar ao combate.

BATALHA:

Na batalha, o pokémon que começa atacando é o de quem ganhou no par ou ímpar.
1. O ataque é composto pelo nível do pokémon que está atacando vezes 2;
2. O pokémon que está sendo atacado terá seu HP diminuído com o ataque;
3. Cada um ataca uma vez por rodada;
4. Ele só pode atacar se seu HP for maior que 0;
5. Não haverá nenhum tipo de defesa;
6. A batalha só acaba quando algum dos pokémons desmaiarem;
7. O pokémon desmaiado não pode mais ser usado;
8. Pode apenas ir para a próxima batalha se tiver pokémons na mochila.

## Input

1. Na primeira linha, será informada a quantidade de Pokémons que Ash e Gary possuem em suas mochilas.
2. Em seguida, para cada Pokémon de Ash e Gary, serão fornecidos os seguintes dados: nome, tipo, HP inicial e nível. Os Pokémons de Ash vêm primeiro, seguidos pelos de Gary.
3. Para cada batalha, antes do confronto, será solicitado que Ash escolha "par" ou "ímpar" para determinar quem começará atacando.
4. Em seguida, os jogadores escolherão seus Pokémons para a batalha com a seguinte entrada:
    - nome_pokemon eu escolho você! para Ash.
    - nome_pokemon chegou a sua vez! para Gary.
5. O processo de batalha continuará até que o comando "FIM DAS BATALHAS" seja fornecido.

OBS: Esses pokémons sempre estarão disponíveis na mochila.

## Output

Ao início de cada batalha, deve ser exibida a mensagem "QUE COMECEM AS BATALHAS".

Durante a decisão de "par ou ímpar", deve-se informar quem começa atacando:
- Se Ash vencer, a mensagem será: "Ash começa atacando!"
- Se Gary vencer, a mensagem será: "Gary começa atacando!"

Ao fim de cada batalha, deve-se informar o resultado:
- Exibir a mensagem "{pokemon_perdedor} desmaiou e {pokemon_vencedor} venceu esta luta".
- O nome do vencedor deve ser exibido em maiúsculas e o do perdedor em minúsculas.

Após todas as batalhas, deve-se exibir:
print("=============== ===============")
- Mostrar a lista de batalhas na ordem em que ocorreram, com o nome do vencedor em maiúsculas e do perdedor em minúsculas.
- Determinar e exibir o vencedor final:
    - "Ash é o grande vencedor!" se Ash vencer mais batalhas.
    - "Gary é o grande vencedor!" se Gary vencer mais batalhas.
    - "Depois de todas as batalhas, ainda terminou em empate!" se houver empate.

- Se não trouxerem pokemón na mochila, deve ser exibido:
    - caso de ambos: print("Nenhuma batalha foi concluída.")
    - apenas um deles: print("{nome} deixou seus pokemons descansando!"), e o outro ganha consequentemente, devendo assim aparecer a frase do vencedor final.

