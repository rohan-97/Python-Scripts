#!/bin/bash
sudo ifconfig wlp2s0 down
echo "wifi band hotay jara vel thamba..."
sleep 2
sudo ifconfig wlp2s0 up
echo "wifi chalu zala..."
