idade_str = input("Digite sua idade:")
idade = int(idade_str)

maior_idade = idade > 18
crianca = idade <= 12
adolescente = idade > 12

if (maior_idade):
    print("Voce é maior de idade.")

else:
    if(crianca):
        print("Voce é uma crianca.")
    elif(adolescente):
        print("Voce é um adolescente.")
