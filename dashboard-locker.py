from tkinter import *
from paho.mqtt import client as mqtt_client

import random, json

broker 		= 'localhost'
port 		= 1883
topic 		= 'proyek'
client_id 	= f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

import json
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        _data = json.loads(msg.payload.decode())
        stats = str(_data["Parameters"]["status"])
        
        if (stats == 0):
            square.create_rectangle(143, 89, 443, 239, fill = '#91F086', outline = 'black')
        else :
            square.create_rectangle(143, 89, 443, 239, fill = '#FF5252', outline = 'black')

    client.subscribe(topic)
    client.on_message = on_message

window = Tk()

# Title bar
window.title('Smart Locker Dashboard')
window.geometry('1366x768')
window.resizable(False, True)
window.configure(bg = 'white')

# Banner
canvas = Canvas(window, width = 1366, height = 200)
canvas.place(x = 0, y = 0)
img = PhotoImage(file = 'banner.png')
canvas.create_image(0, 0, anchor = NW, image = img)

# Square
square = Canvas(window, width=1366, height=568)
square.place(x = 0, y = 200)

# Baris 1 ( x1, y1, x2, y2 )
square.create_rectangle(143, 89, 443, 239, fill = '#91F086', outline = 'black')
square.create_rectangle(533, 89, 833, 239, fill = '#91F086', outline = 'black')
square.create_rectangle(923, 89, 1223, 239, fill = '#FF5252', outline = 'black')

# Baris 2 ( x1, y1, x2, y2 )
square.create_rectangle(143, 329, 443, 479, fill = '#91F086', outline = 'black')
square.create_rectangle(533, 329, 833, 479, fill = '#FF5252', outline = 'black')
square.create_rectangle(923, 329, 1223, 479, fill = '#91F086', outline = 'black')

client = connect_mqtt()
subscribe(client)
client.loop_start()
window.mainloop()
client.loop_stop()