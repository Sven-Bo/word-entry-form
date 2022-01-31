import datetime
from pathlib import Path

import PySimpleGUI as sg
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "vendor-contract.docx"
doc = DocxTemplate(document_path)

today = datetime.datetime.today()
today_in_one_week = today + datetime.timedelta(days=7)

layout = [
    [sg.Text("Client name:"), sg.Input(key="CLIENT", do_not_clear=False)],
    [sg.Text("Vendor name:"), sg.Input(key="VENDOR", do_not_clear=False)],
    [sg.Text("Amount:"), sg.Input(key="AMOUNT", do_not_clear=False)],
    [sg.Text("Description1:"), sg.Input(key="LINE1", do_not_clear=False)],
    [sg.Text("Description2:"), sg.Input(key="LINE2", do_not_clear=False)],
    [sg.Button("Create Contract"), sg.Exit()],
]

window = sg.Window("Contract Generator", layout, element_justification="right")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Create Contract":
        # Add calculated fields to our dict
        values["NONREFUNDABLE"] = round(float(values["AMOUNT"]) * 0.2, 2)
        values["TODAY"] = today.strftime("%Y-%m-%d")
        values["TODAY_IN_ONE_WEEK"] = today_in_one_week.strftime("%Y-%m-%d")

        # Render the template, save new word document & inform user
        doc.render(values)
        output_path = Path(__file__).parent / f"{values['VENDOR']}-contract.docx"
        doc.save(output_path)
        sg.popup("File saved", f"File has been saved here: {output_path}")

window.close()