import flet as ft
import datetime

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
        fecha = date_picker.value
        if fecha:
            fecha_evento.value = f"Fecha seleccionada: {fecha.strftime('%d/%m/%Y')}"
        else:
            fecha_evento.value = "Fecha no seleccionada"
        page.update()

    date_picker = ft.DatePicker(
        first_date=datetime.date.today(),
        last_date=datetime.date(2100, 12, 31),
        on_change=cambiar_fecha
    )

    page.overlay.append(date_picker)

    def abrir_datepicker(e):
        date_picker.open = True
        page.update()

    boton_fecha = ft.Button(
        content=ft.Text("Seleccionar fecha"),
        on_click=abrir_datepicker
    )

    resumen = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.W_500,
        color="blue"
    )

    def mostrar_resumen(e):
        errores = False

    if not nombre_evento.value.strip():
        nombre_evento.error_text = "Este campo es obligatorio"
        errores = True
    else:
        nombre_evento.error_text = None

    if not tipo_evento.value:
        tipo_evento.error_text = "Selecciona un tipo de evento"
        errores = True
    else:
        tipo_evento.error_text = None

    if not modalidad.value:
        errores = True

    if not date_picker.value:
        fecha_evento.value = " Debes seleccionar una fecha"
        fecha_evento.color = "red"
        errores = True
    else:
        fecha_evento.color = "black"

    if errores:
        resumen.value = "Corrige los campos marcados."
        resumen.color = "red"
    else:
        resumen.value = f"""Nombre: {nombre_evento.value}
Tipo: {tipo_evento.value}
Modalidad: {modalidad.value}
Requiere inscripción: {"Sí" if requiere_inscripcion.value else "No"}
Duración: {int(duracion.value)} horas
Fecha: {date_picker.value.strftime('%d/%m/%Y')}
"""
        resumen.color = "green"

    page.update()

    boton_resumen = ft.Button(
        content=ft.Text("Mostrar resumen", color="white"),
        bgcolor="blue",
        on_click=mostrar_resumen
    )

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