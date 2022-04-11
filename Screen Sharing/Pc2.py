from vidstream import ScreenShareClient
import threading

Pc2 = ScreenShareClient('Your 2ND Local IP', 9999)

firstPc = threading.Thread(target=Pc2.start_stream)
firstPc.start() #Here We Handle Thread Using Thread Concept...

while input("") != 'STOP':
    continue

Pc2.stop_stream()