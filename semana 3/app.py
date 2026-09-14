from nicegui import ui

ui.markdown('# NiceGUI Example')
ui.button('Click me', on_click=lambda: ui.notify('0')) 

ui.run(host="127.0.0.1", port=8080, title="NiceGUI Example", favicon="favicon.ico")
UnicodeWarning() 