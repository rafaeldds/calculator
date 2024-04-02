import flet as ft
from flet import colors

bottons = [
    {'operator': 'AC', 'font': colors.BLACK, 'bottom': colors.BLUE_GREY_100},
    {'operator': '±', 'font': colors.BLACK, 'bottom': colors.BLUE_GREY_100},
    {'operator': '%', 'font': colors.BLACK, 'bottom': colors.BLUE_GREY_100},
    {'operator': '/', 'font': colors.WHITE, 'bottom': colors.ORANGE},
    {'operator': '7', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '8', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '9', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '*', 'font': colors.WHITE, 'bottom': colors.ORANGE},
    {'operator': '4', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '5', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '6', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '-', 'font': colors.WHITE, 'bottom': colors.ORANGE},
    {'operator': '1', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '2', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '3', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '+', 'font': colors.WHITE, 'bottom': colors.ORANGE},
    {'operator': '0', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '.', 'font': colors.WHITE, 'bottom': colors.WHITE24},
    {'operator': '=', 'font': colors.WHITE, 'bottom': colors.ORANGE}
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 380
    page.title = 'Calculator'
    page.window_always_on_top = True
    page.window_left = 0

    result = ft.Text(value ='0', color=colors.WHITE, size=20)

    display = ft.Row(
        width=250,
        controls=[result],
        alignment='end',
    )

    btn = [ft.Container(
            content=ft.Text(value=btn['operator'], color=btn['font']),
            width=50,
            height=50,
            bgcolor=btn['bottom'],
            border_radius=100,
            alignment=ft.alignment.center
        ) for btn in bottons]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)

ft.app(target = main)