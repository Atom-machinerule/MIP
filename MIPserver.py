#!/usr/bin/python
import time
#import serial
import cherrypy
#import os.path

#ser = serial.Serial('/dev/ttyAMA0', 9600)
time.sleep(0.1)

global D1
D1 = 1
global D2
D2 = 1
global D3
D3 = 1
global D4
D4 = 1
global D5
D5 = 1
global D6
D6 = 1

print "Starting...." 

class ServerLed(object):

    '''BUtton state 1 (on) or 0 (off)'''
    button_switch= 0 #Initial LED on
    
    def index(self,switch='',refresh=""): 

	global D1
	global D2 
	global D3
	global D4
	global D5 
	global D6


        if switch:
            self.button_switch = int(switch)
            print "New button state %d" % self.button_switch
            D1 = 1
            D2 = 1
            D3 = 1
            D4 = 1
            D5 = 1
            D6 = 1

	if self.button_switch == 1:
	    print "SWITCH = 1"
	    D1 = 0
	    ser.write('f*')
	elif self.button_switch == 2:
	    print "SWITCH = 2"
	    D2 = 0
	    ser.write('l*')
	elif self.button_switch == 3:
	    print "SWITCH = 3"
	    D3 = 0
	    ser.write('r*')
	elif self.button_switch == 4:
	    print "SWITCH = 4"
	    D4 = 0
	    ser.write('s*')
	elif self.button_switch == 5:
	    print "SWITCH = 5"
	    D5 = 0
	    ser.write('b*')

        #reset buttons
	elif self.button_switch == 1:
	    print "SWITCH = 1"
            D2 = 1
            D3 = 1
            D4 = 1
            D5 = 1
            D6 = 1
            return html
        else:
            duty = 0 #disable

        print D1
        print D2
        print D3
        print D4
        print D5
        print D6

        #read HTML template from file
        html = open('/home/pi/MIP/MIP.html','r').read()


        if D1 == 0:
            html = html.replace('f.png', 'ff.png')
        if D2 == 0:
            html = html.replace('l.png', 'll.png')
        if D3 == 0:
            html = html.replace('s.png', 'ss.png')
        if D4 == 0:
            html = html.replace('r.png', 'rr.png')
        if D5 == 0:
            html = html.replace('b.png', 'bb.png')
        if D6 == 0:
            html = html.replace('r.png', 'rr.png')

        return html

    index.exposed = True

#configuration
conf = {
        'global' : { 
            'server.socket_host': '0.0.0.0', #0.0.0.0 or specific IP
            'server.socket_port': 7070 #server port
        },

        '/images': { #images served as static files
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '/home/pi/MIP/images'
        },

        '/favicon.ico': {  #favorite icon
            'tools.staticfile.on': True,  
            'tools.staticfile.filename': '/home/pi/MIP/images/MIP.ico'
        }
    }

cherrypy.quickstart(ServerLed(), config=conf)
