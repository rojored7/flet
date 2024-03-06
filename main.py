import flet as ft

def main(page):
    tasks = []

    def add_clicked(e):
        if new_task.value and new_task1.value and new_task2.value:
            new_task_data = (new_task.value, new_task1.value, new_task2.value)
            tasks.append(new_task_data)
            refresh_data_table()
            new_task.value, new_task1.value, new_task2.value = "", "", ""
            page.update()

    def refresh_data_table():
        data_table.rows.clear()
        for task in tasks:
            data_table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(task[0])),
                ft.DataCell(ft.Text(task[1])),
                ft.DataCell(ft.Text(task[2])),
            ]))
        page.update()

    def show_search_view(e):
        page.controls.clear()
        page.add(search_input, search_action_button, search_results, back_button)
        page.update()

    def search_and_filter(e):
        search_term = search_input.value.lower()
        filtered_tasks = [task for task in tasks if search_term in task[0].lower()]
        search_results.rows.clear()
        for task in filtered_tasks:
            search_results.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(task[0])),
                ft.DataCell(ft.Text(task[1])),
                ft.DataCell(ft.Text(task[2])),
            ]))
        page.update()

    new_task = ft.TextField(hint_text="¿Qué ejercicio vas a hacer?", width=300)
    new_task1 = ft.TextField(hint_text="¿Qué peso vas a usar?", width=300)
    new_task2 = ft.TextField(hint_text="¿Cuántas repeticiones?", width=300)
    add_button = ft.ElevatedButton(text="Añadir", on_click=add_clicked)
    
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

    search_input = ft.TextField(hint_text="Buscar por ejercicio...", width=300, autofocus=True)
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

    def show_main_view():
        page.controls.clear()
        page.add(new_task, new_task1, new_task2, add_button, data_table, ft.ElevatedButton(text="Buscar Ejercicios", on_click=show_search_view))
        page.update()

    show_main_view()

ft.app(target=main)
