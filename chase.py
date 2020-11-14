#!/usr/bin/env python3

# Light each LED in sequence, and repeat.

import opc, time
import settings

numLEDs = 512
client = opc.Client(settings.address)

while True:
	for i in range(numLEDs):
		pixels = [ (0,0,0) ] * numLEDs
		pixels[i] = (255, i/2, 255)
		client.put_pixels(pixels)
		time.sleep(0.1)
