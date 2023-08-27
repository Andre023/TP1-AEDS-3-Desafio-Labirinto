# README para o projeto Labirinto em Python

## Descrição

Este projeto resolve labirintos usando o algoritmo de busca em profundidade (DFS). O programa lê um mapa de um arquivo ou de uma string e identifica o caminho mais curto entre o ponto de início e o ponto de saída.

## Variáveis

- `parede = '#'`: Representa uma parede no labirinto
- `corredor = ' '`: Representa um corredor no labirinto
- `percorrido = '='`: Representa uma célula que foi percorrida
- `errado = 'x'`: Representa um caminho errado
- `correto = '.'`: Representa um caminho correto
- `start = 'S'`: Representa o ponto de partida
- `exit = 'E'`: Representa o ponto de saída

## Classes e Métodos

### Classe Labirinto

#### `readMap(self, text)`

Lê o mapa a partir de um texto e inicializa as posições de início e saída.

#### `readMapFile(self, file)`

Lê o mapa de um arquivo e chama o método `readMap`.

#### `__str__(self)`

Retorna uma representação em string do labirinto.

#### `dfs(self, state, pos, moves, path)`

Implementa o algoritmo DFS para encontrar o caminho do labirinto. Modifica o estado atual do mapa com o caminho encontrado.

#### `solve(self)`

Resolve o labirinto e imprime o tempo total necessário e o caminho encontrado.

## Como usar

1. Instale Python 3.x no seu sistema.
2. Faça o download do arquivo
3. Execute o arquivo main.py.

