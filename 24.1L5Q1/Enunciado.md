Período: 24.1
Lista: 5
Questão: 01 
Dificuldade: Easy

**The Witcher 3: Wild Hunt**

Geralt de Rivia, um renomado caçador de monstros conhecido como Witcher, está em busca da sua filha adotiva, Ciri, enquanto ele precisa enfrentar inúmeros desafios. Para ter sucesso nessa perigosa missão, Geralt chamou você, um habilidoso programador na disciplina de IP, para juntar-se a ele na jornada que está por vir.

![geralt](https://media1.tenor.com/m/QmJWLHJOfT8AAAAC/geralt-of.gif)

#


Durante uma das missões dessa intensa jornada, vocês estão em busca de novas informações sobre o paradeiro de Ciri. Sabendo que estão próximos a uma fortaleza que esconde um sábio vidente, conhecedor de informações valiosas e disposto a ajudá-los, vocês estão determinados a encontrar e questioná-lo sobre a possível localização da filha de Geralt.

Contudo, existe um problema que os impede de acessar a fortaleza no momento: em sua entrada, uma enigmática máquina computacional exige duas sequências de números que liberam a passagem do castelo, funcionando como uma espécie de login e senha, obtidas, por sua vez, a partir de um código também composto por números.

Para resolver o enigma, a partir do código fornecido pela máquina, e acessar a fortaleza, Witcher contará com sua ajuda. Sua tarefa será criar um programa que utilize apenas funções recursivas para decifrar o login e a senha que devem desbloquear o acesso a área secreta e, consequentemente, finalizar essa missão.

A entrada será única, contendo um código que consiste em uma sequência de números, separados entre si por dois pontos (:).

>
> **N1:N2:N3:(…):Ni**
>

#

**Exemplos de entrada: 3:4:2:1, 2:3:5...**

#

**OBS: O tamanho da sequência, ou seja, a quantidade de números, é variável (indeterminado).**

O processo de **decodificação** das credenciais de acesso da área secreta da fortaleza consiste em **duas etapas**, para o cálculo das **sequências numéricas** de **login** e de **senha**, respectivamente.

#

Para decifrar a **sequência de números do login**, o seguinte deve ser feito:

- **Para cada numeral N da entrada**, deve-se percorrer todos os números no intervalo de **N até 0 (inclusive)**, somando-os da seguinte forma:
- Caso o número seja **par**, adicione ao **somatório** o **dobro desse número.**
- Caso o número seja **ímpar**, adicione ao **somatório** o **triplo desse número.**
- O **somatório** de **cada numeral** será uma **parte do login**, que é obtido por completo ao **concatenar** todos os **somatórios calculados**, do primeiro ao último numeral da entrada - nessa ordem.

#

Já para decifrar a **sequência de números da senha**, faça o seguinte:

- **Para cada numeral N da entrada**, deve-se calcular o seu **fatorial.**
- O **fatorial de cada númeral** será uma **parte da senha**, que é obtida por completo ao **concatenar** todos os **fatoriais** obtidos, do primeiro ao último numeral da entrada - nessa ordem.

#

**EXEMPLO:**
- Sequência de entrada: 2:4:1
- Decodificação do login:
    - L1: (2 * 2) + (1 * 3) = 4 + 3 = 7
    - L2: (4 * 2) + (3 * 3) + (2 * 2) + (1 * 3) = 8 + 9 + 4 + 3 = 24
    - L3: (1 * 3) = 3
    - Login: 7243
- Decodificação da senha:
    - S1: 2! = 2
    - S2: 4! = 24
    - S3: 1! = 1
    - Senha: 2241

#

O output será formado pelo anúncio de que o acesso à fortaleza foi desbloqueado, seguido das credenciais de acesso obtidas (login e senha):

>
> **As credenciais de acesso da área secreta da fortaleza foram decodificadas com sucesso!**
>
> **Login: {login_decifrado}**
>
> **Senha: {senha_decifrada}**
>

#

**ATENÇÃO: É OBRIGATÓRIO o uso de funções RECURSIVAS nas etapas de decodificação do login e da senha para o acesso da fortaleza.**