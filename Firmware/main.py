import board
import digitalio
import time

rows = [board.GP0, board.GP1, board.GP2, board.GP3]
cols = [board.GP4, board.GP5, board.GP8, board.GP9]

row_pins = []
col_pins = []

for r in rows:
    pin = digitalio.DigitalInOut(r)
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = True
    row_pins.append(pin)

for c in cols:
    pin = digitalio.DigitalInOut(c)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    col_pins.append(pin)

while True:
    for i, r in enumerate(row_pins):
        r.value = False
        for j, c in enumerate(col_pins):
            if not c.value:
                print("Pressed:", i, j)
        r.value = True
    time.sleep(0.1)
