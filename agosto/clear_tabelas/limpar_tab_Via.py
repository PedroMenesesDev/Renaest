import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DTRC02;"
    "Database=renaest;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

comando = """ 
DROP TABLE [dbo].[Dados_Via]

CREATE TABLE [dbo].[Dados_Via](
	[Tp_Atualizacao] [varchar](1) NULL,
	[Indentificacao_Acidente] [varchar](15) NULL,
	[Acostamento] [varchar](1) NULL,
	[Canteiro_Central] [varchar](1) NULL,
	[Condicao_Via] [varchar](2) NULL,
	[Cruzamento] [varchar](2) NULL,
	[Curva_Via] [varchar](2) NULL,
	[Tp_Pavimento] [varchar](2) NULL,
	[Classe_Funcional_Via] [varchar](2) NULL,
	[Controle_Trafego_Cruzamento] [varchar](2) NULL,
	[Limite_Velocidade] [varchar](3) NULL,
	[Obstaculo_Via] [varchar](1) NULL,
	[Superficie_Trecho_Viario] [varchar](2) NULL,
	[Urbanizacao] [varchar](1) NULL,
	[Jurisprudencia_via] [varchar](2) NULL,
	[Tp_Pista] [varchar](2) NULL,
	[Trava_Seguranca_Metalica] [varchar](1) NULL
) 	ON [PRIMARY]"""

cursor.execute(comando)
cursor.commit()
print('Tabela VIA limpa!')
