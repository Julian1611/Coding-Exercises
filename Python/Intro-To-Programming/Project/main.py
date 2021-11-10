# final code
#
#
### --- program purposes --- ###
# get depot statement from user
# show conclusion of that statement (pie chart, performance, outlook, etc.)
# recommend changes

import stock
import PySimpleGUI as sg

layout = [[sg.Text("This a test!")], [sg.Button("MONEY")]]

# Create the window
window = sg.Window("STONKS", layout, margins=(100,100))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()