#Lendo arquivo CSV
df_reclamacoes = pd.read_csv("dadosgovbr---2014.csv", sep=';', encoding='latin-1')

#----------------------------------------------------------------------------------------------------------------------Questao1--------------------------------------#
#Agrupando a coluna UF e somando os valores da coluna total.
print("Resposta 1: Numero de reclamacoes por Estado:\n")
df_reclamacoes_porEstado = df_reclamacoes.groupby(["UF"])["Total"].sum().reset_index()
print(df_reclamacoes_porEstado)
print("------------------------------------------------------------------------\n")
print("Histograma de reclamacoes por Estado:\n")
plt.hist(df_reclamacoes.UF, bins = 50)
plt.title("Distribuicao da variavel UF")
plt.show()
print("------------------------------------------------------------------------\n")

#----------------------------------------------------------------------------------------------------------------------Questao2--------------------------------------#
#Agrupando a coluna Sexo e somando os valores da coluna Total
print("Resposta 2:Numero de reclamacoes por Sexo:\n")
df_reclamacoes_porSexo = df_reclamacoes.groupby(["Sexo"])["Total"].sum().reset_index()
print(df_reclamacoes_porSexo)
print("------------------------------------------------------------------------\n")
print("Histograma de reclamacoes por Sexo:\n")
plt.hist(df_reclamacoes.Sexo, bins = 3)
plt.title("Distribuicao da variavel Sexo")
plt.show()
print("------------------------------------------------------------------------\n")

#----------------------------------------------------------------------------------------------------------------------Questao3--------------------------------------#
print("------------------------------------------------------------------------\n")
#Filtrando somente as colunas necessarias para essa analise
df_reclamacoes_correlacao = df_reclamacoes[["Nota do Consumidor","Tempo Resposta"]]
#Verificando quantidade de valores nulos
print(f"Quantidade de valores nulos por coluna:\n{df_reclamacoes_correlacao.isnull().sum()}\n")
print(f"Percentual geral de valores nulos:\n{round((df_reclamacoes_correlacao.isnull().sum().sum()/df_reclamacoes_correlacao.shape[0])*100,2)}\n")
#Desconsiderando os valores nulos
df_reclamacoes_correlacao = df_reclamacoes_correlacao.dropna()

print("------------------------------------------------------------------------\n")
#Sao duas variaveis quantitativas discretas verificar as medidas de centralidade
print("Medidas de Centralidade: \n")
print(df_reclamacoes_correlacao.describe())
#A media e a mediana estao bem proximas nas duas variaveis e um conjunto bem comportado
df_reclamacoes_correlacao.rename(columns= {"Nota do Consumidor":"Nota_Consumidor","Tempo Resposta":"Tempo_Resposta"}, inplace = True)

print("------------------------------------------------------------------------\n")
#Calculando o percentil das variaveis Tempo resposta e Nota do consumidor no valor de 90%
print(f"90% do tempo resposta das reclamacoes e igual/abaixo de {int(np.percentile(df_reclamacoes_correlacao.Tempo_Resposta,90))} dias\n")
print(f"90% da nota do consumidor e igual/abaixo da nota {int(np.percentile(df_reclamacoes_correlacao.Nota_Consumidor,90))}\n")

print("------------------------------------------------------------------------\n")
#Visualizacao do tempo resposta do consumidor pelo boxplot
print("Boxplot do Tempo Resposta do Consumidor:\n")
plt.boxplot(df_reclamacoes_correlacao.Tempo_Resposta)
plt.show()

print("------------------------------------------------------------------------\n")
print("Histograma da Nota do Consumidor:\n")
plt.hist(df_reclamacoes_correlacao.Nota_Consumidor, bins = 10)
plt.title("Distribuicao da Nota do Consumidor")
plt.show()

print("------------------------------------------------------------------------\n")
#Grafico de dispersao Nota do Consumidor X Tempo Resposta
plt.figure(figsize=[12,5])
plt.subplots_adjust(wspace=0.2)
plt.subplot(1,2,1)
plt.title("Nota_Consumidor x Tempo_Resposta")
plt.scatter(df_reclamacoes_correlacao.Tempo_Resposta, df_reclamacoes_correlacao.Nota_Consumidor)
plt.xlabel("Tempo_Resposta")
plt.ylabel("Nota_Consumidor")
plt.ylim([0.5,5.5])
plt.show()

print("------------------------------------------------------------------------\n")
print("Frequencia absoluta e relativa da variavel Nota_Consumidor\n")
df_reclamacoes_freq_notaconsu = pd.DataFrame(df_reclamacoes_correlacao.Nota_Consumidor.value_counts())
df_reclamacoes_freq_notaconsu.rename(columns={"Nota_Consumidor":"FA_NotaConsumidor"}, inplace = True)
df_reclamacoes_freq_notaconsu = df_reclamacoes_freq_notaconsu.sort_index(ascending=True)
df_reclamacoes_freq_notaconsu["FR_NotaConsumidor"] = round(df_reclamacoes_freq_notaconsu["FA_NotaConsumidor"]/df_reclamacoes_correlacao.shape[0],5)
print(df_reclamacoes_freq_notaconsu)

print("------------------------------------------------------------------------\n")
print("Frequencia absoluta e relativa da variavel Tempo_Resposta\n")
df_reclamacoes_freq_temporesp = pd.DataFrame(df_reclamacoes_correlacao.Tempo_Resposta.value_counts())
df_reclamacoes_freq_temporesp.rename(columns = {"Tempo_Resposta":"FA_TempoResposta"}, inplace = True)
df_reclamacoes_freq_temporesp = df_reclamacoes_freq_temporesp.sort_index(ascending=True)
df_reclamacoes_freq_temporesp["FR_TempoResposta"] = round(df_reclamacoes_freq_temporesp["FA_TempoResposta"]/df_reclamacoes_correlacao.shape[0],5)
print(df_reclamacoes_freq_temporesp)

print("------------------------------------------------------------------------\n")
#Correlacao da Variavel Nota do consumidor com as outras variaveis
correlacao_notaConsumidor = float(df_reclamacoes_correlacao.corr()[["Nota_Consumidor"]].iloc[1].values)
print(f"A correlacao da variavel Nota do Consumidor com a variavel Tempo Resposta e de:{round(correlacao_notaConsumidor,4)}, indicando uma correlacao fraca\n")

print("------------------------------------------------------------------------\n")
df_reclamacoes_correlacao.boxplot("Nota_Consumidor", by = ["Tempo_Resposta"], figsize=[15,5])
plt.ylabel("Nota_Consumidor")
plt.title("BoxPlot da variavel Nota Consumidor x Tempo Resposta")
plt.show()

#----------------------------------------------------------------------------------------------------------------------Questao4--------------------------------------#
#Filtrando apenas as colunas a serem utilizadas
df_reclamacoes_registradas = df_reclamacoes[["Respondida","Total"]]
#Verificando quantidade de valores nulos
#print(f"Quantidade de valores nulos na coluna Respondida:\n{df_reclamacoes_registradas.isnull().sum()}\n")

print("------------------------------------------------------------------------\n")
#Agrupando pela coluna Respondido
df_reclamacoes_registradas = df_reclamacoes_registradas.groupby(["Respondida"])["Total"].sum().reset_index()
print(f"Quantidade de reclamacoes registradas respondidas e nao respondidas:\n{df_reclamacoes_registradas}\n")

#Verificando a proporcao do numero de reclamacoes registradas e nao respondidas
print("------------------------------------------------------------------------\n")
proporcao_registradas_naoRespondidas = round(df_reclamacoes_correlacao.shape[0]/df_reclamacoes_registradas.Total[0],2)
print(f"Resposta 4: Proporcao da quantidade de reclamacoes registradas e nao respondidas:\n{proporcao_registradas_naoRespondidas}%\n")
print("------------------------------------------------------------------------\n")
print("Histograma da quantidade de reclamacoes respondidas e nao respondidas:\n")
plt.hist(df_reclamacoes.Respondida, bins = 3)
plt.title("Distribuicao das Reclamacoes respondidas e nao respondidas")
plt.show()

#----------------------------------------------------------------------------------------------------------------------Questao5--------------------------------------#
#Qual a probabilidade da nota ser maior ou igual que 4 em cada um dos dias de tempo de resposta?

#Funcao para calculo da probabilidade de acordo com o Tempo Resposta
def Prob_TempoRespCurto(x):
    prob_tempoResposta = df_reclamacoes_correlacao[(df_reclamacoes_correlacao.Nota_Consumidor>=4.0) & (df_reclamacoes_correlacao.Tempo_Resposta == x)].shape[0]/df_reclamacoes_correlacao[df_reclamacoes_correlacao.Tempo_Resposta==x].shape[0]
    return prob_tempoResposta

#Agrupando a coluna tempo resposta
df_reclamacoes_correlacao_agrup = df_reclamacoes[["Tempo Resposta"]]
#Tirando os valores duplicados
df_reclamacoes_correlacao_agrup = df_reclamacoes_correlacao_agrup.drop_duplicates().dropna()
#Transformando a coluna em uma lista
lista_tempoResposta = df_reclamacoes_correlacao_agrup ["Tempo Resposta"].tolist()
#Colocando a lista em ordem crescente
lista_tempoResposta.sort(reverse=False)

print("------------------------------------------------------------------------\n")
#laco for para cada valor da lista
print(f"Se a reclamacao for respondida em:\n")
for i in lista_tempoResposta:
    prob_tempoResposta = Prob_TempoRespCurto(i)
    print(f"{int(i)} dia(s) a probabilidade de ter uma nota IGUAL ou MAIOR que 4 e de {round(prob_tempoResposta*100,2)}%\n")

#----------------------------------------------------------------------------------------------------------------------Questao6--------------------------------------#
print("------------------------------------------------------------------------\n")
#Qual a media das notas das reclamacoes por grupo de problema?
#Considerando apenas as colunas a serem utilizadas
df_reclamacoes_problema = df_reclamacoes[["Grupo Problema","Nota do Consumidor","Total"]]
#Tirando os valores nulos
df_reclamacoes_problema = df_reclamacoes_problema.dropna()
#Calculando a media das notas das reclamacoes atraves do agrupamento do grupo problema
df_reclamacoes_problema_agrupado_detal = df_reclamacoes_problema.groupby("Grupo Problema").agg({"Nota do Consumidor":"mean","Total":"sum"}).reset_index().rename(columns ={"Nota do Consumidor":"Media_Nota_Consumidor","Total":"Numero_Reclamacoes"})
#Deixando a coluna com apenas 2 valores apos a virgula
df_reclamacoes_problema_agrupado_detal.Media_Nota_Consumidor = round(df_reclamacoes_problema_agrupado_detal.Media_Nota_Consumidor,2)
print(f"Distribuicao das reclamacoes por Grupo Problema com a media da Nota do Consumidor\n{df_reclamacoes_problema_agrupado_detal}")


#Grafico para mostrar essa distribuicao
print("------------------------------------------------------------------------\n")
df_reclamacoes_problema_agrupado_detal.boxplot("Media_Nota_Consumidor", by = ["Grupo Problema"], figsize=[15,5])
plt.ylabel("Media_Nota_Consumidor")
plt.title("Media da Nota do Consumidor por Grupo Problema")
plt.show()
