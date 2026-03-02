import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.padding = 20

    titulo = ft.Text(
        value="Formulario de Registro de Eventos",
        size=28,
        weight=ft.FontWeight.BOLD
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
        hint_text="Ej. Congreso de Tecnología"
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión")
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual")
        ]),
        value="Presencial"
    )

    requiere_inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1
    )

    fecha_evento = ft.Text("Fecha no seleccionada")

    def cambiar_fecha(e):
        fecha = e.control.value
        fecha_evento.value = f"Fecha seleccionada: {fecha.strftime('%d/%m/%Y')}"
        page.update()

    date_picker = ft.DatePicker(
        on_change=cambiar_fecha
    )

    page.overlay.append(date_picker)

    boton_fecha = ft.ElevatedButton(
        text="Seleccionar fecha",
        on_click=lambda e: date_picker.pick_date()
    )

    resumen = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.W_500,
        color="blue"
    )

    def mostrar_resumen(e):
        if nombre_evento.value.strip() == "":
            resumen.value = "❌ Error: El nombre del evento no puede estar vacío."
            resumen.color = "red"
        else:
            resumen.value = f"""
Nombre: {nombre_evento.value}
Tipo: {tipo_evento.value}
Modalidad: {modalidad.value}
Requiere inscripción: {"Sí" if requiere_inscripcion.value else "No"}
Duración: {int(duracion.value)} horas
{fecha_evento.value}
"""
            resumen.color = "green"

        page.update()

    boton_resumen = ft.ElevatedButton(
        text="Mostrar resumen",
        on_click=mostrar_resumen,
        bgcolor="blue",
        color="white"
    )

    # -----------------------------
    # Layout Principal
    # -----------------------------
    page.add(
        ft.Column(
            controls=[
                titulo,
                nombre_evento,
                tipo_evento,
                ft.Text("Modalidad:"),
                modalidad,
                requiere_inscripcion,
                ft.Text("Duración estimada (horas):"),
                duracion,
                boton_fecha,
                fecha_evento,
                boton_resumen,
                ft.Divider(),
                resumen
            ],
            spacing=15
        )
    )

ft.app(target=main)