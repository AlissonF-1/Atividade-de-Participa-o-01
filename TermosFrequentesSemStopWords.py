from collections import defaultdict

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

freq = defaultdict(int)
for palavra in palavras_filtradas:
    freq[palavra] += 1

l = [(v, k) for k, v in freq.items()]
l.sort(reverse=True)

n = int(input("Quantos termos? "))

print("\nPalavras mais frequentes (sem stopwords):")
for i in range(min(n, len(l))):
    print(l[i])
