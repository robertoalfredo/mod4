# operacoes.py

def calcular_media(notas):
    """Calcula a média das notas fornecidas."""
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """Verifica se o aluno foi reprovado (média inferior a 6)."""
    return media < 6

def identificar_reprovados(alunos, reprovados):
    """Identifica e retorna os alunos reprovados com suas médias."""
    resultados = []
    for matricula in reprovados:
        aluno = alunos[matricula]
        resultado = f"Aluno Reprovado: {aluno['nome']} – Matrícula: {matricula} – Média Final: {aluno['media']:.2f}"
        resultados.append(resultado)
    return resultados

