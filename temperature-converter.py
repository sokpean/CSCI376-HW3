from nicegui import ui

ui.colors(
      primary='#1976d2',
      secondary='#26a69a',
      accent='#9c27b0',
      positive='#84c292',
      negative='#5f648c',
      info='#52b3c7',
      warning='#f2ce6b'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
            if temp == 4.1:
                rickroll.set_visibility(True)
            else:
                rickroll.set_visibility(False)
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
            rickroll.set_visibility(False)
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: this code applies a positive text color
    except ValueError:
        result_label.set_text("Please enter a valid number.") # this code returns a strings after a exception is reach
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: this code applies a negative text color
        rickroll.set_visibility(False)

def convert_kelvin():
    try:
        temp = float(kelvin_input.value)
        if kelvin_conversion_type.value == "Celsius to Kelvin":
            kelvin_result_label.set_text(f"{temp}°C = {temp + 273.15:.2f}K")
            if temp == -273.15:
                end_of_life_video.set_visibility(True)
            else:
                end_of_life_video.set_visibility(False)
        else:
            kelvin_result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9 + 273.15:.2f}K")
            kelvin_result_label.classes("text-lg font-semibold text-info mt-4")
            end_of_life_video.set_visibility(False)
    except ValueError:
        kelvin_result_label.set_text("Please enter a valid number.")
        kelvin_result_label.classes("text-lg font-semibold text-negative mt-4")
        end_of_life_video.set_visibility(False)


with ui.row().classes("w-full justify-center gap-8 mt-10"):

    with ui.card().classes("w-100 p-6 shadow-xl rounded-xl bg-red-50 border border-gray-200"): 
        # w-100: Set element width to be fixed at 100
        # p-6: add 6 units of padding
        # shadow-xl: adds extra-large shadow
        # mx-auto: centers the card horizontally
        # mt-10: adds 10 units of top margins
        # rounded-xl: adds extra-large border radius
        # additions: bg-red-50 -> sets the background color to pink 
        # additions: border-gray-200 -> add a grey border to the background
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 underline")
        # text-2xl: set text size to extra-large
        # font-bold: bold the text
        # text-accent: change text color to accent color
        # mb-4: adds a bottom margins
        # additions: underline -> underlines the Temperature Converter text
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded bg-gray-50")
        # w-full: sets width to 100% of container
        # border: adds defaukt borders
        # rounded: rounds the corners 
        # additions: bg-gray-50 -> change the enter temperature button to a slight grey color differ from pink background
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: set text color to white
        # py-2: adds vertical padding by 2 units
        # px-4: adds horizontal padding by 4 units
        result_label = ui.label("").classes("text-lg mt-4")
        rickroll = ui.image("https://www.todayifoundout.com/wp-content/uploads/2017/11/rick-astley.png")
        rickroll.set_visibility(False)

    with ui.card().classes("w-100 p-6 shadow-xl rounded-xl bg-blue-50 border border-gray-200"): 
        ui.label("Kelvin Temperature Converter").classes("text-2xl font-bold text-accent mb-4 underline")
        kelvin_input = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded bg-gray-50")
        kelvin_conversion_type = ui.radio(["Celsius to Kelvin", "Fahrenheit to Kelvin"], value="Celsius to Kelvin").classes("mb-4")
        kelvin_convert_button = ui.button("Convert", on_click=convert_kelvin).classes("text-white font-bold py-2 px-4 rounded")
        kelvin_result_label = ui.label("").classes("text-lg mt-4")
        end_of_life_video = ui.html('''<iframe src="https://www.youtube.com/embed/TNUDBdv3jWI"></iframe>''')
        end_of_life_video.set_visibility(False)
        ui.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')
        checkbox = ui.checkbox('check me for a surprise')
        ui.label('BOO!').bind_visibility_from(checkbox, 'value') 
        ui.avatar('img:https://ih1.redbubble.net/image.1968248280.0899/st,small,507x507-pad,600x600,f8f8f8.jpg')
ui.run()