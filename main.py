import flet as ft

def main(page):
    tasks = []

    # Función para añadir una nueva entrada
    def add_clicked(e):
        # Asegura que todos los campos tengan algún valor
        if new_task.value and new_task1.value and new_task2.value:
            # Crea una nueva fila con los valores actuales de los campos de texto
            new_row = ft.DataRow(cells=[
                ft.DataCell(ft.Text(new_task.value)),
                ft.DataCell(ft.Text(new_task1.value)),
                ft.DataCell(ft.Text(new_task2.value)),
            ])
            # Añade la nueva fila a la lista de filas de la DataTable
            data_table.rows.append(new_row)
            # Añade la entrada a la lista de tareas
            tasks.append((new_task.value, new_task1.value, new_task2.value))
            # Actualiza la DataTable en la interfaz de usuario
            page.update()
        
            # Limpia los campos de entrada
            new_task.value = ""
            new_task1.value = ""
            new_task2.value = ""
            new_task.focus()
            new_task1.focus()
            new_task2.focus()
            new_task.update()
            new_task1.update()
            new_task2.update()
        else:
            # Muestra un mensaje de error si alguno de los campos está vacío
            page.snack_bar = ft.SnackBar(content=ft.Text("Todos los campos son obligatorios"))
            page.update()

    # Función para mostrar la vista principal
    def show_main_view():
        page.controls.clear()
        page.add(ft.Column([input_row, data_table, search_button]))
        page.update()

    # Función para mostrar la vista de búsqueda
    def show_search_view():
        page.controls.clear()
        page.add(search_view)
        page.update()

    # Función para buscar y filtrar las entradas
    def search_and_filter(e):
        search_term = search_input.value.lower()
        filtered_tasks = [task for task in tasks if search_term in task[0].lower()]
        search_results.rows = [
            ft.DataRow(cells=[ft.DataCell(ft.Text(task[0])), ft.DataCell(ft.Text(task[1])), ft.DataCell(ft.Text(task[2]))])
            for task in filtered_tasks
        ]
        page.update()

    # Interfaz de usuario para la vista principal
    new_task = ft.TextField(hint_text="¿Qué ejercicio vas a hacer?", width=300)
    new_task1 = ft.TextField(hint_text="¿Qué peso vas a usar?", width=300)
    new_task2 = ft.TextField(hint_text="¿Cuántas repeticiones?", width=300)
    add_button = ft.ElevatedButton(text="Add", on_click=add_clicked)
    input_row = ft.Row([new_task, new_task1, new_task2, add_button])
    
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Ejercicio")),
            ft.DataColumn(label=ft.Text("Peso")),
            ft.DataColumn(label=ft.Text("Repeticiones")),
        ],
        rows=[],
        width=500,
        height=300,
    )
    
    search_button = ft.ElevatedButton(text="Buscar Ejercicios", on_click=lambda e: show_search_view())

    # Interfaz de usuario para la vista de búsqueda
    search_input = ft.TextField(hint_text="Buscar por ejercicio...", autofocus=True, width=300)
    search_action_button = ft.ElevatedButton(text="Buscar", on_click=search_and_filter)
    search_results = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Ejercicio")),
            ft.DataColumn(label=ft.Text("Peso")),
            ft.DataColumn(label=ft.Text("Repeticiones")),
        ],
        rows=[],
        width=500,
        height=300,
    )
    back_button = ft.ElevatedButton(text="Volver", on_click=lambda e: show_main_view())
    search_view = ft.Column([search_input, search_action_button, search_results, back_button])

    # Muestra inicialmente la vista principal
    show_main_view()

ft.app(target=main)