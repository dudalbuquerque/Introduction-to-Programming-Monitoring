Período: 24.2
Lista: 3
Questão: x 
Dificuldade: Média


**Ash enfrenta Gary: uma batalha épica!**

Ash terá que enfrentar novamente um de seus maiores rivais, Gary. 

Para isso, ele contará com seus pokémons de confiança. 

O mesmo vale para Gary, que não deixará barato e entrará com seus Pokémons mais poderosos. 

Ambos estarão com seus Pokémons em suas mochilas e irão poder escolher qual usar. Cada batalha só será resolvida quando um Pokémon desmaiar, e será decidido quem inicia cada batalha através de um 'par ou ímpar'! 

![Ahs](https://media1.tenor.com/m/7-tMnBp6KJoAAAAd/pokemon-pocket-monsters.gif)

#



Seu desafio será criar **um programa que simule o confronto entre Ash e Gary**. 

**BATALHA:**

Na batalha, o pokémon que começa atacando é o de quem ganhou no par ou ímpar e deve ocorrer da seguinte forma:

**1.** O valor de ataque é composto pelo nível do pokémon que está atacando vezes 2;

**2.** O pokémon que está sendo atacado terá seu HP diminuído com o valor de ataque;

**3.** Ele só pode atacar se seu HP for maior que 0;

**4.** Não haverá nenhum tipo de defesa;

**5.** A batalha só acaba quando algum dos pokémons desmaiar. E, até que isso aconteça, ficam intercalando os ataques (Um ataca, depois o outro);

**6.** O pokémon desmaiado não pode mais ser usado;

**7.** Só poderá ir para a próxima batalha se ainda tiver pokémons na mochila.


## Input

Inicialmente, você receberá a quantidade de pokémons que Ash e Gary, respectivamente, carregam em suas mochilas:

> **qtd_Ash qtd_Gary**

Logo após, para cada pokémon, você vai receber uma entrada informando os dados abaixo. Atente-se para o fato de que os primeiros são os pokemons de Ash e depois chegam os de Gary, de acordo com a quantidade determinada anteriormente. A entrada virá no seguinte formato:

> **Nome do pokémon, tipo, HP inicial, nível**

Com os dados coletados, é possível dar início ao confronto. Você deverá receber as entradas relacionadas às batalhas até que a entrada seja:

> **"FIM DAS BATALHAS"**

Para cada batalha, Ash irá decidir se jogará 'par' ou 'ímpar'. Assim, você irá receber essa decisão e, em seguida, os números (de 0 a 10) jogados por eles:

> **decisao_Ash**

> **numero_Ash numero_gary**

Em seguida, eles irão escolher os pokémons para a batalha, da seguinte forma:

>**"{nome_pokemonASH} eu escolho você!”**

>**“{nome_pokemonGARY} chegou a sua vez!”**

**OBS.:** Esses pokémons escolhidos sempre estarão disponíveis na mochila.
Lembre-se que, para cada batalha, esse quarteto de entradas deve ser recebido. Ou seja, o jogo de par ou ímpar e a escolha dos pokémons.


## Output

Antes da primeira batalha, deve ser impresso:
> **QUE COMECEM AS BATALHAS**

Ao fim de cada batalha, deve-se informar o resultado da seguinte forma:
> **{pokemon_perdedor} desmaiou e {pokemon_vencedor} venceu esta luta**

Ao final de todas as batalhas, deve-se exibir uma linha de divisão do output:
> **=============== ===============**

E, então, deve ser mostrado a lista de batalhas na ordem em que ocorreram, com o nome do vencedor em maiúsculo e do perdedor em minúsculo (o primeiro pokemon sempre será o de Ash e o segundo é o de Gary, nessa ordem)

> **1° Batalha: {pokémonA} vs {pokémonB}**

>...

> **X° Batalha: {pokémonY} vs {pokémonZ}**

Por fim, deve-se determinar e exibir o vencedor final do total de batalhas:

- Se Ash vencer mais batalhas:

> **Ash é o grande vencedor!**

- Se Gary vencer mais batalhas:

> **Gary é o grande vencedor!**

- Caso haja empate:

> **Depois de todas as batalhas, ainda terminou em empate!**

- Porém, atenção, se ambos não trouxeram pokemón na mochila, deve ser exibido:
> **Nenhuma batalha foi concluída.**

- E, caso apenas um deles não tenha trazido, imprima:

> **{nome} deixou seus pokemons descansando!**

Nesse último caso, o outro ganha por consequência, devendo assim aparecer a frase do vencedor final, a qual vem depois desse print.
