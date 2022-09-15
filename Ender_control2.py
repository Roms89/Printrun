#to send a file of gcode to the printer
import pyximport
pyximport.install()
from printrun.printcore import printcore
from printrun import gcoder
import time
#import keyboard
#import freeport
#import xmlrpc.client


def set_up(port, gcode_file):
    p = printcore(port, 115200)
    p.connect(port, 115200)
    gcode1 = [i.strip() for i in open(gcode_file)]
    gcode1 = gcoder.LightGCode(gcode1)
    p_p = [p, gcode1, port]
    while not p_p[0].online:
      time.sleep(0.1)
    p_p[0].pause()
    p_p[0].resume()
    p_p[0].disconnect()
    return p_p

def connect(p):
    p[0].connect(p[2], 115200)

def ender_print(p):
    p[0].startprint(p[1])

#def E_stop(p1, p2):
#    p1[0].pause(), p2[0].pause()


def Ender_main():
    port_1 = str(input("Enter port for pump_1: "))
    gcode1 = str(input("Enter filename for gcode: "))
    port_2 = str(input("Enter port for pump_2: "))
    gcode2 = str(input("Enter filename for gcode: "))

    p1 = set_up(port_1, gcode1)
    p2 = set_up(port_2, gcode2)

    connect(p1)
    connect(p2)

    count = "False"

    while count == "False": 
        status_p = str(input("Start print? Y/N "))
        if status_p == "Y":
            ender_print(p1), ender_print(p2)
        elif status_p == "N":
            p1[0].disconnect(), p2[0].disconnect()
            break
        else:
            print("Please enter 'Y' or 'N'.")

count = "False"

while count == "False":
    new_run = str(input("New run? Y/N "))
    if new_run == "Y":
        Ender_main()
    elif new_run == "N":
        break
    else:
        print("Please enter 'Y' or 'N'.")              

#rpc = xmlrpc.client.ServerProxy('http://localhost:8000')

#if keyboard.is_pressed("q"):
#    E_stop(p1, p2)
