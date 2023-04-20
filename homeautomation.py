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
            L2.value(1)
        elif "turn off the fan" in br or "off the fan" in br or "deactivate the fan" in br or "stop the fan" in br or "switch off the fan" in br or "fan off" in br:
            L2.value(0)

        # Light control
        elif "turn on the light" in br or "on the light" in br or "activate the light" in br or "start the light" in br or "switch on the light" in br or "light on" in br:
            L1.value(1)
        elif "turn off the light" in br or "off the light" in br or "deactivate the light" in br or "stop the light" in br or "switch off the light" in br or "light off" in br:
            L1.value(0)

        # Control both fan and light
        elif "turn off both" in br or "switch off both" in br or "deactivate both" in br or "turn off fan and light" in br or "off light fan" in br or "off fan light" in br or "turn off light and fan" in br:
            L1.value(0)
            L2.value(0)
        elif "turn on both" in br or "switch on both" in br or "activate both" in br or "turn on fan and light" in br or "on light fan" in br or "on fan light" in br or "turn on light and fan" in br:
            L1.value(1)
            L2.value(1)

        # Timer for light control
        elif "turn off the lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(0)
        elif "deactivate the lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(0)
        elif "off the lights in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L1.value(0)

        # Timer for fan control
        elif "turn off the fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(0)
        elif "deactivate the fan in" in br:
            seconds = int(br.split("in")[1].strip())
            time.sleep(seconds)
            L2.value(0)

        # Turn off the lights at a specific time
        elif "turn off the lights at" in br:
            time_str = br.split("at")[1].strip()
            time_obj = time.strptime(time_str, "%I:%M %p")
            current_time = time.localtime(time.time())
            if current_time.tm_hour == time_obj.tm_hour and current_time.tm_min == time_obj.tm_min:
                L1.value(0)

            # Turn off the fan at a specific time
        elif "turn off the fan at" in br:
         time_str = br.split("at")[1].strip()
        time_obj = time.strptime(time_str, "%I:%M %p")
        current_time = time.localtime(time.time())
        if current_time.tm_hour == time_obj.tm_hour and current_time.tm_min == time_obj.tm_min:
            L2.value(0)

    # Turn on the lights at a specific time
        elif "turn on the lights at" in br:
         time_str = br.split("at")[1].strip()
        time_obj = time.strptime(time_str, "%I:%M %p")
        current_time = time.localtime(time.time())
        if current_time.tm_hour == time_obj.tm_hour and current_time.tm_min == time_obj.tm_min:
            L1.value(1)

    # Turn on the fan at a specific time
        elif "turn on the fan at" in br:
         time_str = br.split("at")[1].strip()
        time_obj = time.strptime(time_str, "%I:%M %p")
        current_time = time.localtime(time.time())
        if current_time.tm_hour == time_obj.tm_hour and current_time.tm_min == time_obj.tm_min:
            L2.value(1)

        else:
        # Print unrecognized commands
         print("Unrecognized command: ", br)

    except Exception as e:
     print("Error: ", e)

