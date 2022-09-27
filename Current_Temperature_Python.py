current_temperature = 0
# Created By: Alex.C
# Created On:2022/09/27
# This block of code tells the microbit to flash the temperature number on the LED's.

def on_forever():
    global current_temperature
    current_temperature = input.temperature()
    basic.show_number(current_temperature)
    basic.pause(500)
    basic.clear_screen()
basic.forever(on_forever)
