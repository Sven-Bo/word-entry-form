import PySimpleGUI as sg

layout = [
    [sg.Text("First Name"), sg.Input(key="FIRST_NAME")],
    [sg.Text("Last Name"), sg.Input(key="LAST_NAME")],
    [sg.Button("Read"), sg.Exit()],
]

window = sg.Window("My first GUI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Read":
        print(event, values)

window.close()