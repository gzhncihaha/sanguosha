import socket  
import threading  
import getpass  
import time
from Room import * 

inString = bytes('', encoding = "utf8")  
inStringList = []
outString = ''  

def DealOut(s):  
    computername=socket.gethostname()
    global nick, outString  
    while True:  
        if outString != '':
            print("send:"+outString)
            s.sendall(bytes(outString, encoding = "utf8"))
            outString = ''  
  
def DealIn(s):  
    global inString, inStringList  
    while True:  
        inString = s.recv(1024)
        inStringList.append(str(inString, encoding = "utf8"))
        if inString != '':
            print("inString:"+str(inString, encoding="utf8"))

class ToServer:
   # def __init__(self, ip, port):
        #nick = getpass.getuser()
        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        #sock.connect((ip, port))

        #thin = threading.Thread(target = DealIn, args = (sock,))#开辟一个读入的线程  
        #thin.start()  
        #thout = threading.Thread(target = DealOut, args = (sock,))#开辟一个写出的线程  
        #thout.start()  
    def initialize(self, ip, port):
        #self.nick = getpass.getuser()
        self.nick = 's' + str(randint(0, 2147483647))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.connect((ip, port))

        thin = threading.Thread(target = DealIn, args = (sock,))#开辟一个读入的线程  
        thin.start()  
        thout = threading.Thread(target = DealOut, args = (sock,))#开辟一个写出的线程  
        thout.start()  
    def sendStr(self, s):
        global outString
        outString = s
    def recvStr(self):
        global inString
        temp = inString
        inString = bytes('None', encoding = "utf8") 
        #time.sleep(0.5)
        return str(temp, encoding = "utf8")
    def recvStrList(self):
        global inStringList
        temp = inStringList
        inStringList = []
        return temp

#trans = ToServer("192.168.19.1", 5001)
communicater = ToServer()


  