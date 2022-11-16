from datetime import datetime
import os
import pyodbc
import pandas as pd
from asyncio.windows_events import NULL
import math
from tabela_Veiculos import codVeiculo
import PySimpleGUI as sg

# -------------------------------------------- FUNÇÔES --------------------------------------------------------


def testeVazioCpf(variavel_testada):

    if math.isnan(variavel_testada) or variavel_testada == 'NaT' or variavel_testada is None:
        variavel_retorno = '0'*11
        variavel_retorno = f"'{variavel_retorno}'"

    else:
        variavel_retorno = str(int(variavel_testada)).strip()
        if len(variavel_retorno) < 11:
            variavel_retorno = "'{:0>11}'".format(variavel_retorno)

        else:
            variavel_retorno = f"'{variavel_retorno}'"

    return variavel_retorno


def testeVazioDataNasc(variavel_testada):

    data_errada = variavel_testada

    if type(data_errada) == str:
        data_errada = datetime.strptime(
            data_errada, '%m/%d/%Y').date()
        data_retorno = datetime.strftime(data_errada, '%d%m%Y')
    else:
        variavel_retorno = str(variavel_testada)[:10]
        if variavel_retorno == 'nan' or variavel_retorno == 'None' or variavel_retorno == 'NaT':
            data_retorno = f"'00000000'"
        else:
            #variavel_retorno = f"'{str(variavel_retorno)}'"
            data_retorno = str(variavel_testada.strftime(
                "%d-%m-%Y")).replace("-", '')
            data_retorno = f"'{data_retorno}'"

    return data_retorno


def exameRealizado(exame):
    str_exame = str(exame).strip().upper()
    if str_exame == 'NAN' or str_exame == 'NONE' or str_exame == 'NAT':
        cod_exame = "'0'"
    elif 'ETILÔMETRO' in str_exame:
        cod_exame = "'1'"
    elif 'SANGUÍNEO' in str_exame:
        cod_exame = "'2'"
    elif 'SEM COLETA' in str_exame:
        cod_exame = "'3'"
    else:
        cod_exame = "'9'"

    return cod_exame


def tpGenero(genero):
    str_genero = str(genero).strip().upper()
    if str_genero == 'NAN' or str_genero == 'NONE' or str_genero == 'NAT':
        cod_genero = "'0'"
    elif str_genero == 'M':
        cod_genero = "'1'"
    elif str_genero == 'F':
        cod_genero = "'2'"
    else:
        cod_genero = "'9''"

    return cod_genero


def enderecoEnvolvido(endereco):
    str_endereco = str(endereco).strip().replace("'", "''")
    if str_endereco == 'nan' or str_endereco == 'None' or str_endereco == 'NaT':
        endereco_retorno = '$'*40
    else:
        if len(str_endereco) < 40:
            x = 40 - len(str_endereco)
            endereco_retorno = str_endereco + '$'*x

    endereco_retorno = f"'{str(endereco_retorno)}'"

    return endereco_retorno


def nomeEnvolvido(nome):
    str_nome = str(nome).strip().upper()
    if str_nome == 'NAN' or str_nome == 'NONE' or str_nome == 'NAT':
        nome_retorno = '$'*60
    else:
        if len(str_nome) < 60:
            x = 60 - len(str_nome)
            nome_retorno = str_nome + '$'*x

    nome_retorno = f"'{nome_retorno}'"

    return nome_retorno


def gravLesao(lesao):
    str_lesao = str(lesao).strip().upper()
    if str_lesao == 'NAN' or str_lesao == 'NONE' or str_lesao == 'NAT':
        cod_lesao = f"'00'"
    elif 'GRAVE' in str_lesao:
        cod_lesao = "'02'"
    elif 'LEVE' in str_lesao:
        cod_lesao = "'03'"
    elif 'SEM FERIMENTO' in str_lesao:
        cod_lesao = "'04'"
    else:
        cod_lesao = "'99'"

    return cod_lesao


def equipSeg(tipoVeiculo, capacete, cinto):
    cod_tipo_Veiculo = codVeiculo(tipoVeiculo)
    str_capacete = str(capacete).strip().upper()
    str_cinto = str(cinto).strip().upper()
    if (str_capacete == 'NAN' or str_capacete == 'NONE' or str_capacete == 'NAT') and (str_cinto == 'NAN' or str_cinto == 'NONE' or str_cinto == 'NAT'):
        cod_equip_seg = "'00'"

    elif cod_tipo_Veiculo == "'2'" or cod_tipo_Veiculo == "'12'" or cod_tipo_Veiculo == "'14'" or cod_tipo_Veiculo == "'15'" or cod_tipo_Veiculo == "'18'" or cod_tipo_Veiculo == "'24'" or cod_tipo_Veiculo == "'29'":
        if str_capacete == 'S':
            cod_equip_seg = "'10'"
        else:
            cod_equip_seg = "'09'"
    elif cod_tipo_Veiculo == "'1'" or cod_tipo_Veiculo == "'3'" or cod_tipo_Veiculo == "'4'" or cod_tipo_Veiculo == "'5'" or cod_tipo_Veiculo == "'6'" or cod_tipo_Veiculo == "'7'" or cod_tipo_Veiculo == "'13'" or cod_tipo_Veiculo == "'16'" or cod_tipo_Veiculo == "'17'" or cod_tipo_Veiculo == "'21'" or cod_tipo_Veiculo == "'26'" or cod_tipo_Veiculo == "'27'" or cod_tipo_Veiculo == "'28'":
        if str_cinto == 'S':
            cod_equip_seg = "'01'"
        else:
            cod_equip_seg = "'02'"
    elif cod_tipo_Veiculo == "'22'":
        cod_equip_seg = "'07'"
    else:
        cod_equip_seg = "'99'"

    return cod_equip_seg


def suspeitaAlcool(voz, tontura, halito):
    str_voz = str(voz).strip().upper()
    str_tontura = str(tontura).strip().upper()
    str_halito = str(halito).strip().upper()
    if (str_voz == 'NAN' or str_voz == 'NONE' or str_voz == 'NAT') and (str_tontura == 'NAN' or str_tontura == 'NONE' or str_tontura == 'NAT') and (str_halito == 'NAN' or str_halito == 'NONE' or str_halito == 'NAT'):
        suspeita_alcool = f"'0'"

    elif str_voz == 'S' or str_tontura == 'S' or str_halito == 'S':
        suspeita_alcool = "'2'"

    elif str_voz == 'N' and str_tontura == 'N' and str_halito == 'N':
        suspeita_alcool = "'1'"
    else:
        suspeita_alcool = "'9'"

    return suspeita_alcool


# -------------------------------------------------------  Criação de dataframe -------------------------------
tabela = pd.read_excel(
    'C:/Users/phmnsilva/Downloads/SEINFRA_AGOSTO2022.xlsx', sheet_name="SEINFRO").sort_values(by='NUBOLETIM')

# -------------------------------------------------------- Conexão ----------------------------------------------
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DTRC02;"
    "Database=renaest;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


seq_pessoa_envolvido = 0
contador = 0
id = f"{tabela['NUBOLETIM'][0]}{str(tabela['SGRODOVIA'][0]).strip()}{int(tabela['NUKM'][0])}"
# --------------------------------------------------------- Criação de variaveis para script --------------------
for i in range(0, len(tabela)):

    identificacao_acidente = f"'{tabela['SGRODOVIA'][i].strip() + '' + str(tabela['NUANO'][i])}'"
    cpf_envolvido = testeVazioCpf(tabela['NUCPF'][i])
    data_nascimento_envolvido = testeVazioDataNasc(tabela['DTNASCIMENTO'][i])
    nome_envolvido = nomeEnvolvido(tabela['NMVITIMA'][i])
    genero_envolvido = tpGenero(tabela['FLSEXO'][i])
    endereco_envolvido = enderecoEnvolvido(tabela['DEENDERECO'][i])
    equip_seg_envolvido = equipSeg(
        tabela['DEESPECIEVEICULO'][i], tabela['FLCAPACETE'][i], tabela['FLCINTOSEGURANCA'][i])
    grav_lesao_envolvido = gravLesao(tabela['DECONDFERIMENTO'][i])
    suspeito_alcool = suspeitaAlcool(
        tabela['FLVOZANORMAL'][i], tabela['FLMARCHAEBRIOSA'][i], tabela['FLHALITOSE'][i])
    teste_alcool_envolvido = exameRealizado(tabela['FLEXAMEREALIZ'][i])
    sg.one_line_progress_meter('Loading', i, len(
        tabela), 'key', 'Optional message', orientation="h", size=(50, 30))

    # ------- analise de sequencial de envolvidos, e retorna o valor

    primeiro_escopo = f"{tabela['NUBOLETIM'][i]}{str(tabela['SGRODOVIA'][i]).strip()}{int(tabela['NUKM'][i])}"
    if id == primeiro_escopo:
        contador += 1
    else:
        contador = 1
        id = primeiro_escopo

    seq_pessoa_envolvido = "'{:0>3}'".format(contador)
    # --------

    comando = f"""INSERT INTO [dbo].[Dados_Pessoa]
            (
            [Identificacao_Acidente],
            [CPF_Envolvido],
            [Numero_Registro_CNH],
            [Dt_Nasc_Envolvido],
            [Nome_Envolvido],
            [Nome_Mae_Envolvido],
            [Tp_Genero_Envolvido],
            [Dt_Obito_Envolvido],
            [Tp_User_Via_Envolvido],
            [Tp_Vitima_Envolvido],
            [CEP_Endereco_Envolvido],
            [Endereco_Envolvido],
            [Numero_Endereco_Envolvido],
            [Bairro_Endereco_Envolvido],
            [Municipio_Endereco_Envolvido],
            [UF_Endereco_Envolvido],
            [Equip_Seg_Envolvido],
            [Grav_Lesao_Envolvido],
            [Suspeito_uso_Alcool_Envolvido],
            [Teste_Alcool_Envolvido],
            [Resultado_Alcool_Envolvido],
            [Suspeito_Uso_Drogas_Envolvido],
            [Teste_Drogas_Envolvido],
            [Resultado_Teste_Drogas],
            [Posicao_Assento_Envolvido],
            [Manobra_Pedestre_Envolvido],
            [Seq_Pessoa_Envolvido],
            [Encaminhamento_Envolvido],
            [Receptor_Vitima_Envolvido],
            [Indi_Pessoa_estrangeira],
            [Indi_Pessoa_com_Deficiencia]
            )

                VALUES
                
                ( {identificacao_acidente},{cpf_envolvido}, '00000000000'
                ,{data_nascimento_envolvido},{nome_envolvido},'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                ,{genero_envolvido}, '00000000', '00', '0', '00000000',{endereco_envolvido}
                ,'00000', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', '00000', '$$', {equip_seg_envolvido},{grav_lesao_envolvido}
                ,{suspeito_alcool}, {teste_alcool_envolvido}, '0', '0', '0', '0', '00', '00', {seq_pessoa_envolvido}, '00', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', '0', '0')"""
    cursor.execute(comando)

cursor.commit()
sg.popup('Os dados foram transferidos para o Banco de dados.')
