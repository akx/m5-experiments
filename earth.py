from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x000000)
earth0 = unit.get(unit.EARTH, unit.PORTA)


ev = None


def buttonA_wasPressed():
    global ev
    pass


btnA.wasPressed(buttonA_wasPressed)


lcd.clear()
lcd.setBrightness(0)
while True:
    ev = earth0.analogValue
    lcd.print(ev, 0, 0, 0xFFFFFF)
    lcd.print((axp.getChargeI()), 0, 25, 0xFFCC66)
    if ev < 25:
        M5Led.on()
    else:
        M5Led.off()
    wait(1)
    wait_ms(2)
