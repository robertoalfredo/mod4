from operacoes import calcular_media, verificar_reprovacao, identificar_reprovados

# Estruturas de dados para armazenar os alunos e suas notas
alunos = {
    101: {'nome': 'Alice', 'notas': [7.5, 6.0, 8.0, 5.5]},
    102: {'nome': 'Bruno', 'notas': [4.0, 5.5, 3.0, 4.5]},
    103: {'nome': 'Carla', 'notas': [9.0, 8.5, 7.5, 8.0]},
    104: {'nome': 'Daniel', 'notas': [6.0, 5.5, 5.0, 4.5]},
}

# Lista para armazenar os números de matrícula dos alunos reprovados
reprovados = []

# Processamento das médias e verificação de reprovação
for matricula, dados in alunos.items():
    media = calcular_media(dados['notas'])
    alunos[matricula]['media'] = media
    if verificar_reprovacao(media):
        reprovados.append(matricula)

# Identificação dos alunos reprovados
resultados = identificar_reprovados(alunos, reprovados)

# Exibição dos resultados
for resultado in resultados:
    print(resultado)