import crc16


class Command:
    def __init__(self, command):
        self.command = command
        self.hex_command = []
        self.command_split = [char for char in command]
        self.command_encoded = command.encode()
        self.crc_string = hex(crc16.crc16xmodem(self.command_encoded))
        self.crc_int = int(self.crc_string, 16)
        self.crc_high, self.crc_low = divmod(self.crc_int, 0x100)

    def convert_tohex(self):
        hex_list = []
        for char in self.command_split:
            char = ord(char)
            hex_list.append(char)
            self.hex_command.append(char)
        return hex_list

    def append_crc(self):
        self.hex_command.append(self.crc_high)
        self.hex_command.append(self.crc_low)

    def append_delim(self):
        self.hex_command.append(13)

    def build_command(self):
        self.convert_tohex()
        self.append_crc()
        self.append_delim()
