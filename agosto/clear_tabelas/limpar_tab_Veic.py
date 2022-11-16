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
DROP TABLE [dbo].[Dados_Veiculo]

CREATE TABLE [dbo].[Dados_Veiculo](
	[Tp_Atualizacao] [varchar](1) NULL,
	[Identificacao_Acidente] [varchar](15) NULL,
	[Placa_veiculo] [varchar](7) NULL,
	[Renavam_veiculo] [varchar](11) NULL,
	[Chassi] [varchar](21) NULL,
	[Tp_Veiculo] [varchar](2) NULL,
	[Manobra_Veicular] [varchar](2) NULL,
	[Encaminhamento_Veiculo] [varchar](1) NULL,
	[Motivo_Encaminhamento_Veiculo] [varchar](1) NULL,
	[Estrutura] [varchar](1) NULL,
	[Monta] [varchar](1) NULL,
	[Receptor_Veiculo_orgao] [varchar](50) NULL,
	[Sequencial_Veiculo_acidente] [varchar](2) NULL,
	[Numero_Ocupantes_Veiculo] [varchar](3) NULL,
	[Indicador_veiculo_Estrangeiro] [varchar](1) NULL
) ON [PRIMARY]"""

cursor.execute(comando)
cursor.commit()
print('Tabela VEICULOS limpa!')
