from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

from pins import ROW_PINS, COL_PINS
from keymap import keymap
from encoder import encoder_handler
from oled import update_oled

keyboard = KMKKeyboard()

keyboard.row_pins = ROW_PINS
keyboard.col_pins = COL_PINS
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.encoder = encoder_handler
keyboard.keymap = keymap

def after_layer_change(keyboard):
    update_oled(keyboard.active_layers[0])

keyboard.after_layer_change = after_layer_change

if __name__ == "__main__":
    keyboard.go()