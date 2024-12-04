def soma(codigo_referente):
    if codigo_referente == 0:
        return 0
    else:
        if codigo_referente % 2 == 0:
            return codigo_referente + soma(codigo_referente - 2)
        else:
            return soma(codigo_referente - 1)

codigo_referente = int(input())
senha_para_acesso = soma(codigo_referente) 
print (f"A senha para a área secreta da foretaleza é: {senha_para_acesso}")
