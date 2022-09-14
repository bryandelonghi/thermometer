micro_temp = 0

def on_button_pressed_a():
    global micro_temp
    micro_temp = input.temperature()
    basic.show_number(micro_temp)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
