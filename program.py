import time

print("\n")
print("-----------------------------------------------------");
print("|Programa para inverter posições do arquivo de texto|")
print("-----------------------------------------------------")
print("\n\n\n\n\n")

input("Pressione enter para iniciar...")
print("\n\n\n\n\n")

def loading_bar():
    while True:
        for i in range(1, 51):
            print(f"\rCarregando... {i * 2}% [{'|' * i + ' ' * (50 - i)}]", end='')
            time.sleep(0.01)
        break
loading_bar()

def inverter_texto(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as entrada:
        linhas = entrada.readlines()

    with open(arquivo_saida, 'w') as saida:
        for linha in linhas:
            if len(linha) >= 445:
                parte1 = linha[:394]
                parte2 = linha[400:444]
                parte3 = linha[394:400]
                linha_invertida = parte1 + parte2  + parte3 + "\n"
                saida.write(linha_invertida)
            else:
                saida.write(linha)
    print("\n\n\n\n")
    print("Texto invertido com sucesso!\n")
    


arquivo_entrada = "input.txt"
arquivo_saida = "output.txt"

inverter_texto(arquivo_entrada, arquivo_saida)

input("Pressione enter para sair...")