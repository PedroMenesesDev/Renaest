from datetime import datetime
import pyodbc
import pandas as pd
from asyncio.windows_events import NULL
import PySimpleGUI as sg

# -------------------------------------------- FUNÇÔES --------------------------------------------------------


def testeVazioData(variavel_testada):

    variavel_retorno = str(variavel_testada)[:10]
    if variavel_retorno == 'nan' or variavel_retorno == 'None' or variavel_retorno == 'NaT':
        data_retorno = f"'00000000'"
    else:
        if type(variavel_testada) == str:
            data_retorno = datetime.strptime(
                variavel_testada, '%m/%d/%Y').date()
            data_retorno = datetime.strftime(data_retorno, '%d%m%Y')
            data_retorno = f"'{data_retorno}'"
        else:
            data_retorno = datetime.strftime(variavel_testada, '%m%d%Y')
            data_retorno = f"'{data_retorno}'"

    return data_retorno


def diaSemana(data):

    str_data = str(data)[:10]
    if str_data == 'nan' or str_data == 'None' or str_data == 'NaT':
        data_retorno = f"'0'"
    else:
        if type(data) == str:
            data_retorno = datetime.strptime(
                data, '%m/%d/%Y').date()
            data_retorno = datetime.strftime(data_retorno, '%w')
            data_retorno = f"'{int(data_retorno)+1}'"
        else:
            data_retorno = datetime.strftime(data, '%m%d%Y')
            data_retorno = datetime.strptime(
                data_retorno, '%d%m%Y').date()
            data_retorno = datetime.strftime(data_retorno, '%w')
            data_retorno = f"'{int(data_retorno)+1}'"

    return data_retorno


def faseDia(hora):

    str_hora = str(hora).upper()
    if str_hora == 'NAN' or str_hora == 'NONE' or str_hora == 'NAT':
        str_fase_dia = "'0'"
    elif hora > 0 and hora < 559:
        str_fase_dia = "'4'"
    elif hora > 559 and hora < 1159:
        str_fase_dia = "'1'"
    elif hora > 1159 and hora < 1759:
        str_fase_dia = "'2'"
    elif hora > 1759 and hora < 2359:
        str_fase_dia = "'3'"
    else:
        str_fase_dia = "'9'"

    return str_fase_dia


def enderecoAcidente(variavel_testada):
    variavel_retorno = str(variavel_testada).strip().replace("'", "''")
    if variavel_retorno == 'nan' or variavel_retorno == 'None' or variavel_retorno == 'NaT':
        variavel_retorno = '$'*40
        variavel_retorno = f"'{str(variavel_retorno)}'"
    else:
        if len(variavel_retorno) < 40:
            x = 40 - len(variavel_retorno)
            variavel_retorno += '$'*x

    variavel_retorno = f"'{str(variavel_retorno)}'"

    return variavel_retorno


def ufAcidente(variavel_testada):
    variavel_retorno = str(variavel_testada).strip().replace("'", "''")
    if variavel_retorno == 'nan' or variavel_retorno == 'None' or variavel_retorno == 'NaT':
        variavel_retorno = '$$'
        variavel_retorno = f"'{str(variavel_retorno)}'"
    else:
        variavel_retorno = f"'{str(variavel_retorno)}'"

    return variavel_retorno


def condTempo(tempo):
    str_tempo = str(tempo).strip().upper()
    if str_tempo == 'NAN' or str_tempo == 'NONE' or str_tempo == 'NAT':
        cod_tempo = f"'00'"
    elif 'BOM' in str_tempo:
        cod_tempo = "'01'"
    elif 'CHUVOSO' in str_tempo or 'CHUVA' in str_tempo:
        cod_tempo = "'02'"
    elif 'NEVE' in str_tempo:
        cod_tempo = "'04'"
    elif 'NEBLINA' in str_tempo:
        cod_tempo = "'05'"
    elif 'NUBLADO' in str_tempo:
        cod_tempo = "'06'"
    elif 'GRANIZO' in str_tempo:
        cod_tempo = "'07'"
    elif 'VENTO' in str_tempo:
        cod_tempo = "'08'"
    elif 'OUTR' in str_tempo:
        cod_tempo = "'09'"
    else:
        cod_tempo = "'99'"

    return cod_tempo


def condLuminosidade(luminosidade):
    str_luminosidade = str(luminosidade).strip().upper()
    if str_luminosidade == 'NAN' or str_luminosidade == 'NONE' or str_luminosidade == 'NAT':
        cod_luminosidade = f"'00'"
    elif 'DIA' in str_luminosidade:
        cod_luminosidade = "'01'"
    elif 'AMANHACENDO' in str_luminosidade or 'CRESPÚSCULO' in str_luminosidade:
        cod_luminosidade = "'02'"
    elif str_luminosidade == 'ESCURIDÃO':
        cod_luminosidade = "'03'"
    elif 'VIA NÃO ILUMINADA' in str_luminosidade:
        cod_luminosidade = "'04'"
    elif 'VIA ILUMINADA' in str_luminosidade:
        cod_luminosidade = "'05'"
    else:
        cod_luminosidade = "'99'"

    return cod_luminosidade


def tipoAcidente(acidente):
    str_acidente = str(acidente).strip().upper()
    if str_acidente == 'NAN' or str_acidente == 'NONE' or str_acidente == 'NAT':
        cod_tipo_acidente = f"'00'"
    elif 'PEDESTRE' in str_acidente:
        cod_tipo_acidente = "'01'"
    elif 'CAPOTAMENTO' in str_acidente:
        cod_tipo_acidente = "'03'"
    elif str_acidente == 'CHOQUE':
        cod_tipo_acidente = "'04'"
    elif str_acidente == 'COLISÃO':
        cod_tipo_acidente = "'05'"
    elif 'FRONTAL' in str_acidente:
        cod_tipo_acidente = "'06'"
    elif 'LATERAL' in str_acidente:
        cod_tipo_acidente = "'07'"
    elif 'TRANSVERSAL' in str_acidente:
        cod_tipo_acidente = "'08'"
    elif 'TRASEIRA' in str_acidente:
        cod_tipo_acidente = "'09'"
    elif 'ENGAVETAMENTO' in str_acidente:
        cod_tipo_acidente = "'10'"
    elif 'QUEDA' in str_acidente:
        cod_tipo_acidente = "'11'"
    elif str_acidente == 'TOMBAMENTO':
        cod_tipo_acidente = "'12'"
    elif 'ANIMAL' in str_acidente:
        cod_tipo_acidente = "'13'"
    elif 'OUTRO' in str_acidente:
        cod_tipo_acidente = "'14'"
    elif 'ENGAVETAMENTO' in str_acidente:
        cod_tipo_acidente = "'10'"
    else:
        cod_tipo_acidente = "'99'"

    return cod_tipo_acidente


def testeVazioMunic(variavel_testada):
    variavel_retorno = str(variavel_testada).strip().replace("'", "''")
    if variavel_retorno == 'nan' or variavel_retorno == 'None' or variavel_retorno == 'NaT':
        variavel_retorno = f"'00000'"
    else:
        variavel_retorno = f"'{str(variavel_retorno)}'"

    return variavel_retorno


def testeVazioHora(variavel_testada):
    variavel_retorno = str(variavel_testada).strip().replace("'", "''")
    if variavel_retorno == 'nan' or variavel_retorno == 'None' or variavel_retorno == 'NaT':
        variavel_retorno = f"'999999'"
    else:
        variavel_retorno = f"'{str(variavel_retorno)}'"

    return variavel_retorno


def testeVazioKm(variavel_testada):
    variavel_retorno = str(variavel_testada).strip().upper()
    if variavel_retorno == 'NAN' or variavel_retorno == 'NONE' or variavel_retorno == 'NAT':
        variavel_retorno = f"'0000'"
    else:
        km = str(int(variavel_testada/1000))

        variavel_retorno = f"'{km}'"

    return variavel_retorno


# -------------------------------------------------------  Criação de dataframe -------------------------------
tabela = pd.read_excel(
    'C:/Users/phmnsilva/Downloads/SEINFRA_AGOSTO2022.xlsx', sheet_name="SEINFRO")

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
    hora_acidente = testeVazioHora(tabela['HRACIDENTE'][i])
    data_acidente = testeVazioData(tabela['DTACIDENTE'][i])
    endereco_acidente = enderecoAcidente(tabela['DETRECHO'][i][:40])
    cod_municipio = testeVazioMunic(tabela['CDMUNICIPIO'][i])
    uf_ocorrencia_acidente = ufAcidente(tabela['SGUNIDADEFEDERAL'][i])
    km_via_acidente = testeVazioKm(tabela['NUKM'][i])
    tipo_acidente = tipoAcidente(tabela['DETIPOACIDENTE'][i])
    cond_iluminacao = condLuminosidade(tabela['DELUMINOSIDADE'][i])
    cond_tempo = condTempo(tabela['DECONDICAOTEMPO'][i])
    dia_semana = diaSemana(tabela['DTACIDENTE'][i])
    fase_dia = faseDia(tabela['HRACIDENTE'][i])
    sg.one_line_progress_meter('My Meter', i, len(
        tabela), 'key', 'Optional message', orientation="h", size=(50, 30))
    

    comando = f"""
            INSERT INTO [dbo].[Dados_Acidente]
            (
            [Identificacao_Acidente],
            [Data_Acidente],
            [Hora_acidente],
            [CEP_Ocorrencia_Acidente],
            [Endereco_Ocorrencia_Acidente],
            [Numero_Ocorrencia_Acidente],
            [Bairro_Ocorrencia_Acidente],
            [Municipio_Ocorencia],
            [UF_Ocorrencia_Acidente],
            [Quadra_Trecho_Referencia],
            [KM_Via_Acidente],
            [Tp_Acidente],
            [Condicao_iluminacao],
            [Condicoes_Meteorologicas],
            [Nome_Comunicante],
	        [Tp_Impacto],
            [Dia_Semana],
            [Fase_Dia],
            [Sentido_Via],
            [Causa_Principal],
            [Causas_Concorrentes],
            [Dano_Meio_Ambiente],
            [Dano_Patrimonio],
            [DataHora_Abertura_Comunicacao],
            [DataHora_Acionamento_Equipe],
            [DataHora_Finalizacao_Atendimento],
            [DataHora_Fim_Preenchimento_Ocorrencia],
            [DataHora_Inicio_Atendimento],
            [DataHora_Inicio_Preenchimento_Ocorrencia],
            [Indicador_Processo],
            [Status_Registro],
            [Latitude],
            [Longitude],
            [Numero_Pedestres_envolvidos],
            [Metodo_Coleta]
            )

            VALUES
                
                ({identificacao_acidente}, {data_acidente}, {hora_acidente}, '00000000',{endereco_acidente},'00000'
                , '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',{cod_municipio}, {uf_ocorrencia_acidente}, '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',{km_via_acidente}, {tipo_acidente}
                , {cond_iluminacao}, {cond_tempo}, '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' , '00' ,{dia_semana}, {fase_dia}
                ,'0' , '00', '00000000000000000000', '0', '0', '00000000000000', '00000000000000', '00000000000000'
                , '00000000000000', '00000000000000', '00000000000000', '0', '0', '$$$$$$$$$$$', '$$$$$$$$$$$','000', '0')"""

    cursor.execute(comando)

cursor.commit()
sg.popup('Os dados foram transferidos para o Banco de dados.')
