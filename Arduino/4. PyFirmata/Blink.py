from pyfirmata import ArduinoMega
import time
import keyboard
port = 'COM3'
board = ArduinoMega(port)


while True:
    if keyboard.is_pressed('shift'):
        print('You Pressed Shift Key!') # Press Many time if it's not working
        break
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)