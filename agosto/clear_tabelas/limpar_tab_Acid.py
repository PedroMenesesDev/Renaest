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
	DROP TABLE [dbo].[Dados_Acidente]

	CREATE TABLE [dbo].[Dados_Acidente](
		[Tp_Atualizacao] [varchar](1) NULL,
		[Identificacao_Acidente] [varchar](15) NULL,
		[Data_Acidente] [varchar](8) NULL,
		[Hora_acidente] [varchar](6) NULL,
		[CEP_Ocorrencia_Acidente] [varchar](8) NULL,
		[Endereco_Ocorrencia_Acidente] [varchar](40) NULL,
		[Numero_Ocorrencia_Acidente] [varchar](5) NULL,
		[Bairro_Ocorrencia_Acidente] [varchar](30) NULL,
		[Municipio_Ocorencia] [varchar](5) NULL,
		[UF_Ocorrencia_Acidente] [varchar](2) NULL,
		[Quadra_Trecho_Referencia] [varchar](30) NULL,
		[KM_Via_Acidente] [varchar](4) NULL,
		[Tp_Acidente] [varchar](2) NULL,
		[Condicao_iluminacao] [varchar](2) NULL,
		[Condicoes_Meteorologicas] [varchar](2) NULL,
		[Nome_Comunicante] [varchar](60) NULL,
		[Tp_Impacto] [varchar](2) NULL,
		[Dia_Semana] [varchar](1) NULL,
		[Fase_Dia] [varchar](1) NULL,
		[Sentido_Via] [varchar](1) NULL,
		[Causa_Principal] [varchar](2) NULL,
		[Causas_Concorrentes] [varchar](20) NULL,
		[Dano_Meio_Ambiente] [varchar](1) NULL,
		[Dano_Patrimonio] [varchar](1) NULL,
		[DataHora_Abertura_Comunicacao] [varchar](14) NULL,
		[DataHora_Acionamento_Equipe] [varchar](14) NULL,
		[DataHora_Finalizacao_Atendimento] [varchar](14) NULL,
		[DataHora_Fim_Preenchimento_Ocorrencia] [varchar](14) NULL,
		[DataHora_Inicio_Atendimento] [varchar](14) NULL,
		[DataHora_Inicio_Preenchimento_Ocorrencia] [varchar](14) NULL,
		[Indicador_Processo] [varchar](1) NULL,
		[Status_Registro] [varchar](1) NULL,
		[Latitude] [varchar](11) NULL,
		[Longitude] [varchar](11) NULL,
		[Numero_Pedestres_envolvidos] [varchar](3) NULL,
		[Metodo_Coleta] [varchar](1) NULL
	) ON [PRIMARY]"""

cursor.execute(comando)
cursor.commit()
print('Tabela ACIDENTE limpa!')
