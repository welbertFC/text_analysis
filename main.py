from Analytical_characters import AnalyticalCharacteres
from Analytical_word import AnalyticalWord
from Sum import Sum
from collections import Counter

text = '''
O software tem como objetivo oferecer uma ferramenta simples e prática para a elaboração de um plano de negócios.
Criar uma empresa é um desafio e o plano de negócios, enquanto instrumento de planejamento, é adotado em todo o
mundo, por diversas instituições e por empresas dos mais diversos porte e setores.
Um plano de negócios tem como proposta fazer com que o empreendedor seja capaz de estimar se, a partir da sua
visão de futuro, experiência e conhecimento de mercado, seu projeto é viável ou não. Apesar de não eliminar totalmente
os riscos, evita que erros sejam cometidos pela falta de análise.
O sistema foi preparado para orientá-lo no preenchimento de cada seção do plano a partir das informações coletadas
por você. Para ajudá-lo, a ferramenta explica as etapas do plano, apresentando dicas, alertas e recomendações. Os
exemplos disponibilizados são fictícios, de natureza pedagógica e trazem informações e valores meramente ilustrativos.
Tenho ciência e concordo com os termos acima.
FABIO JULIO DE MOURA
Informações Gerais
Um plano de negócios não garante por si só o sucesso de uma empresa. Fatores externos também influenciam o
negócio, portanto monitore ameaças e oportunidades.
Fatores internos também determinam a existência e o crescimento de uma empresa. Esses fatores estão sob controle
do empreendedor e são relacionados à implantação de controles e à uma gestão eficiente.
Informação é a matéria-prima para qualquer ação de planejamento e quanto mais precisa for, maior será a qualidade
do plano de negócios. Portanto, leia revistas especializadas, consulte associações e entidades do seu segmento,
participe de feiras e cursos, faça pesquisas na Internet, converse com outros empresários, clientes, fornecedores e
especialistas (consultores, contabilistas, advogados, etc.).
O plano de negócio deve ser revisado periodicamente, pois é flexível e está sujeito a ajustes em função das
mudanças no mercado ou do ambiente interno da empresa.
Apesar do plano ser um instrumento de gestão importante, há outras ferramentas que devem ser utilizadas por você
na administração da empresa.
O plano de negócios pode ser solicitado por uma instituição financeira ou por um investidor para a captação de
recursos. Entretanto, este plano não assegura a obtenção dos recursos em si, pois cada instituição tem processos
próprios, requisitos e exigências.
Um plano de negócio pode ser utilizado para obter sócios e investidores, estabelecer parcerias com fornecedores e
clientes ou mesmo buscar recursos. Porém, o usuário mais importante do plano de negócios é o próprio
'''

# aparicoes = Counter(text.lower())
# total_de_caracteres = sum(aparicoes.values())
# proporcoes = [(letra, frquencia / total_de_caracteres) for letra, frquencia in aparicoes.items()]
# proporcoes = Counter(dict(proporcoes))
# mais_comuns = proporcoes.most_common(15)
# for caractere, proporcao in mais_comuns:
#     print(caractere)
#     print('{:.2f}%'.format(proporcao * 100))


#
# for caractere, vezes_que_aparece in vezes_aparece:
#         print(f'caractere: {caractere} == {vezes_que_aparece}')




# obejto_texto = Sum(text)
#
# print(obejto_texto)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
for interação in matriz:
    for elemento in interação:
        print(elemento, end='  ')
    print("\n")



