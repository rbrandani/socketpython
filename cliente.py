# Echo client program
import socket #biblioteca tcp
import RPi.GPIO as gpio #biblioteca IO
import time #biblioteca tempo

gpio.setmode(gpio.BCM) #escolhendo o "nome" do pino, poderia ser o numero gpio.board
gpio.setup(4,gpio.OUT) #led
gpio.setup(27,gpio.IN, gpio.PUD_DOWN) #botao

HOST = '192.168.0.108'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        if (gpio.input(27)==gpio.HIGH):
            s.sendall(b'ON')
        else:
            s.sendall(b'OFF')
        data = s.recv(1024)
        if data.decode("utf-8") == "ON":
            gpio.output(4, gpio.HIGH)
            print('LIGADO')
        else:
            gpio.output(4, gpio.LOW)
            print('DESLIGADO')
        time.sleep(0.5)    
        