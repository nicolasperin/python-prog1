altura_anacleto = 1.5
altura_felisberto = 1.1
cont = 1
while altura_felisberto < altura_anacleto:
    altura_anacleto = altura_anacleto + 0.02
    altura_felisberto = altura_felisberto + 0.03
    cont += 1

print("Vai demorar %d anos para que Felisberto seja maior que Anacleto" %cont)