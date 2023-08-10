from PyQt5 import QtCore, QtWidgets, QtSerialPort

"""""
class Com(QtSerialPort.QSerialPort):
    def print(self):
        print(1)

"""""


class Com():
    serial = QtSerialPort.QSerialPort()
    serial.setPortName("/dev/ttyACM0")
    serial.setBaudRate(9600)

    def open1(self):
        try:
            self.serial.open()
            print(self.serial.isOpen())
        except:
            print(f"Cant opnet {self.serial.portName()}")

    @classmethod
    def read(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            return text

    @classmethod
    def send(self, data):
        self.serial.write(data)
