import PySimpleGUI as fe

conta = [
    [fe.Text('Usuário')],
    [fe.Input(key='Usuário')],
    [fe.Text('Senha')],
    [fe.Input(key='Senha')],
    [fe.Button('Login')],
    [fe.Text('', key='Mensagem')],
]

window = fe.Window('Entre Com Sua Conta', layout=conta)

while True:
    event, value = window.read()
    if event == fe.WIN_CLOSED:
        break
    elif event == 'Login':
        usuario_correto = 'Danilo'
        senha_correta = '123'
        usuario = value['Usuário']
        senha = value['Senha']
        if senha == usuario_correto and senha_correta:
            window['Mensagem'].update('Logi Feito Com Sucesso')
        else:
            window['Mensagem'].update('Usuário Ou Senha Incorreto')
