# Programa para exibir uma estrela de 5 pontas
import math

# Configurações da estrela
tamanho = 15  # Tamanho da estrela

# Gera as coordenadas da estrela
def gerar_estrela(tamanho):
    angulo_base = 2 * math.pi / 5  # Ângulo entre os pontos
    pontos = []
    for i in range(10):
        raio = tamanho if i % 2 == 0 else tamanho / 2
        angulo = i * angulo_base
        x = raio * math.cos(angulo)
        y = raio * math.sin(angulo)
        pontos.append((x, y))
    return pontos

# Gera o desenho da estrela
def desenhar_estrela(tamanho):
    pontos = gerar_estrela(tamanho)
    for y in range(-tamanho, tamanho + 1):
        linha = ""
        for x in range(-tamanho * 2, tamanho * 2 + 1):
            dentro = False
            for px, py in pontos:
                if abs(x - px) < 1 and abs(y - py) < 1:
                    dentro = True
                    break
            linha += "*" if dentro else " "
        print(linha)

# Desenha a estrela
desenhar_estrela(tamanho)
input()
