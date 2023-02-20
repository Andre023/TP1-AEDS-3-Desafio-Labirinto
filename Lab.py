import time

parede = '#'
corredor = ' '
percorrido = '='
errado = 'x'
correto = '.'
start = 'S'
exit = 'E'

class Labirinto(object):
    def readMap(self, text):
        self.map = text.split('\n')
        for i, l in enumerate(self.map):
            p = l.find(start)
            if p >= 0:
                self.start = (i, p)
            p = l.find(exit)
            if p >= 0:
                self.exit = (i, p)
            self.map[i] = list(l)
        if not self.start:
            raise ValueError("O mapa não possui uma entrada!")
        if not self.exit:
            raise ValueError("O mapa não possui uma saída!")

    def readMapFile(self, file):
        with open(file, 'r') as f:
            self.readMap(f.read())

    def __str__(self):
        output = ""
        for row in self.map:
            for col in row:
                output += col + " "
            output += "\n"
        return output

    def dfs(self, state, pos, moves, path):
        y, x = pos          # extrai as coordenadas da posição atual
        if state[y][x] == exit:  # Se a posição atual for a saída, retorna True (achou o caminho)
            return True
        if state[y][x] != start:
                                    # Marca a posição atual como percorrida, exceto se for a entrada
            state[y][x] = percorrido
        for move in moves:  # para cada movimento possível
            dy, dx, label = move    # extrai as coordenadas relativas e a direção do movimento
            new_y, new_x = y + dy, x + dx    # calcula as novas coordenadas
            if 0 <= new_y < len(state) and 0 <= new_x < len(state[0]): # Verifica se as novas coordenadas estão dentro do mapa
                if state[new_y][new_x] not in [percorrido, errado, start]:  # Verifica se a nova posição ainda não foi visitada ou é a entrada
                    if state[new_y][new_x] in [corredor, exit]: # Se a nova posição é um corredor ou a saída, chama recursivamente a função
                        if self.dfs(state, (new_y, new_x), moves, path): # Se encontrou o caminho, marca a posição atual como correta
                            state[y][x] = correto # Adiciona a posição atual ao caminho
                            path.append((y, x)) # Retorna True (achou o caminho)
                            return True
                    elif state[new_y][new_x] == parede:
                        continue
            state[y][x] = errado
        return False

    def solve(self):
        start_time = time.time()
        moves = [(0, 1, 'E'), (0, -1, 'W'), (1, 0, 'S'), (-1, 0, 'N')]
        state = [row[:] for row in self.map]
        path = []
        if self.dfs(state, self.start, moves, path):
            self.map = [''.join(row) for row in state]
        else:
            raise ValueError("O labirinto não possui solução.")
        end_time = time.time()
        print("Tempo total: {:.5f} segundos".format(end_time - start_time))
        print("Caminho de S a E:")
        
        # Adiciona elementos de path em uma lista como uma pilha
        stack = []
        for p in path:
            stack.append(p)
            
        # Remove elementos da lista como uma pilha e imprime
        while stack:
            print(stack.pop(), end=" ")
        print("\n")

        return self.map