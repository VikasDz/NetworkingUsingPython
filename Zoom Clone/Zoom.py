from vidstream import *
import tkinter as tk
import socket
import threading



local_ip = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip, 8888)
receiver = AudioReceiver(local_ip, 1000)

def start_listening():
     p1 = threading.Thread(target=server.start_server)
     p2 = threading.Thread(target=receiver.start_server)
     p1.start()
     p2.start()

def start_Camera():
     camera_Client = CameraClient(Text_target_ip.get(1.0, 'end-1c'), 1111)
     t1 = threading.Thread(target=camera_Client.start_stream)
     t1.start()

def start_Screen_Sharing():
     Screen_Client = ScreenShareClient(Text_target_ip.get(1.0, 'end-1c'), 1111)
     t2 = threading.Thread(target=Screen_Client.start_stream)
     t2.start()


def start_Audio():
     Audio_Sender = Audio_Sender(Text_target_ip.get(1.0, 'end-1c'), 6666)
     t2 = threading.Thread(target=Audio_Sender.start_stream)
     t2.start()


# Gui Setup

window = tk.Tk()
window.title("Zoom Clone")
window.geometry('300x200')


label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

Text_target_ip = tk.Text(window, height=1)
Text_target_ip.pack()


btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_Camera = tk.Button(window, text="Start Camera", width=50, command=start_Camera)
btn_Camera.pack(anchor=tk.CENTER, expand=True)

btn_Screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_Screen_Sharing)
btn_Screen.pack(anchor=tk.CENTER, expand=True)

btn_Audio = tk.Button(window, text="Start Audio", width=50, command=start_Audio)
btn_Audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()