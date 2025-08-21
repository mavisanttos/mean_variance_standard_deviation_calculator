import numpy as np #  importa o Numpy

def calculate(lista): # cria uma função
    if len(lista) != 9: # verifica se a lista tem 9 elementos
        raise ValueError('List must contain nine numbers.') # dá erro caso a lista não tenha 9 números

    matriz = np.array(lista).reshape(3, 3)  # cria matriz 3x3 a partir da lista

    calculations = { # cria o dicionário
        'mean': [ # média dos valores da matriz
            np.mean(matriz, axis=0).tolist(),  # calcula a média por coluna
            np.mean(matriz, axis=1).tolist(),  # calcula a média por linha
            np.mean(matriz).tolist()           # calcula a média total
        ],
        'variance': [ # variância dos valores da matriz
            np.var(matriz, axis=0).tolist(),  # calcula a variância por coluna
            np.var(matriz, axis=1).tolist(),  # calcula a variância por linha
            np.var(matriz).tolist()           # calcula a variância total
        ],
        'standard deviation': [ # desvio-padrão dos valores da matriz
            np.std(matriz, axis=0).tolist(),  # calcula a desvio-padrão por coluna
            np.std(matriz, axis=1).tolist(),  # calcula a desvio-padrão por linha
            np.std(matriz).tolist()           # calcula a desvio-padrão total
        ],
        'max': [ # máximo dos valores da matriz
            np.max(matriz, axis=0).tolist(),  # calcula o número máximo da coluna
            np.max(matriz, axis=1).tolist(),  # calcula o número máximo da linha
            np.max(matriz).tolist()           # calcula o número máximo do total
        ],
        'min': [ # mínimo dos valores da matriz
            np.min(matriz, axis=0).tolist(),  # calcula o número mínimo da coluna
            np.min(matriz, axis=1).tolist(),  # calcula o número mínimo da linha
            np.min(matriz).tolist()           # calcula o número mínimo do total
        ],
        'sum': [ # soma dos valores da matriz
            np.sum(matriz, axis=0).tolist(),  # calcula a soma da coluna
            np.sum(matriz, axis=1).tolist(),  # calcula a soma da linha
            np.sum(matriz).tolist()           # calcula a soma total
        ]
    }

    return calculations # retorna o dicionário definido pela função