import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Ler arquivo csv
df_titanic = pd.read_csv("titanic.csv")
#df_titanic.head()

#Utilizaremos somente as colunas Survived e Sex
df_titanic_filtrado = df_titanic[['Survived', 'Sex']]
#df_titanic_filtrado.head()

#Verificar a quantidade de dados nulos
print(f"Quantidade de valores nulos:{df_titanic_filtrado.isnull().sum().sum()}\n")

print("------------------------------------------------------------------------\n")
#Verificar os tipos de variaveis
print(f"Tipos de variaveis:\n{df_titanic_filtrado.dtypes}\n")

print("------------------------------------------------------------------------\n")
#Sao duas variaveis qualitativas nominais verificar as medidas de centralidade
qtd_pessoas = df_mc.Survived[0]
print(f"Quantidade de pessoas: {qtd_pessoas}\n")

print("------------------------------------------------------------------------\n")
#Distribuicao geral
print("Frequencia absoluta e relativa da variavel Sex\n")
df_titanic_freq_sex = pd.DataFrame(df_titanic_filtrado.Sex.value_counts())
df_titanic_freq_sex.rename(columns= {"Sex":"Frequencia_Absoluta"}, inplace = True)
df_titanic_freq_sex["Frequencia_Relativa"] = round(df_titanic_freq_sex.Frequencia_Absoluta/qtd_pessoas,2)
print(f"{df_titanic_freq_sex}\n")

print("------------------------------------------------------------------------\n")
print("Frequencia absoluta e relativa da variavel Survived\n")
df_titanic_freq_survived = pd.DataFrame(df_titanic_filtrado.Survived.value_counts())
df_titanic_freq_survived.rename(columns= {"Survived":"Frequencia_Absoluta"}, inplace = True)
df_titanic_freq_survived["Frequencia_Relativa"] = round(df_titanic_freq_survived.Frequencia_Absoluta/qtd_pessoas,2)
print(f"{df_titanic_freq_survived}\n")

#Grafico da sequencia para a variavel Sex
plt.bar(df_titanic_filtrado.Sex.unique(), df_titanic_filtrado.Sex.value_counts(), color = "lightblue")
plt.title("Distribuicao de frequencia para variavel Sex\n", {"fontsize": 12, "fontweight": "bold"})
plt.show()

print("------------------------------------------------------------------------\n")
#Probabilidade de sobreviver se voce e do sexo masculino
prob_h = round(df_titanic_filtrado[(df_titanic_filtrado.Survived==1) & (df_titanic_filtrado.Sex=="male")].shape[0] / df_titanic_filtrado[(df_titanic_filtrado.Sex=="male")].shape[0],2)
print(f"Probabilidade de sobreviver se voce e homem: {prob_h}\n")

#Probabilidade de sobreviver se voce e do sexo feminino
prob_m = round(df_titanic_filtrado[(df_titanic_filtrado.Survived==1) & (df_titanic_filtrado.Sex=="female")].shape[0] /df_titanic_filtrado[(df_titanic_filtrado.Sex=="female")].shape[0],2)
print(f"Probabilidade de sobreviver se voce e mulher: {prob_m}\n")

print("------------------------------------------------------------------------\n")
print("Calculando os valores observados:\n")
#Agrupando os dados por sexo
df_titanic_observado= df_titanic_filtrado.groupby("Sex").apply(lambda x: x.Survived.value_counts()).unstack()
#Renomeando as colunas
df_titanic_observado.rename(columns = {0:"Nao_Sobreviveu",1:"Sobreviveu"}, inplace = True)
#Calculando a coluna Total
df_titanic_observado["Total"] = df_titanic_observado["Nao_Sobreviveu"]+df_titanic_observado["Sobreviveu"]
print(df_titanic_observado)

print("------------------------------------------------------------------------\n")
#Isolando a frequencia relativa
fr_naoSobreviveu = pd.DataFrame(df_titanic_freq_survived["Frequencia_Relativa"]).iloc[0].values
fr_sobreviveu = pd.DataFrame(df_titanic_freq_survived["Frequencia_Relativa"]).iloc[1].values

#Calculando o valor esperado
df_esperado_naoSobreviveu = df_titanic_observado.Total.values * fr_naoSobreviveu
df_esperado_sobreviveu = df_titanic_observado.Total.values * fr_sobreviveu

df_esperado = pd.DataFrame(np.c_[df_esperado_naoSobreviveu,df_esperado_sobreviveu])
df_esperado

#Calculo do chi-quadrado
#Observado menos o esperado
desvios= (df_titanic_observado.iloc[:,:2].values - df_esperado.values)

desvios_ao_quadrado = desvios**2

chi_quadrado = sum(sum(desvios_ao_quadrado/df_esperado.values))
print(f"O qui-quadrado de Pearson e de: {chi_quadrado} indicando uma boa relacao entre as variaveis Survived e Sex")
