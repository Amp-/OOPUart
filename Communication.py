from PyQt5 import QtCore, QtWidgets, QtSerialPort

portName = "/dev/ttyACM1"
baudRate = 9600
class Com():
    serial = QtSerialPort.QSerialPort()
    serial.setPortName(portName)
    serial.setBaudRate(baudRate)

    def open1(cls):
        try:
            cls.serial.open()
            print(cls.serial.isOpen())
        except:
            print(f"Cant opnet {cls.serial.portName()}")

    @classmethod
    def read(cls):
        while cls.serial.canReadLine():
            text = cls.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            return text

    @classmethod
    def send(cls, data):
        cls.serial.write(data)
    @classmethod
    def togle(self):
        if not self.serial.isOpen():
            if not self.serial.open(QtCore.QIODevice.ReadWrite):
                return False

    @classmethod
    def close(cls):
        cls.serial.close()