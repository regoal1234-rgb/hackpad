import busio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306
from pins import OLED_SDA, OLED_SCL

displayio.release_displays()

i2c = busio.I2C(OLED_SCL, OLED_SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = SSD1306(display_bus, width=128, height=32)

group = displayio.Group()
display.root_group = group

layer_label = label.Label(terminalio.FONT, text="Layer: BASE", x=0, y=12)
group.append(layer_label)

def update_oled(layer):
    names = ["BASE", "FN", "MEDIA"]
    layer_label.text = f"Layer: {names[layer]}"