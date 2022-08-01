from vidstream import AudioSender
from vidstream import AudioReceiver

import threading
import socket

# ip = socket.gethostbyname(socket.gethostname())

receiver = AudioReceiver('192.168.254.36', 9999)
receiver_Thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('Other Laptopn IpV4', 5555)
sender_thread = threading.Thread(target=sender.start_stream)

receiver_Thread.start()
sender_thread.start()