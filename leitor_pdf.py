from PyPDF2 import PdfReader
import spacy

#Função que extrai o texto do PDF
def extrair_texto_pdf(caminho):
    with open(caminho, "rb") as arquivo_texto:
        reader = PdfReader(arquivo_texto)
        results = []

        for i in range(0,len(reader.pages)):
            pagina_selecionada = reader.pages[i]
            texto_pagina = pagina_selecionada.extract_text()
            results.append(texto_pagina)
        return ' '.join(results)

#Extraindo texto do PDF e transformando em doc nlp
textoCompleto = extrair_texto_pdf(
    r'C:\Users\Alefera\Desktop\Arcondinst.pdf')

#Inicialização do spacy com modelo pt-br
nlp = spacy.load("pt_core_news_sm")

#Carrega o arquivo de texto como doc
doc = nlp(textoCompleto)

#Define as palavras chaves para busca
palavras_chaves = ["condicionado"]

#Vetor que guarda os spans que contém as palavras chaves
encontrados = []

#Faz a busca das palavras chaves no doc
for token in doc:
    if token.text in palavras_chaves:
        span = doc[token.i: token.i + 1].sent
        encontrados.append(span.text)
        print("Palavra chave", token, "encontrada em:", '\n', span.text, '\n')

#Cria o arquivo de texto das partes que contém as palavras encontradas
if encontrados != []:
    with open('encontrados.doc', 'w', encoding='utf-8') as arquivo:
        for span in encontrados:
            arquivo.write(span + '\n')
    print('Arquivo de texto gerado com sucesso!')
else:
    print('Nenhuma palavra chave encontrada!')