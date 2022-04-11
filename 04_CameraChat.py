from vidstream import CameraClient
from vidstream import StreamingServer
import threading
import time 

Pc1 = StreamingServer('Your 1st Local IP', 8090)
#For Know Local IP Address of Your Local Pc ---> ifconfig
Pc2 = CameraClient('Your 2nd Local IP', 9090)
#Your 2nd Local IP Address Of Your Pc ---> ifconfig

firstPc = threading.Thread(target=Pc1.start_server)
firstPc.start() #Here We Handle Thread Using Thread Concept...

time.sleep(3) # Here we Sleep Program For 3 Second

secondPc = threading.Thread(target=Pc2.start_server)
secondPc.start()

while input("") != "STOP":
    continue

Pc1.stop_server()
Pc2.stop_server()

#Run Both Script in Both Pc But Here We Swap IP Address in Scripts 🥱

