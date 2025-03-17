from nicegui import ui

# Define the color scheme
ui.colors(
      primary='#1976d2',
      secondary='#26a69a',
      accent='#9c27b0',
      positive='#84c292',
      negative='#5f648c',
      info='#52b3c7',
      warning='#f2ce6b'
)

# Function to convert between Celsius and Fahrenheit
def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")

# Function to convert between Kelvin and other temperature scales
def convert_kelvin():
    try:
        temp = float(kelvin_input.value)
        if kelvin_conversion_type.value == "Celsius to Kelvin":
            kelvin_result_label.set_text(f"{temp}°C = {temp + 273.15:.2f}K")
        else:
            kelvin_result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9 + 273.15:.2f}K")
        kelvin_result_label.classes("text-lg font-semibold text-info mt-4")
    except ValueError:
        kelvin_result_label.set_text("Please enter a valid number.")
        kelvin_result_label.classes("text-lg font-semibold text-negative mt-4")

# Organize the two cards side by side
with ui.row().classes("w-full justify-center gap-8 mt-10"):

    # First Card: Celsius <-> Fahrenheit Converter
    with ui.card().classes("w-100 p-6 shadow-xl rounded-xl bg-red-50 border border-gray-200"): 
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 underline")
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded bg-gray-50")
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded bg-primary hover:bg-secondary transition-all duration-300")
        result_label = ui.label("").classes("text-lg mt-4 text-center tracking-wide")

    # Second Card: Kelvin Converter
    with ui.card().classes("w-100 p-6 shadow-xl rounded-xl bg-blue-50 border border-gray-200"): 
        ui.label("Kelvin Temperature Converter").classes("text-2xl font-bold text-secondary mb-4 underline")
        kelvin_input = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded bg-gray-50")
        kelvin_conversion_type = ui.radio(["Celsius to Kelvin", "Fahrenheit to Kelvin"], value="Celsius to Kelvin").classes("mb-4")
        kelvin_convert_button = ui.button("Convert to Kelvin", on_click=convert_kelvin).classes("text-white font-bold py-2 px-4 rounded bg-primary hover:bg-secondary transition-all duration-300")
        kelvin_result_label = ui.label("").classes("text-lg mt-4 text-center tracking-wide")

ui.run()
