import pyodbc
import pandas as pd
from asyncio.windows_events import NULL
import PySimpleGUI as sg

# -------------------------------------------- FUNÇÔES --------------------------------------------------------


def tipoAcostamento(acostamento):
    str_acostamento = str(acostamento).strip().upper()
    if str_acostamento == 'NAN' or str_acostamento == 'NONE' or str_acostamento == 'NAT':
        cod_acostamento = "'0'"

    elif str_acostamento == 'S':
        cod_acostamento = "'1'"

    elif str_acostamento == 'N':
        cod_acostamento = "'2'"

    else:
        cod_acostamento = "'9'"

    return cod_acostamento


def tipoPavimento(pavimento):
    str_pavimentp = str(pavimento).strip().upper()
    if str_pavimentp == 'NAN' or str_pavimentp == 'NONE' or str_pavimentp == 'NAT':
        codig_pavimento = "'00'"

    elif str_pavimentp == 'ASFALTO':
        codig_pavimento = "'01'"

    elif str_pavimentp == 'CASCALHO':
        codig_pavimento = "'02'"

    elif str_pavimentp == 'CONCRETO':
        codig_pavimento = "'03'"

    elif str_pavimentp == 'PARALELEPÍPEDO':
        codig_pavimento = "'04'"

    elif str_pavimentp == 'TERRA':
        codig_pavimento = "'05'"

    elif str_pavimentp == 'OUTROS':
        codig_pavimento = "'09'"
    else:
        codig_pavimento = "'99'"

    return codig_pavimento


# -------------------------------------------------------  Criação de dataframe -------------------------------
tabela = pd.read_excel(
    'C:/Users/phmnsilva/Downloads/SEINFRA_AGOSTO2022.xlsx', sheet_name="SEINFRO")

tabela = tabela[['NUANO', 'NUBOLETIM', 'SGRODOVIA', 'NUKM', 'DETIPOACOSTAMENTO',
                 'DETIPOPAVIMENTO']].drop_duplicates().reset_index(drop=True)

# -------------------------------------------------------- Conexão ----------------------------------------------
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DTRC02;"
    "Database=renaest;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

# --------------------------------------------------------- Criação de variaveis para script --------------------
for i in range(0, len(tabela)):

    identificacao_acidente = f"'{tabela['SGRODOVIA'][i].strip() + '' + str(tabela['NUANO'][i])}'"
    acostamento = tipoAcostamento(tabela['DETIPOACOSTAMENTO'][i])
    tp_pavimento = tipoPavimento(tabela['DETIPOPAVIMENTO'][i])
    sg.one_line_progress_meter('My Meter', i, len(
        tabela), 'key', 'Optional message', orientation="h", size=(50, 30))

    comando = f"""INSERT INTO [dbo].[Dados_Via]
            (
            [Indentificacao_Acidente],
            [Acostamento],
            [Canteiro_Central], 
            [Condicao_Via],
            [Cruzamento],
            [Curva_Via],
            [Tp_Pavimento],
            [Classe_Funcional_Via],
            [Controle_Trafego_Cruzamento],
            [Limite_Velocidade],
            [Obstaculo_Via],
            [Superficie_Trecho_Viario],
            [Urbanizacao],
            [Jurisprudencia_via],
            [Tp_Pista],
	        [Trava_Seguranca_Metalica]
            )

                VALUES
                
                ( {identificacao_acidente},{acostamento}, '0','00','00','00',{tp_pavimento}, '00','00','000','0','00','0','00', '00', '0')"""
    cursor.execute(comando)

cursor.commit()
sg.popup('Os dados foram transferidos para o Banco de dados.')
