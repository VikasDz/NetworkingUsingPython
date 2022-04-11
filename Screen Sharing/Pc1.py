from vidstream import StreamingServer
import threading

Pc1 = StreamingServer('Your 1st Local IP', 9999)

firstPc = threading.Thread(target=Pc1.start_server)
firstPc.start() #Here We Handle Thread Using Thread Concept...

while input("") != 'STOP':
    continue

Pc1.start_server()
