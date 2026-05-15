####################################################################################
##################################### Proj2 ########################################
####################################################################################

letras = 'ABCÇDEFGHIJLMNOPQRSTUVXZ'

# Representação interna do TAD casa:
# O TAD casa é representado por um tuplo imutável de dois inteiros (linha, coluna),
# onde cada valor está entre 1 e 15 inclusive. Esta representação é hashable e imutável,
# conforme exigido no enunciado.

# Assinaturas das operações básicas do TAD casa:
# - Construtor:
#   cria_casa: int × int --> casa
# - Seletores:
#   obtem_lin: casa --> int
#   obtem_col: casa --> int
# - Reconhecedor:
#   eh_casa: universal --> bool
# - Teste:
#   casas_iguais: universal × universal --> bool
# - Transformadores:
#   casa_para_str: casa --> str
#   str_para_casa: str --> casa

# Função de alto nível associada ao TAD casa:
# incrementa_casa: casa × str × int --> casa

#2.1.1 TAD casa

def cria_casa(lin, col):
    """
    cria_casa: inteiro × inteiro --> casa
    Recebe dois inteiros (lin para linha, col para coluna) entre 1 e 15, devolve um tuplo representando a casa.
    Gera ValueError com mensagem 'cria_casa: argumentos inválidos' se os argumentos forem inválidos.
    """

    if not (isinstance(lin, int) and isinstance(col, int) and 1 <= lin <= 15 and 1 <= col <= 15):
        raise ValueError("cria_casa: argumentos inválidos")
    
    return (lin, col)

def obtem_lin(l):
    """
    obtem_lin: casa --> inteiro
    Devolve a linha da casa c.
    """


    if not eh_casa(l):
        raise ValueError("obtem_lin: argumento inválido")
    
    return l[0]

def obtem_col(c):
    """
    obtem_col: casa --> inteiro
    Devolve a coluna da casa c.
    """

    if not eh_casa(c):
        raise ValueError("obtem_col: argumento inválido")
    
    return c[1]

def eh_casa(arg):
    """
    eh_casa: universal --> booleano
    Devolve True se arg é um TAD casa (tuplo com dois inteiros entre 1 e 15), False caso contrário.
    """

    return (isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int) and isinstance(arg[1], int) and 1 <= arg[0] <= 15 and 1 <= arg[1] <= 15)

def casas_iguais(c1, c2):
    """
    casas_iguais: universal × universal --> booleano
    Devolve True se c1 e c2 são casas e são iguais, False caso contrário.
    """

    return eh_casa(c1) and eh_casa(c2) and c1 == c2

def casa_para_str(c):
    """
    casa_para_str: casa --> cad. carateres
    Devolve a representação da casa c como cadeia de carateres no formato '(lin,col)'.
    """

    if not eh_casa(c):
        raise ValueError("casa_para_str: argumento inválido")
    
    return f"({obtem_lin(c)},{obtem_col(c)})"

def str_para_casa(s):
    """
    str_para_casa: cad. carateres --> casa
    Devolve a casa representada pela cadeia s no formato '(lin,col)'.
    Gera ValueError com mensagem 'str_para_casa: argumento inválido' se s for inválido.
    """

    if not (isinstance(s, str) and s.startswith('(') and s.endswith(')')):
        raise ValueError("str_para_casa: argumento inválido")
    
    try:
        # Remove parênteses e divide pela vírgula
        nums = s[1:-1].split(',')

        if len(nums) != 2:
            raise ValueError
        
        lin, col = int(nums[0]), int(nums[1])
        return cria_casa(lin, col)
    
    except (ValueError, TypeError):
        raise ValueError("str_para_casa: argumento inválido")

def incrementa_casa(c, d, s):
    """
    incrementa_casa: casa × cad. carateres × inteiro --> casa
    Devolve a casa a seguir de c na direção d ('H' ou 'V') a uma distância s (inteiro positivo).
    Se a casa resultante for inválida (fora de 1-15), devolve c.
    """
    if not (eh_casa(c) and d in ('H', 'V') and isinstance(s, int) and s > 0):
        return c
    lin, col = obtem_lin(c), obtem_col(c)
    if d == 'H':
        nova_col = col + s
        if 1 <= nova_col <= 15:
            return cria_casa(lin, nova_col)
    else:  # d == 'V'
        nova_lin = lin + s
        if 1 <= nova_lin <= 15:
            return cria_casa(nova_lin, col)
    return c

# Representação interna do TAD jogador:
# O TAD jogador é representado por um dicionário mutável com chaves 'tipo' ('humano' ou 'agente'),
# 'identidade' (nome ou nível), 'pontos' (inteiro), e 'letras' (string ordenada de letras maiúsculas).
# Esta representação permite modificações destrutivas nos modificadores.

# Assinaturas das operações básicas do TAD jogador:
# - Construtores:
#   cria_humano: str --> jogador
#   cria_agente: str --> jogador
# - Seletores:
#   jogador_identidade: jogador --> str
#   jogador_pontos: jogador --> int
#   jogador_letras: jogador --> str
# - Modificadores:
#   recebe_letra: jogador × str --> jogador
#   usa_letra: jogador × str --> jogador
#   soma_pontos: jogador × int --> jogador
# - Reconhecedores:
#   eh_jogador: universal --> bool
#   eh_humano: universal --> bool
#   eh_agente: universal --> bool
# - Teste:
#   jogadores_iguais: universal × universal --> bool
# - Transformador:
#   jogador_para_str: jogador --> str

# Função de alto nível associada ao TAD jogador:
# distribui_letras: jogador × list × int --> jogador

#TAD Jogador 2.1.2

def cria_humano(nome):
    """
    cria_humano: str --> jogador
    Recebe uma cadeia de carateres (não vazia) a representar o nome do jogador e devolve um jogador humano com 0 pontos e sem letras.
    Gera ValueError com mensagem 'cria_humano: argumento inválido' se o argumento for inválido.
    """

    if not (isinstance(nome, str) and nome.strip()):
        raise ValueError("cria_humano: argumento inválido")
    
    return {'tipo': 'humano', 'identidade': nome.strip(), 'pontos': 0, 'letras': ''}

def cria_agente(nivel):
    """
    cria_agente: str --> jogador
    Recebe uma cadeia de carateres a representar o nível ('FACIL', 'MEDIO' ou 'DIFICIL') e devolve um jogador agente com 0 pontos e sem letras.
    Gera ValueError com mensagem 'cria_agente: argumento inválido' se o argumento for inválido.
    """

    niveis_validos = {'FACIL', 'MEDIO', 'DIFICIL'}

    if not (isinstance(nivel, str) and nivel in niveis_validos):
        raise ValueError("cria_agente: argumento inválido")
    
    return {'tipo': 'agente', 'identidade': nivel, 'pontos': 0, 'letras': ''}

def jogador_identidade(j):
    """
    jogador_identidade: jogador --> str
    Devolve o nome do jogador j se humano ou o nível se agente.
    """
    
    return j['identidade']

def jogador_pontos(j):
    """
    jogador_pontos: jogador --> int
    Devolve os pontos do jogador j.
    """

    return j['pontos']

def jogador_letras(j):
    """
    jogador_letras: jogador --> str
    Devolve a cadeia de carateres ordenada com todas as letras do jogador j.
    """

    return ''.join(sorted(j['letras'], key=lambda x: letras.index(x)))

def recebe_letra(j, l):
    """
    recebe_letra: jogador × str --> jogador
    Modifica destrutivamente o jogador j acrescentando a letra l às suas letras, devolve o próprio jogador.
    """
    if not (isinstance(l, str) and len(l) == 1 and l.isalpha()):
        raise ValueError("recebe_letra: argumento inválido")
    
    j['letras'] += l.upper()
    j['letras'] = ''.join(sorted(j['letras'], key=lambda x: letras.index(x)))
    return j

def usa_letra(j, l):
    """
    usa_letra: jogador × str --> jogador
    Modifica destrutivamente o jogador j retirando a letra l das suas letras, devolve o próprio jogador.
    """
    if not (isinstance(l, str) and len(l) == 1 and l.isalpha() and l.upper() in j['letras']):
        raise ValueError("usa_letra: argumento inválido")
    
    j['letras'] = j['letras'].replace(l.upper(), '', 1)
    j['letras'] = ''.join(sorted(j['letras'], key=lambda x: letras.index(x)))
    return j

def soma_pontos(j, p):
    """
    soma_pontos: jogador × int --> jogador
    Modifica destrutivamente o jogador j somando os pontos p à sua pontuação atual, devolve o próprio jogador.
    """
    if not (isinstance(p, int) and p >= 0):
        raise ValueError("soma_pontos: argumento inválido")
    
    j['pontos'] += p
    return j

def eh_jogador(arg):
    """
    eh_jogador: universal --> bool
    Devolve True se arg é um TAD jogador, False caso contrário.
    """

    return (isinstance(arg, dict) and 'tipo' in arg and 'identidade' in arg and 'pontos' in arg and 'letras' in arg and arg['tipo'] in ('humano', 'agente') and isinstance(arg['identidade'], str) and isinstance(arg['pontos'], int) and isinstance(arg['letras'], str))

def eh_humano(arg):
    """
    eh_humano: universal --> bool
    Devolve True se arg é um TAD jogador humano, False caso contrário.
    """

    return eh_jogador(arg) and arg['tipo'] == 'humano'

def eh_agente(arg):
    """
    eh_agente: universal --> bool
    Devolve True se arg é um TAD jogador agente, False caso contrário.
    """

    return eh_jogador(arg) and arg['tipo'] == 'agente'

def jogadores_iguais(j1, j2):
    """
    jogadores_iguais: universal × universal --> bool
    Devolve True apenas se j1 e j2 forem jogadores e forem iguais.
    """
    
    return eh_jogador(j1) and eh_jogador(j2) and j1 == j2

def jogador_para_str(j):
    """
    jogador_para_str: jogador --> str
    Devolve a cadeia de caracteres que representa o jogador como 'nome (pontos): letras' (humano) ou 'BOT(nivel) (pontos): letras' (agente).
    """

    if not eh_jogador(j):
        raise ValueError("jogador_para_str: argumento inválido")
    
    prefixo = f"{j['identidade']}" if eh_humano(j) else f"BOT({j['identidade']})"
    letras_str = ' '.join(jogador_letras(j)) if j['letras'] else ""
    return f"{prefixo} ({j['pontos']:3}):" + (f" {letras_str}" if letras_str else "")

def distribui_letras(jog, saco, num):
    """
    distribui_letras: jogador × list × int --> jogador
    Retira um máximo de num letras do final da lista saco e as acrescenta ao jogador jog, devolvendo o jogador.
    Modifica destrutivamente saco e jog.
    """

    if not (eh_jogador(jog) and isinstance(saco, list) and all(isinstance(l, str) and len(l) == 1 and l.isalpha() for l in saco) and isinstance(num, int) and num >= 0):
        raise ValueError("distribui_letras: argumento inválido")
    
    letras_a_distribuir = min(num, len(saco))
    
    for _ in range(letras_a_distribuir):
        if saco:
            letra = saco.pop()
            recebe_letra(jog, letra)
    
    return jog

# Representação interna do TAD vocabulário:
# O TAD vocabulário é representado por um dicionário aninhado: {comprimento: {primeira_letra: [lista de palavras]}},
# permitindo procura acelerada por comprimento e primeira letra. As palavras são únicas e em maiúsculas.

# Assinaturas das operações básicas do TAD vocabulário:
# - Construtor:
#   cria_vocabulario: tuple --> vocabulário
# - Seletores:
#   obtem_pontos: vocabulário × str --> int
#   obtem_palavras: vocabulário × int × str --> tuple

# Funções de alto nível associadas ao TAD vocabulário:
# testa_palavra_padrao: vocabulário × str × str × str --> bool
# ficheiro_para_vocabulario: str --> vocabulário
# vocabulario_para_str: vocabulário --> str
# procura_palavra_padrao: vocabulário × str × str × int --> tuple

#TAD Vocabolario 2.1.3

def cria_vocabulario(v):
    """
    cria_vocabulario: tuple --> vocabulario
    Devolve o vocabulário que contém as palavras do tuplo v, verificando se contém pelo menos uma palavra única, com comprimento entre 2 e 15, e letras maiúsculas do alfabeto português.
    Gera ValueError com mensagem 'cria_vocabulario: argumento inválido' se o argumento for inválido.
    """
    if not (isinstance(v, tuple) and v and all(isinstance(p, str) for p in v) and len(set(v)) == len(v)):
        raise ValueError("cria_vocabulario: argumento inválido")
    
    vocab = {}

    for palavra in v:
        if not (isinstance(palavra, str) and 2 <= len(palavra) <= 15 and all(c.isupper() and c in letras for c in palavra)):
            raise ValueError("cria_vocabulario: argumento inválido")
        
        comp = len(palavra)

        if comp not in vocab:
            vocab[comp] = {}

        if palavra[0] not in vocab[comp]:
            vocab[comp][palavra[0]] = []

        if palavra not in vocab[comp][palavra[0]]:
            vocab[comp][palavra[0]].append(palavra)

    return vocab


def obtem_pontos(vocab, palavra):
    """
    obtem_pontos: vocabulario × str --> int
    Devolve os pontos da palavra no vocabulário, ou 0 se não encontrada.
    """
    pontos_letras = {'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 4, 'H': 4,
                    'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1,
                    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8}
    
    palavra = palavra.upper()
    
    if not (isinstance(palavra, str) and palavra and all(c in pontos_letras for c in palavra)):
        return 0
    
    # Verifica se a palavra existe no vocabulário
    comp = len(palavra)
    if comp in vocab and palavra[0] in vocab[comp] and palavra in vocab[comp][palavra[0]]:
        return sum(pontos_letras[c] for c in palavra)
    return 0


def obtem_palavras(vocab, comp, letra):
    """
    obtem_palavras: vocabulario × int × str --> tuple
    Devolve tuplo de pares (palavra, pontuação) com comprimento comp e primeira letra letra, ordenados por pontuação decrescente e lexicograficamente em caso de empate.
    """

    if not (isinstance(comp, int) and isinstance(letra, str) and len(letra) == 1 and letra.isupper()):
        return ()
    
    if comp not in vocab or letra not in vocab[comp]:
        return ()
    
    def normalize(s):
        return s.replace('Ç', 'C')
    
    palavras = [(p, obtem_pontos(vocab, p)) for p in vocab[comp][letra]]
    return tuple(sorted(palavras, key=lambda x: (-x[1], normalize(x[0]))))


def testa_palavra_padrao(vocab, palavra, padrao, letras):
    """
    testa_palavra_padrao: vocabulario × str × str × str --> bool
    Devolve True se palavra existe no vocabulário e pode ser formada substituindo '.' em padrao por letras, False caso contrário.
    """
    if not all(c in '.ABCDEFGHIJLMNOPQRSTUVXZÇ' for c in padrao):
        return False
    
    palavra = palavra.upper()
    padrao = padrao.upper()
    letras = letras.upper()
    
    if palavra not in vocab.get(len(palavra), {}).get(palavra[0], []):  # Simplificado, removi any desnecessário
        return False
    
    needed = [palavra[i] for i in range(len(padrao)) if padrao[i] == '.']
    for l in set(needed):
        if needed.count(l) > letras.count(l):
            return False
    
    for i in range(len(palavra)):
        if padrao[i] != '.' and padrao[i] != palavra[i]:
            return False
        
    return True

def ficheiro_para_vocabulario(nome_fich):
    """
    ficheiro_para_vocabulario: str --> vocabulario
    Devolve o vocabulário formado pelas palavras do ficheiro nome_fich,
    ignorando linhas vazias e convertendo palavras válidas (2-15 letras) para maiúsculas.
    """
    vocab = {}
    try:
        with open(nome_fich, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
    except FileNotFoundError:
        raise ValueError("ficheiro_para_vocabulario: ficheiro não encontrado")

    for linha in linhas:
        palavra = linha.strip()
        if palavra and 2 <= len(palavra) <= 15 and all(c.isalpha() for c in palavra):
            palavra = palavra.upper()
            if not all(c in letras for c in palavra):
                continue
            comp = len(palavra)
            if comp not in vocab:
                vocab[comp] = {}
            if palavra[0] not in vocab[comp]:
                vocab[comp][palavra[0]] = []
            if palavra not in vocab[comp][palavra[0]]:
                vocab[comp][palavra[0]].append(palavra)

    return vocab


def vocabulario_para_str(vocab):
    """
    vocabulario_para_str: vocabulario -->> str
    Devolve cadeia com todas as palavras ordenadas por comprimento crescente, depois por primeira letra, e por pontuação decrescente/lexicográfica.
    """
    
    def normalize(s):
        return s.replace('Ç', 'C')
    
    resultado = []
    for comp in sorted(vocab.keys()):
        for letra in sorted(vocab[comp].keys()):
            lista_palavras = vocab[comp][letra]
            if not lista_palavras:
                continue
            
            # Ordena diretamente por -pontos e normalize
            sorted_palavras = sorted(lista_palavras, key=lambda p: (-obtem_pontos(vocab, p), normalize(p)))
            resultado.extend(sorted_palavras)

    return '\n'.join(resultado)

def procura_palavra_padrao(vocab, padrao, letras, min_pontos):
    """
    procura_palavra_padrao: vocabulario × str × str × int --> tuple
    Devolve tuplo (palavra, pontuação) da palavra com maior pontuação formável com letras, respeitando padrao e min_pontos, ou ('', 0) se não encontrada.
    """
    if not (isinstance(padrao, str) and isinstance(letras, str) and isinstance(min_pontos, int) and min_pontos >= 0):
        return ('', 0)
    
    padrao = padrao.upper()
    letras = letras.upper()
    
    def normalize(s):
        return s.replace('Ç', 'C')
    
    comp = len(padrao)
    melhor_palavra = ''
    melhor_pontos = 0

    if comp not in vocab:
        return ('', 0)

    if padrao[0].isalpha():
        if padrao[0] not in vocab[comp]:
            return ('', 0)
        
        for palavra in vocab[comp][padrao[0]]:
            if testa_palavra_padrao(vocab, palavra, padrao, letras) and obtem_pontos(vocab, palavra) >= min_pontos:
                pontos = obtem_pontos(vocab, palavra)

                if pontos > melhor_pontos or (pontos == melhor_pontos and normalize(palavra) < normalize(melhor_palavra)):
                    melhor_palavra, melhor_pontos = palavra, pontos
    else:
        for letra in sorted(set(letras.upper())):
                    # Remove uma instância da letra inicial das letras disponíveis para descontar o uso
                    letras_temp = letras.replace(letra, '', 1)
                    novo_padrao = letra + padrao[1:]

                    if letra in vocab[comp]:
                        for palavra in vocab[comp][letra]:
                            if testa_palavra_padrao(vocab, palavra, novo_padrao, letras_temp) and obtem_pontos(vocab, palavra) >= min_pontos:
                                pontos = obtem_pontos(vocab, palavra)

                                if pontos > melhor_pontos or (pontos == melhor_pontos and normalize(palavra) < normalize(melhor_palavra)):
                                    melhor_palavra, melhor_pontos = palavra, pontos

    return (melhor_palavra, melhor_pontos)

# Representação interna do TAD tabuleiro:
# O TAD tabuleiro é representado por uma lista mutável de 15 listas, cada uma com 15 strings
# ('.' para vazia ou letra maiúscula). Esta representação permite modificações destrutivas.

# Assinaturas das operações básicas do TAD tabuleiro:
# - Construtor:
#   cria_tabuleiro: {} --> tabuleiro
# - Seletores:
#   obtem_letra: tabuleiro × casa --> str
# - Modificadores:
#   insere_letra: tabuleiro × casa × str --> tabuleiro
# - Reconhecedores:
#   eh_tabuleiro: universal --> bool
#   eh_tabuleiro_vazio: universal --> bool
# - Teste:
#   tabuleiros_iguais: universal × universal --> bool
# - Transformador:
#   tabuleiro_para_str: tabuleiro --> str

# Funções de alto nível associadas ao TAD tabuleiro:
# obtem_padrao: tabuleiro × casa × casa --> str
# insere_palavra: tabuleiro × casa × str × str --> tabuleiro
# obtem_subpadroes: tabuleiro × casa × casa × int --> tuple × tuple
# gera_todos_padroes: tabuleiro × int --> tuple × tuple × tuple

#tad tabuleiro

def cria_tabuleiro():
    """
    cria_tabuleiro: {} --> tabuleiro
    Devolve um tabuleiro vazio representado por uma lista de 15 listas, cada uma com 15 elementos '.' (casas livres).
    """
    return [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


def obtem_letra(t, c):
    """
    obtem_letra: tabuleiro × casa → str
    Devolve a letra contida na casa c do tabuleiro t.
    """
    if not eh_tabuleiro(t) or not eh_casa(c):
        raise ValueError("obtem_letra: argumento inválido")
    
    lin, col = obtem_lin(c) - 1, obtem_col(c) - 1
    return t[lin][col]

def insere_letra(t, c, l):
    """
    insere_letra: tabuleiro × casa × str → tabuleiro
    Modifica destrutivamente o tabuleiro t colocando a letra l na casa c, devolve o próprio tabuleiro.
    """
    if not eh_tabuleiro(t) or not eh_casa(c) or not (isinstance(l, str) and len(l) == 1 and l in letras):
        raise ValueError("insere_letra: argumento inválido")
    
    lin, col = obtem_lin(c) - 1, obtem_col(c) - 1
    t[lin][col] = l

    return t

def eh_tabuleiro(arg):
    """
    eh_tabuleiro: universal → bool
    Devolve True se arg é um TAD tabuleiro, False caso contrário.
    """
    return (isinstance(arg, list) and len(arg) == 15 and all(isinstance(row, list) and len(row) == 15 for row in arg) and all(all(c in '.' + ''.join(letras) for c in row) for row in arg))

def eh_tabuleiro_vazio(arg):
    """
    eh_tabuleiro_vazio: universal → bool
    Devolve True se arg é um TAD tabuleiro vazio (sem letras), False caso contrário.
    """
    return eh_tabuleiro(arg) and all(all(c == '.' for c in row) for row in arg)

def tabuleiros_iguais(t1, t2):
    """
    tabuleiros_iguais: universal × universal → bool
    Devolve True apenas se t1 e t2 forem tabuleiros e forem iguais.
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2

def tabuleiro_para_str(t):
    """
    tabuleiro_para_str: tabuleiro → str
    Devolve a cadeia de caracteres que representa o tabuleiro com cabeçalho, linhas numeradas e bordas.
    """
    if not eh_tabuleiro(t):
        raise ValueError("tabuleiro_para_str: argumento inválido")
    
    resultado = "                       1 1 1 1 1 1\n"
    resultado += "     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5\n"
    resultado += "   +-------------------------------+\n"
    for i in range(15):
        linha = f"{i+1:2} |" if i < 9 else f"{i+1} |"

        for j in range(15):
            linha += f" {t[i][j]}"

        linha += " |\n"
        resultado += linha

    resultado += "   +-------------------------------+"

    return resultado

def obtem_padrao(t, i, f):
    """
    obtem_padrao: tabuleiro × casa × casa → str
    Devolve a sequência de letras contida no tabuleiro t entre a casa i e a casa f (ambas inclusive) na mesma linha ou coluna.
    """
    if not (eh_tabuleiro(t) and eh_casa(i) and eh_casa(f)):
        raise ValueError("obtem_padrao: argumento inválido")
    
    lin_i, col_i = obtem_lin(i) - 1, obtem_col(i) - 1
    lin_f, col_f = obtem_lin(f) - 1, obtem_col(f) - 1

    if lin_i == lin_f:  # Mesma linha
        if not (col_i <= col_f and lin_i < 15 and col_f < 15):
            raise ValueError("obtem_padrao: argumento inválido")
        
        return ''.join(t[lin_i][col] for col in range(col_i, col_f + 1))
    
    elif col_i == col_f:  # Mesma coluna
        if not (lin_i <= lin_f and col_i < 15 and lin_f < 15):
            raise ValueError("obtem_padrao: argumento inválido")
        
        return ''.join(t[lin][col_i] for lin in range(lin_i, lin_f + 1))
    else:

        raise ValueError("obtem_padrao: argumento inválido")

def insere_palavra(t, c, d, p):
    """
    insere_palavra: tabuleiro × casa × str × str → tabuleiro
    Modifica destrutivamente o tabuleiro t colocando a palavra p na casa c na direção d, devolve o próprio tabuleiro.
    """
    if not (eh_tabuleiro(t) and eh_casa(c) and d in ('H', 'V') and isinstance(p, str) and all(l in letras for l in p)):
        raise ValueError("insere_palavra: argumento inválido")
    
    lin, col = obtem_lin(c) - 1, obtem_col(c) - 1
    tam = len(p)

    if d == 'H' and (col + tam > 15):
        raise ValueError("insere_palavra: argumento inválido")
    
    if d == 'V' and (lin + tam > 15):
        raise ValueError("insere_palavra: argumento inválido")
    
    for i, l in enumerate(p):
        if d == 'H':
            lin_atual, col_atual = lin, col + i

        else:  # d == 'V'
            lin_atual, col_atual = lin + i, col

        if not (0 <= lin_atual < 15 and 0 <= col_atual < 15):
            raise ValueError("insere_palavra: argumento inválido")
        
        valor_atual = t[lin_atual][col_atual]

        if valor_atual != '.' and valor_atual != l:
            raise ValueError("insere_palavra: argumento inválido")
        
        t[lin_atual][col_atual] = l

    return t

def obtem_subpadroes(t, i, f, l):
    """
    obtem_subpadroes: tabuleiro × casa × casa × int → tuple × tuple
    Devolve dois tuplos: o primeiro com subpadrões viáveis (máximo l espaços livres), o segundo com casas de início correspondentes.
    """
    if not (eh_tabuleiro(t) and eh_casa(i) and eh_casa(f) and isinstance(l, int) and l >= 0):
        raise ValueError("obtem_subpadroes: argumentos inválidos")

    lin_i, col_i = obtem_lin(i) - 1, obtem_col(i) - 1
    lin_f, col_f = obtem_lin(f) - 1, obtem_col(f) - 1

    if lin_i == lin_f:
        direction = 'H'
        length = col_f - col_i + 1
    elif col_i == col_f:
        direction = 'V'
        length = lin_f - lin_i + 1
    else:
        raise ValueError("obtem_subpadroes: argumentos inválidos")

    padrao = obtem_padrao(t, i, f)
    
    def normalize(s):
        return s.replace('Ç', 'C')
    
    # Identificar blocos de letras
    blocks = []
    idx = 0
    while idx < length:
        if padrao[idx] != '.':
            start = idx
            while idx < length and padrao[idx] != '.':
                idx += 1
            blocks.append((start, idx - 1))
        else:
            idx += 1

    padroes = []
    casas = []
    n = len(blocks)

    # Gerar subpadrões para cada combinação de blocos
    for bi in range(n):
        for bj in range(bi, n):
            block_start = blocks[bi][0]
            block_end = blocks[bj][1]
            
            # Calcular espaços internos entre blocos
            internal = 0
            for k in range(bi, bj):
                gap = blocks[k+1][0] - blocks[k][1] - 1
                internal += gap
            
            # Determinar limites de espaços antes e depois
            if bi == 0:
                max_pre = block_start
            else:
                max_pre = block_start - blocks[bi-1][1] - 2
            
            if bj == n - 1:
                max_suf = length - 1 - block_end
            else:
                max_suf = blocks[bj+1][0] - block_end - 2
            
            max_pre = max(0, max_pre)
            max_suf = max(0, max_suf)
            
            # Gerar padrões com diferentes quantidades de espaços
            for pre in range(max_pre, -1, -1):
                for suf in range(max_suf, -1, -1):
                    total_dots = pre + suf + internal
                    if 1 <= total_dots <= l:
                        pattern = '.' * pre + padrao[block_start:block_end + 1] + '.' * suf
                        start_idx = block_start - pre
                        
                        if direction == 'V':
                            casa = cria_casa(lin_i + 1 + start_idx, col_i + 1)
                        else:
                            casa = cria_casa(lin_i + 1, col_i + 1 + start_idx)
                        
                        padroes.append(pattern)
                        casas.append(casa)
    if padroes:
        combined = list(zip(padroes, casas))
        combined.sort(key=lambda x: (obtem_lin(x[1]), obtem_col(x[1]), -len(x[0]), x[0]))
        padroes, casas = zip(*combined)
    else:
        padroes, casas = (), ()
    return tuple(padroes), tuple(casas)

def gera_todos_padroes(t, l):
    """
    gera_todos_padroes: tabuleiro × int → tuple × tuple × tuple
    Devolve três tuplos: subpadrões viáveis (máximo l espaços livres), casas de início, e direções ('H' ou 'V').
    """
    if not (eh_tabuleiro(t) and isinstance(l, int) and l >= 0):
        raise ValueError("gera_todos_padroes: argumento inválido")
    
    pat = []
    cas = []
    dire = []
    
    # Processa linhas horizontais
    for row in range(1, 16):
        p, c = obtem_subpadroes(t, cria_casa(row, 1), cria_casa(row, 15), l)
        pat.extend(p)
        cas.extend(c)
        dire.extend(['H'] * len(p))
    
    # Processa colunas verticais
    for col in range(1, 16):
        p, c = obtem_subpadroes(t, cria_casa(1, col), cria_casa(15, col), l)
        pat.extend(p)
        cas.extend(c)
        dire.extend(['V'] * len(p))
    
    return tuple(pat), tuple(cas), tuple(dire)

####################################################################################
#########################################2.2########################################
####################################################################################

def baralha_saco(seed):
    """
    # - baralha_saco: int → list
   - Descrição: Recebe um inteiro positivo seed como semente para inicializar um gerador de números aleatórios baseado no algoritmo XOR shift,
     utilizado para garantir a reprodutibilidade do baralhamento. A função devolve uma lista de strings contendo as letras do alfabeto português 
     maiúsculo (A, B, C, Ç, D, E, F, G, H, I, J, L, M, N, O, P, Q, R, S, T, U, V, X, Z) com suas respectivas ocorrências definidas pelas regras do 
     Scrabble (ex.: 14 'A', 3 'B', 2 'Ç', etc.), totalizando 100 letras. O processo de baralhamento utiliza o algoritmo de Fisher-Yates adaptado com
       o gerador pseudoaleatório, rearranjando os elementos da lista internamente de forma aleatória. Não modifica argumentos externos, criando e 
       retornando uma nova lista baralhada a cada chamada, sendo essencial para inicializar o saco de letras do jogo de forma imprevisível e justa.

    """
    letras = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z']
    ocorrencias = [14, 3, 4, 2, 5, 11, 2, 2, 2, 10, 2, 5, 6, 4, 10, 4, 1, 6, 8, 5, 7, 2, 1, 1]
    
    saco = []
    for letra, occ in zip(letras, ocorrencias):
        saco.extend([letra] * occ)
    
    def gera_numero_aleatorio(estado):
        s = estado
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= (s >> 17) & 0xFFFFFFFF
        s ^= (s << 5) & 0xFFFFFFFF
        return s
    
    estado = seed
    n = len(saco)
    for i in range(n - 1, 0, -1):
        rand = gera_numero_aleatorio(estado)
        estado = rand
        j = rand % (i + 1)
        saco[j], saco[i] = saco[i], saco[j]
    
    return saco

def jogada_humano(tab, jog, vocab, pilha):
    """
     - jogada_humano: tabuleiro × jogador × vocabulário × list → bool
  - Descrição: Recebe um tabuleiro, um jogador humano, um vocabulário e uma lista representando o saco de letras (pilha).
    Processa o turno completo do jogador humano, solicitando input do utilizador para uma das ações: passar ('P'), trocar
    letras ('T <seq_letras>') ou jogar uma palavra ('J <linha> <coluna> <dir> <palavra>'). Devolve True se o jogador realizou
    uma jogada válida ou trocou letras, False se passou. Modifica destrutivamente o tabuleiro, o jogador e a pilha conforme a 
    ação executada, respeitando as regras (ex.: primeira jogada deve cobrir a casa central (8,8), jogadas posteriores requerem
    padrões viáveis e palavras no vocabulário).

    """
    if not (eh_tabuleiro(tab) and eh_humano(jog) and isinstance(pilha, list)):
        raise ValueError("jogada_humano: argumentos inválidos")

    nome = jogador_identidade(jog)
    letras_jog = jogador_letras(jog)
    primeira_jogada = eh_tabuleiro_vazio(tab)

    while True:
        jogada = input(f"Jogada {nome}: ").strip()
        
        if jogada == 'P':
            return False
        
        if jogada.startswith('T '):
            partes = jogada.split()[1:]
            if not partes:
                continue
            letras_to_trade = []
            valid = True
            for l in partes:
                if not (isinstance(l, str) and len(l) == 1 and l.isalpha()):
                    valid = False
                    break
                letras_to_trade.append(l.upper())
            if not valid:
                continue
            if len(letras_to_trade) > len(pilha):
                continue
            cnt_trade = {}
            for l in letras_to_trade:
                cnt_trade[l] = cnt_trade.get(l, 0) + 1
            cnt_hand = {}
            for l in jogador_letras(jog):
                cnt_hand[l] = cnt_hand.get(l, 0) + 1
            if any(cnt_trade.get(l, 0) > cnt_hand.get(l, 0) for l in cnt_trade):
                continue
            for l in letras_to_trade:
                usa_letra(jog, l)
            for _ in range(len(letras_to_trade)):
                if pilha:
                    recebe_letra(jog, pilha.pop())
            return True
        
        if jogada.startswith('J '):
            partes = jogada.split()
            if len(partes) != 5:
                continue
            try:
                lin = int(partes[1])
                col = int(partes[2])
                casa = cria_casa(lin, col)
                direcao = partes[3].upper()
                palavra = partes[4].upper()
            except (ValueError, TypeError):
                continue
            
            if direcao not in ('H', 'V') or not all(c in letras for c in palavra):
                continue
            
            tam = len(palavra)
            if direcao == 'H' and (col + tam - 1 > 15):
                continue
            if direcao == 'V' and (lin + tam - 1 > 15):
                continue
            
            fim = incrementa_casa(casa, direcao, tam - 1)
            padrao = obtem_padrao(tab, casa, fim)
            
            comp = len(palavra)
            if comp not in vocab or palavra[0] not in vocab[comp] or palavra not in vocab[comp][palavra[0]]:
                continue
            
            if not testa_palavra_padrao(vocab, palavra, padrao, letras_jog):
                continue
            
            needed = []
            for i, c in enumerate(padrao):
                if c == '.':
                    needed.append(palavra[i])
            cnt_needed = {}
            for l in needed:
                cnt_needed[l] = cnt_needed.get(l, 0) + 1
            cnt_hand = {}
            for l in letras_jog:
                cnt_hand[l] = cnt_hand.get(l, 0) + 1
            if any(cnt_needed.get(l, 0) > cnt_hand.get(l, 0) for l in cnt_needed):
                continue
            
            if primeira_jogada:
                cobre_centro = False
                if direcao == 'H':
                    if lin == 8 and col <= 8 <= col + tam - 1:
                        cobre_centro = True
                else:
                    if col == 8 and lin <= 8 <= lin + tam - 1:
                        cobre_centro = True
                if not cobre_centro:
                    continue
            else:
                if all(c == '.' for c in padrao):
                    continue
            
            insere_palavra(tab, casa, direcao, palavra)
            pontos = obtem_pontos(vocab, palavra)
            soma_pontos(jog, pontos)
            for letra in needed:
                usa_letra(jog, letra)
            for _ in range(len(needed)):
                if pilha:
                    recebe_letra(jog, pilha.pop())
            return True
        
def ordena_letras(letras):
    """
    Ordena as letras em ordem lexicogrica das letras do português.
    """
    return sorted(letras, key=lambda x: (ord(x.replace('Ç', 'C')), 1 if x == 'Ç' else 0))

def jogada_agente(tab, jog, vocab, saco):
    """
     - jogada_agente: tabuleiro × jogador × vocabulário × list → bool
   - Descrição: Recebe um tabuleiro, um jogador agente, um vocabulário e uma lista representando o saco de letras. 
   Processa o turno do agente, escolhendo a melhor jogada possível com base no nível ('FACIL', 'MEDIO' ou 'DIFICIL'), 
   que determina a amostragem de padrões. Devolve True se o agente jogou uma palavra ou trocou letras, False se passou (especialmente na primeira jogada). 
   Modifica destrutivamente o tabuleiro, o jogador e o saco conforme a ação executada.

    """
    primeira_jogada = tab[7][7] == '.'  # Verifica se esta é a primeira jogada do jogo

    todos_padroes_gerados = gera_todos_padroes(tab, len(jogador_letras(jog)))
    amostra_padroes = []
    lista_resultados = []
    lista_posicoes = []
    lista_orientacoes = []
    melhor_opcao = ('', 0, (0, 0), '')  # Inicializa com valores default
    mensagem_turno = "Jogada " + jog['identidade']

    if jog['identidade'] == 'FACIL' and eh_agente(jog):
        amostra_padroes = (todos_padroes_gerados[0][::100], todos_padroes_gerados[1][::100], todos_padroes_gerados[2][::100])
    elif jog['identidade'] == 'MEDIO' and eh_agente(jog):
        amostra_padroes = (todos_padroes_gerados[0][::50], todos_padroes_gerados[1][::50], todos_padroes_gerados[2][::50])
    elif jog['identidade'] == 'DIFICIL' and eh_agente(jog):
        amostra_padroes = (todos_padroes_gerados[0][::10], todos_padroes_gerados[1][::10], todos_padroes_gerados[2][::10]) #0: subpadrões, 1: casa de inicio, 2: direção

    for idx, padrao_atual in enumerate(amostra_padroes[0]):
        resultado = procura_palavra_padrao(vocab, padrao_atual, jog['letras'], 0)
        lista_resultados.append(resultado)
        lista_posicoes.append(amostra_padroes[1][idx])
        lista_orientacoes.append(amostra_padroes[2][idx])

    for idx_resultado in range(len(lista_resultados)):
        if lista_resultados[idx_resultado][1] > melhor_opcao[1] or (lista_resultados[idx_resultado][1] == melhor_opcao[1] and lista_resultados[idx_resultado][0] < melhor_opcao[0]):
            melhor_opcao = (lista_resultados[idx_resultado][0], lista_resultados[idx_resultado][1], lista_posicoes[idx_resultado], lista_orientacoes[idx_resultado])

    if primeira_jogada:
        mensagem_turno += ": P"
        print(mensagem_turno)
        return False

    if melhor_opcao[1] > 0:  # Faz uma jogada
        posicao_inicio = melhor_opcao[2]
        orientacao = melhor_opcao[3]
        palavra_escolhida = melhor_opcao[0]
        posicao_fim = incrementa_casa(posicao_inicio, orientacao, len(palavra_escolhida) - 1)
        padrao_atual = obtem_padrao(tab, posicao_inicio, posicao_fim)
        letras_necessarias = [palavra_escolhida[i] for i in range(len(padrao_atual)) if padrao_atual[i] == '.']
        insere_palavra(tab, posicao_inicio, orientacao, palavra_escolhida)
        soma_pontos(jog, melhor_opcao[1])
        for letra in letras_necessarias:
            usa_letra(jog, letra)
        distribui_letras(jog, saco, len(letras_necessarias))
        mensagem_turno += ": J " + str(obtem_lin(posicao_inicio)) + " " + str(obtem_col(posicao_inicio)) + " " + orientacao + " " + palavra_escolhida
        print(mensagem_turno)
        return True
    else:  # Troca letras
        contador_letras = 0
        letras_acumuladas = ""
        if len(saco) >= 7:
            mensagem_turno += ": T"
            letras_atuais = jog['letras']
            letras_unicas = sorted(set(letras_atuais))
            for letra in letras_unicas:
                qtd_letra = letras_atuais.count(letra)
                letras_acumuladas += letra * qtd_letra
                for _ in range(qtd_letra):
                    usa_letra(jog, letra)
                    contador_letras += 1
            letras_acumuladas = ''.join(ordena_letras(letras_acumuladas))
            
            saco.extend(list(letras_acumuladas))

            for letra in letras_acumuladas:
                mensagem_turno += " " + letra
            distribui_letras(jog, saco, contador_letras)
            print(mensagem_turno)
            return True
        # Passa o turno
        mensagem_turno += ": P"
        print(mensagem_turno)
        return False

def scrabble2(jogadores, arquivo_vocab, semente):
    """
    # - scrabble2: tuple × str × int → tuple
   - Descrição: Recebe um tuplo de strings representando os nomes ou níveis dos jogadores (2 a 4, com '@' para agentes), 
 uma string nome_fich para o ficheiro de vocabulário e um inteiro seed para inicializar o baralhamento. 
 Executa o jogo Scrabble2, gerenciando turnos de jogadores humanos e agentes, distribuindo letras iniciais, 
 atualizando o tabuleiro e pontuações. Devolve um tuplo com as pontuações finais dos jogadores na ordem de entrada. 
 Modifica destrutivamente os dados internos (tabuleiro, jogadores, saco) durante a execução, terminando quando todos passam 
 consecutivamente ou um jogador fica sem letras e o saco vazio.2,5s
    """
    if not (isinstance(jogadores, tuple) and 2 <= len(jogadores) <= 4):
        raise ValueError("scrabble2: argumentos inválidos")
    
    for p in jogadores:
        
        if p.startswith('@'):
            dificuldade = p[1:].upper()
            if dificuldade not in {'FACIL', 'MEDIO', 'DIFICIL'}:
                raise ValueError("scrabble2: argumentos inválidos")
        else:
            if not all(c.isspace() or c.isalpha() or c in "-'." for c in p):
                raise ValueError("scrabble2: argumentos inválidos")
            
        if not (isinstance(p, str) and p):
            raise ValueError("scrabble2: argumentos inválidos")
    
    if not (isinstance(semente, int) and semente > 0):
        raise ValueError("scrabble2: argumentos inválidos")
    
    if not (isinstance(arquivo_vocab, str) and arquivo_vocab):
        raise ValueError("scrabble2: argumentos inválidos")
    
    dicionario = ficheiro_para_vocabulario(arquivo_vocab)
    
    lista_jogadores = []

    for p in jogadores:
        if p.startswith('@'):
            dificuldade = p[1:].upper()
            lista_jogadores.append(cria_agente(dificuldade))
        else:
            lista_jogadores.append(cria_humano(p))
    
    bolsa_letras = baralha_saco(semente)
    
    grelha = cria_tabuleiro()
    
    for jogador in lista_jogadores:
        distribui_letras(jogador, bolsa_letras, 7)
    
    print("Bem-vindo ao SCRABBLE2.")
    
    indice_turno = 0
    passes_seguidos = 0
    
    while True:
        print(tabuleiro_para_str(grelha))
        
        for jogador in lista_jogadores:
            print(jogador_para_str(jogador))
        
        jog_atual = lista_jogadores[indice_turno]
        id_jog = jogador_identidade(jog_atual)
        
        if eh_humano(jog_atual):
            jogada_feita = jogada_humano(grelha, jog_atual, dicionario, bolsa_letras)
        else:
            jogada_feita = jogada_agente(grelha, jog_atual, dicionario, bolsa_letras)

        if jogada_feita:
            passes_seguidos = 0
        else:
            passes_seguidos += 1
        
        if passes_seguidos == len(lista_jogadores):
            break
        
        if len(jogador_letras(jog_atual)) == 0 and len(bolsa_letras) == 0:
            break
        
        indice_turno = (indice_turno + 1) % len(lista_jogadores)
    
    return tuple(jogador_pontos(jogador) for jogador in lista_jogadores)