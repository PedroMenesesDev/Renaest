import tabela_Veiculos
import pyodbc
import pandas as pd
from asyncio.windows_events import NULL
import PySimpleGUI as sg

# -------------------------------------------- FUNÇÔES --------------------------------------------------------


def placaVeiculo(placa):
    str_placa = str(placa).strip().upper()
    if str_placa == 'NAN' or str_placa == 'NONE' or str_placa == 'NAT' or str_placa == 'NÃO':
        placa_return = "'$$$$$$$'"

    else:
        placa_return = f"'{str_placa}'"

    return placa_return


# -------------------------------------------------------  Criação de dataframe -------------------------------
tabela = pd.read_excel(
    'C:/Users/phmnsilva/Downloads/SEINFRA_AGOSTO2022.xlsx', sheet_name="SEINFRO")

tabela_veiculos = tabela[['NUANO', 'NUBOLETIM', 'SGRODOVIA', 'NUKM', 'NUPLACA',
                          'DEESPECIEVEICULO']].drop_duplicates().sort_values(by='NUBOLETIM').reset_index(drop=True)

# -------------------------------------------------------- Conexão ----------------------------------------------
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DTRC02;"
    "Database=renaest;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

sequencial_veiculo_acidente = 0
contador = 0
id = f"{tabela_veiculos['NUBOLETIM'][0]}{str(tabela_veiculos['SGRODOVIA'][0]).strip()}{int(tabela_veiculos['NUKM'][0])}"

# --------------------------------------------------------- Criação de variaveis para script --------------------
for i in range(0, len(tabela_veiculos)):

    identificacao_acidente = f"'{tabela_veiculos['SGRODOVIA'][i].strip()}{str(tabela_veiculos['NUANO'][i])}'"
    placa_veiculo = placaVeiculo(tabela_veiculos['NUPLACA'][i])
    tp_veiculo = tabela_Veiculos.codVeiculo(tabela['DEESPECIEVEICULO'][i])
    sg.one_line_progress_meter('Loading', i, len(
        tabela_veiculos), orientation="h", size=(50, 30))

    primeiro_escopo = f"{tabela_veiculos['NUBOLETIM'][i]}{str(tabela_veiculos['SGRODOVIA'][i]).strip()}{int(tabela_veiculos['NUKM'][i])}"
    if id == primeiro_escopo:
        contador += 1
    else:
        contador = 1
        id = primeiro_escopo
    sequencial_veiculo_acidente = "'{:0>2}'".format(
        contador)

    # -------------------------------
    comando = f"""INSERT INTO [dbo].[Dados_Veiculo]
            (
            [Identificacao_Acidente],
            [Placa_veiculo],
            [Renavam_veiculo],
            [Chassi],
            [Tp_Veiculo],
            [Manobra_Veicular],
            [Encaminhamento_Veiculo], 
            [Motivo_Encaminhamento_Veiculo],
            [Estrutura],
            [Monta],
            [Receptor_Veiculo_orgao],
	        [Sequencial_Veiculo_acidente],
            [Numero_Ocupantes_Veiculo],
            [Indicador_veiculo_Estrangeiro]            
            )

                VALUES
                
                ({identificacao_acidente}, {placa_veiculo},'00000000000', '$$$$$$$$$$$$$$$$$$$$$', {tp_veiculo}, '00', '0', '0', '0', '0'
                , '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', {sequencial_veiculo_acidente},'000', '0')"""

    cursor.execute(comando)

cursor.commit()
sg.popup('Os dados foram transferidos para o Banco de dados.')
