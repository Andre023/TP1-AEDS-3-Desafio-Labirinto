from Lab import Labirinto

filename = input("Digite o nome do arquivo (0 para sair): ")
if filename != "0":
    try:
        l = Labirinto()
        l.readMapFile(filename)
        l.solve()
        print(l)
    except Exception as e:
        print(e)
