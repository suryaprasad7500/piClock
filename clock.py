from time import strftime
import time
from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)

while True:
    with canvas(device) as draw:
        cur_time = datetime.now().strftime("%H:%M")
        text(draw, (0, 0), cur_time, fill="white", font=proportional(CP437_FONT))
    time.sleep(30)