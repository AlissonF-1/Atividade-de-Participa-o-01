
stopwords = [
    'a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas', 'de', 'do', 'da', 'dos', 'das',
    'em', 'no', 'na', 'nos', 'nas', 'por', 'com', 'para', 'e', 'ou', 'que', 'se', 'não',
    'mais', 'menos', 'muito', 'pouco', 'já', 'também', 'como', 'mas', 'porque', 'quando'
]

texto = input("Digite seu texto: ")

texto_limpo = ""
for caractere in texto:
    if caractere.isalnum() or caractere.isspace():
        texto_limpo += caractere.lower()
    else:
        texto_limpo += " "

palavras = texto_limpo.split()

palavras_filtradas = []
for palavra in palavras:
    if palavra not in stopwords:
        palavras_filtradas.append(palavra)

print("Palavras sem stopwords:")
print(palavras_filtradas)
