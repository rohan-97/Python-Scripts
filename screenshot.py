#!/usr/bin/python3.5
import pyscreenshot
import time
while True:
    pyscreenshot.grab_to_file("/home/rohan/Downloads/Kachra/aspire/" + str(time.ctime()).replace(" ", "_") + ".jpeg")
    time.sleep(30)
