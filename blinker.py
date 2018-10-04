#!/usr/bin/python3.5
import os
import time

while True:
	os.system("xset dpms force off")
	time.sleep(20)
	os.system("xset dpms force on")
	os.system('espeak "Open You eyes"')
	time.sleep(300)
