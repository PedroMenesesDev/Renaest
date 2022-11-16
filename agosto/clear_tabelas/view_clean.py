import PySimpleGUI as sg


sg.theme('DarkBlue14')
layout = [
    [sg.Text('Limpar as tabelas:')],
    [sg.Checkbox('Pessoa')],
    [sg.Checkbox('Acidente')],
    [sg.Checkbox('Via')],
    [sg.Checkbox('Veiculos')],
    [sg.Push(), sg.Button('Limpar Tabela')]
]

window = sg.Window('Limpeza de Tabelas', layout=layout, size=(300, 200))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    elif values[0] or values[1] or values[2] or values[3]:
        nomes_tabelas = ''
        if values[0]:
            nomes_tabelas += '- Pessoa \n'
        if values[1]:
            nomes_tabelas += '- Acidente \n'
        if values[2]:
            nomes_tabelas += '- Via \n'
        if values[3]:
            nomes_tabelas += '- Veiculos \n'

        text = sg.PopupYesNo(
            'Deseja limpar as tabelas selecionas ?\n{}'.format(nomes_tabelas)).upper()

        if text == 'YES':
            if values[0]:
                import limpar_tab_Pess
            if values[1]:
                import limpar_tab_Acid
            if values[2]:
                import limpar_tab_Via
            if values[3]:
                import limpar_tab_Veic
        else:
            continue
        sg.popup('Tabelas Limpas: \n{}'.format(nomes_tabelas))

window.close()
exit()
