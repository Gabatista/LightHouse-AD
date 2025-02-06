import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)

#leitura dos arquivos csv
df_agencias = pd.read_csv('agencias.csv')
df_clientes = pd.read_csv('clientes.csv')
df_colaborador_agencia = pd.read_csv('colaborador_agencia.csv')
df_colaborador = pd.read_csv('colaboradores.csv')
df_contas = pd.read_csv('contas.csv')
df_propostas_credito = pd.read_csv('propostas_credito.csv')
df_transacoes = pd.read_csv('transacoes.csv')

#clientes
#quantidade de agencias por uf

#estado = df_agencias.groupby('uf').count()
#print(estado)




#agencias
#quantidade de clientes
#print(df_clientes)

#tratando dados para obter o estado via endereço
#df_clientes['uf'] = df_clientes['endereco'].str[-2:]
#print(df_clientes)

#clientes_estado = df_clientes.groupby('uf')['uf'].count().sort_values(ascending=False)
#print(clientes_estado)


#obtendo ano de nascimento
#df_clientes['ano_nascimento'] = df_clientes['data_nascimento'].str[:4]
#ano_nasc_clientes = df_clientes.groupby('ano_nascimento')['ano_nascimento'].count()
#clientes_nascimento.columns = ["index","ano"]
#clientes_nascimento.groupby('data_nascimento')['data_nascimento'].count().sort_values(ascending=False)
#ano = clientes_nascimento.groupby(clientes_nascimento)
#print(ano_nasc_clientes)

#ano_nasc_clientes.to_csv(r'C:\Users\UC396QV\OneDrive - EY\Desktop\Lighthouse\analise de dados\banvic_data\sa.txt')

#obtendo pf ou pj
#tipo_cliente = df_clientes.groupby('tipo_cliente')['tipo_cliente'].count().sort_values(ascending=False)
#print(tipo_cliente)


#colaborador e agencia
colaborador = df_colaborador_agencia.groupby('cod_agencia')['cod_agencia'].count()
#print(colaborador)


#clientes por colaborador
clie_por_colab = df_contas.groupby('cod_colaborador')['num_conta'].count().sort_values(ascending=False)
clie_por_colab.to_csv(r'C:\Users\UC396QV\OneDrive - EY\Desktop\Lighthouse\analise de dados\banvic_data\scliente.txt')

#ano de nascimento e geração do colaborador
df_colaborador['ano_nascimento'] = df_colaborador['data_nascimento'].str[:4]
ano_nasc_colaborador = df_colaborador.groupby('ano_nascimento')['ano_nascimento'].count()

#endereco do colaborador
df_colaborador['uf'] = df_colaborador['endereco'].str[-2:]

#clientes_nascimento.groupby('data_nascimento')['data_nascimento'].count().sort_values(ascending=False)
#ano = clientes_nascimento.groupby(clientes_nascimento)
#print(ano_nasc_colaborador)


#juntando os dataframes

df_colaboradores = df_colaborador_agencia.merge(df_colaborador[['cod_colaborador','ano_nascimento','uf']],on='cod_colaborador',how='left')
colaborador_uf = df_colaboradores.groupby('uf')['uf'].count().sort_values(ascending=False)
print(colaborador_uf)