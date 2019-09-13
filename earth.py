from m5stack import *
from m5ui import *
import unit

earth0 = unit.get(unit.EARTH, unit.PORTA)
dry_resistance_threshold = 0.5
lcd.clear()
lcd.setBrightness(200)
lcd.font(lcd.FONT_Ubuntu)  # , 0, False)
while True:
    ev = earth0.analogValue / 1024
    lcd.clear()
    lcd.print("%d%%" % int(ev * 100), 10, 10, 0xFFFFFF)
    if ev > 0 and ev < dry_resistance_threshold:
        M5Led.on()
        speaker.tone(1600, 20)
        wait_ms(60)
    else:
        M5Led.off()
    wait(1)
