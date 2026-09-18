from nicegui import ui
item = []

def render_list():
    list_container.clear()
    with list_container:
        if not item:
            ui.label('Lista vacía').classes('text-green-700 italic')
            return

        with ui.row().classes('items-center gap-2 flex-wrap'):
            for idx, val in enumerate(item):
                with ui.column().classes('items-center gap-1'):
                    ui.label(str(val)).classes('w-16 h-16 flex items-center justify-center '
                        'bg-green-700 text-white font-bold text-lg rounded-lg shadow-md')
                    ui.label(f'[{idx}]*').classes('text-xs font-semibold text-green-900')

def do_append():
    if val_input.value is not None:
        item.append(val_input.value)
        render_list()    

def do_insert():
    if val_input.value is not None and idx_input is not None:
        idx = max(0, min(int(idx_input.value), len(item)))
        item.insert(idx, val_input.value)
        render_list()


def do_pop():
    if not item:
        return

    idx = len(item) - 1 if idx_input.value is None else int(idx_input.value)
    idx = max(0, min(idx, len(item) - 1))
    item.pop(idx)
    render_list()

def do_remove():
    if val_input.value is None:
        return

    try:
        item.remove(val_input.value)
    except ValueError:
        ui.notify('El valor no está en la lista', type='warning')
        return
    render_list()

def do_sort():
    item.sort()
    render_list()

def do_reverse():
    item.reverse()
    render_list()

def do_count():
    if val_input.value is None:
        return

    ui.notify(f'El valor aparece {item.count(val_input.value)} vez/veces')

def do_clear():
    item.clear()
    render_list()


ui.page_title('Visualizador de Listas en Python con NiceGui')

with ui.column().classes('p-6 gap-6 w-full'):
    ui.label('Practica Grafica de una Lista').classes('text-2xl font-bold text-green-900')

    with ui.card().classes('w-full p-4 min-h-[140px] bg-green-50 border-green-200'):
        list_container = ui.row().classes('w-full items-center')

    with ui.card().classes('w-full p-4 gap-4'):
        ui.label('OPERACIONES').classes('text-sm font-semibold text-green-700')   

        with ui.row().classes('gap-4 items-center'):
            val_input = ui.number('Valor', placeholder="Introduce un número").classes('w-40')
            idx_input = ui.number('Indice', value=0, min=0).classes('w-40')

        with ui.row():
            ui.button('append(x)', icon='add', color='green', on_click=do_append)
            ui.button('remove(x)', icon='remove', color='red', on_click=do_remove)
            ui.button('insert(i)', icon='add_circle', color='green', on_click=do_insert)
            ui.button('pop(i)', icon='remove', color='red', on_click=do_pop)
            ui.button('sort()', icon='sort', color='green', on_click=do_sort)
            ui.button('reverse()', icon='swap_vert', color='green', on_click=do_reverse)
            ui.button('count(x)', icon='123', color='green', on_click=do_count)
            ui.button('clear()', icon='delete', color='red', on_click=do_clear)
render_list()
ui.run()