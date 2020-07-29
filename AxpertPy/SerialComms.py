import serial


class Connection:
    def __init__(self, port, baud, command):
        self.isConnected = False
        self.port = port
        self.baud = baud
        self.command = command

    def establish_connection(self):
        try:
            self.ser = serial.Serial(self.port, baudrate=self.baud, timeout=1)
            self.isConnected = True
            print("Serial connection established")
        except:
            print("Serial connection failed")

    def send_command(self):
        if (self.isConnected == True):
            self.ser.write(serial.to_bytes(self.command))
            response_bytes = self.ser.readline()
            response_decoded = response_bytes.decode("ISO-8859-1")
            response_parsed = response_decoded[1:-1]
            response = response_parsed.split()
            return response
        else:
            return "Cannot send command because there is no connection established"
