import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("Number 1")],
          [sg.Input(key='-NUM1-')],
          [sg.Text("Number 2")],
          [sg.Input(key='-NUM2-')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Add'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Addition of two number', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    num_sum = int(values['-NUM1-']) + int(values['-NUM2-'])
    window['-OUTPUT-'].update('Sum is  {}'.format(num_sum))

# Finish up by removing from the screen
window.close()
