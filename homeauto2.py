from machine import UART, Pin
import time

bt = UART(0, 9600)
L1 = Pin(6, Pin.OUT)
L2 = Pin(7, Pin.OUT)

while True:
    try:
        br = bt.readline().decode().strip()

        # Fan control
        if "turn on the fan" in br or "on the fan" in br or "activate the fan" in br or "start the fan" in br or "switch on the fan" in br or "fan on" in br:
            L1.value(0)
        elif "turn off the fan" in br or "off the fan" in br or "deactivate the fan" in br or "stop the fan" in br or "switch off the fan" in br or "fan off" in br:
            L1.value(1)

        # Light control
        elif "turn on the light" in br or "on the light" in br or "activate the light" in br or "start the light" in br or "switch on the light" in br or "light on" in br:
            L2.value(0)
        elif "turn off the light" in br or "off the light" in br or "deactivate the light" in br or "stop the light" in br or "switch off the light" in br or "light off" in br:
            L2.value(1)

        # Control both fan and light
        elif "turn off both" in br or "switch off both" in br or "deactivate both" in br or "turn off fan and light" in br or "off light fan" in br or "off fan light" in br or "turn off light and fan" in br:
            L1.value(1)
            L2.value(1)
        elif "turn on both" in br or "switch on both" in br or "activate both" in br or "turn on fan and light" in br or "on light fan" in br or "on fan light" in br or "turn on light and fan" in br:
            L1.value(0)
            L2.value(0)

        # Timer for light control
        elif "turn off lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(1)
        elif "deactivate lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(1)
        elif "off lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(1)
        elif "turn on lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(0)
        elif "activate lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(0)
        elif "on lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(0)

        # Timer for fan control
        elif "turn off fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(1)
        elif "deactivate fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(1)
        elif "off fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(1)
        elif "turn on fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(0)
        elif "activate fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(0)
        elif "on fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(0)
        

    except:
        time.sleep(1)
