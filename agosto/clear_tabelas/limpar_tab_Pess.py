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
DROP TABLE [dbo].[Dados_Pessoa]

CREATE TABLE [dbo].[Dados_Pessoa](
	[Tp_Atualizacao] [varchar](1) NULL,
	[Identificacao_Acidente] [varchar](15) NULL,
	[CPF_Envolvido] [varchar](11) NULL,
	[Numero_Registro_CNH] [varchar](11) NULL,
	[Dt_Nasc_Envolvido] [varchar](8) NULL,
	[Nome_Envolvido] [varchar](60) NULL,
	[Nome_Mae_Envolvido] [varchar](60) NULL,
	[Tp_Genero_Envolvido] [varchar](1) NULL,
	[Dt_Obito_Envolvido] [varchar](8) NULL,
	[Tp_User_Via_Envolvido] [varchar](2) NULL,
	[Tp_Vitima_Envolvido] [varchar](1) NULL,
	[CEP_Endereco_Envolvido] [varchar](8) NULL,
	[Endereco_Envolvido] [varchar](40) NULL,
	[Numero_Endereco_Envolvido] [varchar](5) NULL,
	[Bairro_Endereco_Envolvido] [varchar](30) NULL,
	[Municipio_Endereco_Envolvido] [varchar](5) NULL,
	[UF_Endereco_Envolvido] [varchar](2) NULL,
	[Equip_Seg_Envolvido] [varchar](2) NULL,
	[Grav_Lesao_Envolvido] [varchar](2) NULL,
	[Suspeito_uso_Alcool_Envolvido] [varchar](1) NULL,
	[Teste_Alcool_Envolvido] [varchar](1) NULL,
	[Resultado_Alcool_Envolvido] [varchar](1) NULL,
	[Suspeito_Uso_Drogas_Envolvido] [varchar](1) NULL,
	[Teste_Drogas_Envolvido] [varchar](1) NULL,
	[Resultado_Teste_Drogas] [varchar](1) NULL,
	[Posicao_Assento_Envolvido] [varchar](2) NULL,
	[Manobra_Pedestre_Envolvido] [varchar](2) NULL,
	[Seq_Pessoa_Envolvido] [varchar](3) NULL,
	[Encaminhamento_Envolvido] [varchar](2) NULL,
	[Receptor_Vitima_Envolvido] [varchar](60) NULL,
	[Indi_Pessoa_estrangeira] [varchar](1) NULL,
	[Indi_Pessoa_com_Deficiencia] [varchar](1) NULL
) 	ON [PRIMARY]"""

cursor.execute(comando)
cursor.commit()
print('Tabela PESSOAS limpa!')
