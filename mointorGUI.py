import ping3
import PySimpleGUI as sg

layout = [
    [sg.Text("Network Monitoring Tool", expand_x=True,justification='center', pad=10)],
    [sg.Text("Enter IP Addresses / Domains:")],
    [sg.InputText("", key="IP", pad=10)],
    [sg.Text("Timeout (seconds):", )],
    [sg.InputText("", key="timeout", pad=10)],
    [sg.Button("Start Monitor", key="start", )],
    [sg.Table(headings=["IP Address", "Status"], values=[], key="table", auto_size_columns=False, justification="left", col_widths=[20, 19])]
]
sg.theme('Green')

window = sg.Window("Network Monitoring Tool", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "start":
        dest = values["IP"].split(",")
        timeout = int(values["timeout"])
        if timeout is None:
            timeout = 4
        result = []
        for dests in dest:
            if ping3.ping(dests, timeout=timeout) is False:
                status = "Unreachable"
            elif ping3.ping(dests, timeout=timeout) is None:
                status = "Invaild"
            else:
                status = "Reachable"
            result.append([dests, status])
        window["table"].update(values=result)

window.close()
