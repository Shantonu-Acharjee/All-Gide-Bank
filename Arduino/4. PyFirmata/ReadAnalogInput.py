from pyfirmata import ArduinoMega
import time
port = 'COM3'

board = ArduinoMega(port)

pin = board.get_pin('a:0:1')
