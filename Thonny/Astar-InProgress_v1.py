import pyxel
import random
from queue import PriorityQueue

def h_score(celula, destino):
    linhac = celula[0]
    colunac = celula[1]
    linhad = destino[0]
    colunad = destino[1]
    return abs(colunac - colunad) + abs(linhac -linhad)
def aestrela(celula_inicial,  grid, mapa):
    #criar todo tabuleiro com o f_score infinito
    f_score = {celula: float("inf") for celula in grid}
    g_score = {}
    #calcular o valor da celula inicial
    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
    
    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial)
    fila.put(item)
    
    #queue = []
    #queue.append(item)
    caminho = {}
    while not fila.empty():
        celula = fila.get()[2]
        #celula = queue[0][2]
        if celula == destino:
            break
        for direcao in "NSEW":
            if mapa[celula][direcao] == 1:
                coluna_celula = celula[0]
                linha_celula = celula[1]
                if direcao == "N":
                    proxima_celula = (coluna_celula, linha_celula - 1)
                elif direcao == "S":
                    proxima_celula = (coluna_celula, linha_celula + 1)
                elif direcao == "W":
                    proxima_celula = (coluna_celula - 1, linha_celula)
                elif direcao == "E":
                    proxima_celula = (coluna_celula + 1, linha_celula)
                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_celula, destino)
                
                if novo_f_score < f_score[proxima_celula]:
                    
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    item = (novo_f_score, h_score(proxima_celula, destino), proxima_celula)
                    fila.put(item)
                    caminho[proxima_celula] = celula
                    
                    #del queue[0]
                    #queue.append(item)
                    
    
    #caminhar a partir da celula inicial explorando os proximos caminhos
        #para cada possibilidade de caminho
            # se o caminho é possivel
                # calcular o f_score dos caminhos possiveis
                # se o f_score calculado < f_score antigo
                    # substituir o f_score antigo pelo calculado
                    #escolher o caminho para seguir que tem:
                        # o menor f_score
                        # se os f_score forem iguais, que tem menor h_score 
    caminho_final = {}
    celula_analisada = destino
    while celula_analisada != celula_inicial:
        caminho_final[caminho[celula_analisada]] = celula_analisada
        celula_analisada = caminho[celula_analisada]
    return caminho_final



def update():
    pass

def draw():
    #desenha onde o agente esta
    pyxel.pset(inicio[0], inicio[1], 1)
    if pyxel.frame_count % 15 == 0 and (agente[0] != destino[0] or agente[1] != destino[1]):
        pyxel.pset(agente[0], agente[1] ,2)
        pyxel.pset(caminho[(agente[0], agente[1])][0], caminho[(agente[0], agente[1])][1], 2)
        
        agente[0] = caminho[(agente[0], agente[1])][0]
        agente[1] = caminho[(agente[0], agente[1])][1]

pyxel.init(50, 50)
count = 0
pyxel.cls(7)
grid = []
dir_map = {}

for i in range(pyxel.width):
    for j in range(pyxel.height):
        grid.append((i, j))
agente = [49, 49]
inicio = (49, 49)
destino = (0, 0)
for i in range (2000):
    pyxel.pset(random.randint(0, 99), random.randint(0, 99), 0)
pyxel.pset(49, 49, 3)
pyxel.pset(0, 0, 7)

for i in range(pyxel.width ):
    for j in range(pyxel.height):
        #norte
        if (j-1 < 0) or (pyxel.pget(i, j-1) == 0):
            N = 0
        else:
            N = 1
        #sul
        if (j+1 >= pyxel.height ) or (pyxel.pget(i, j+1) == 0):
            S = 0
        else:
            S = 1
        #leste (east)
        if (i+1 >= pyxel.width) or (pyxel.pget(i+1, j) == 0):
            E = 0
        else:
            E = 1   
        #oeste (west)
        if (i-1 < 0) or (pyxel.pget(i-1, j) == 0):
            W = 0
        else:
            W = 1
        dir_map.update({(i, j):{"N": N,"S": S,"E": E,"W": W}})
caminho = aestrela(inicio ,grid, dir_map)
print(caminho)
pyxel.run(update, draw)