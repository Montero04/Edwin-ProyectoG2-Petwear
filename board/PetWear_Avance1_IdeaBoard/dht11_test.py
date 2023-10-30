# Codigo para DHT11
# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
# Modificado por Jefry Valverde y Gabriela Urbina
# Universidad CENFOTEC
#
# SPDX-License-Identifier: MIT

import time

import adafruit_dht
import board

dht = adafruit_dht.DHT11(board.IO27)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)