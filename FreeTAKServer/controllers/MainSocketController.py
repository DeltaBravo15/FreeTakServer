#######################################################
# 
# MainSocketController.py
# Python implementation of the Class MainSocketController
# Generated by Enterprise Architect
# Created on:      21-May-2020 12:23:05 PM
# Original author: Natha Paquette
# 
#######################################################
from model.MainSocket import MainSocket
import socket

class MainSocketController:
    def __init__(self):  
        self.m_MainSocket = MainSocket()

    def changeIP(self, IP):
        self.m_MainSocket.ip = IP

    def changePort(self, port):
        self.m_MainSocket.port = port

    def createSocket(self):
        self.m_MainSocket.sock = socket.socket(self.m_MainSocket.socketAF, self.m_MainSocket.socketSTREAM)
        self.m_MainSocket.sock.setsockopt(self.m_MainSocket.solSock, self.m_MainSocket.soReuseAddr, self.m_MainSocket.sockProto)
        self.m_MainSocket.sock.bind((self.m_MainSocket.ip, self.m_MainSocket.port))
        return self.m_MainSocket.sock