def bis(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input(" digite um ano: "))

if bis(ano):
    print("Sim, o ano", ano, "é bissexto")
else:
    print("Não, o ano", ano, "não é bissexto.")
    #Rafael e Vitória 