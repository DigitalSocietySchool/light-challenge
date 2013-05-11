import serial
import pyhue


SEPARATOR = ';'
sp = lambda x: list(map(int, x.split(SEPARATOR)))

bridge = pyhue.Bridge('145.28.47.48', 'lightchallenge')
light = bridge.lights[1]
ser = serial.Serial('COM13', 9600)
last_bri = None
last_hue = None

def process_line(serial_line):
    line = serial_line.strip()
    photo_value, pir_value = sp(line)
    bri = int((photo_value - 400) * 255 / 600)
    hue = 25500 if pir_value else 12750
    return bri, hue

while True:
    try:
        bri, hue = process_line(ser.readline())
        if bri != last_bri or hue != last_hue:
            light.set_state({"bri":bri, "hue":hue})
            last_bri, last_hue = bri, hue
    except ValueError:
        print("Not integer value")
        continue
    except KeyboardInterrupt:
        print("Closing the serial port")
        ser.close()
        break
