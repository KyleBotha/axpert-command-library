class Parser:
    def __init__(self, response, command):
        self.response = response
        self.command = command
        self.command_list = ["QPIGS"]
        self.isCommand = self.identify_command()

    def identify_command(self):
        if(self.command_list.count(self.command) > 0):
            self.isCommand = True
            return True

    def parse_command(self):
        if(self.identify_command()):
            if(self.command == "QPIGS"):
                return self.parse_qpigs(self.response)
        else:
            return "Command does not exist"

    def multiplier(self, value, multiplier):
        val = float(value)
        calc = val*multiplier
        return str(calc)

    def parse_qpigs(self, response):
        qpigs_params = [
            f"Grid voltage = {response[0]}V",
            f"Grid frequency = {response[1]}Hz",
            f"AC output voltage = {response[2]}V",
            f"AC output frequency = {response[3]}Hz",
            f"AC output apparent power = {self.multiplier(response[4], 1)}VA",
            f"AC output active power = {self.multiplier(response[5], 1)}VA",
            f"Output load percent  = {self.multiplier(response[6], 1)}%",
            f"BUS voltage = {response[7]}V",
            f"Battery voltage = {response[8]}V",
            f"Battery charging current = {response[9]}A",
            f"Battery capacity = {self.multiplier(response[10], 1)}%",
            f"Inverter heat sink temperature = {self.multiplier(response[11], 1)}{chr(176)}C",
            f"PV Input current 1 (PV Input current for battery. ) = {response[12]}",
            f"PV Input voltage 1 = {response[13]}V",
            f"Battery voltage from SCC 1 = {response[14]}V",
            f"Battery discharge current = {response[15]}A",
            f"Device Status = {response[16]} << SEE PROTOCOL MANUAL FOR ",
            f"Battery voltage offset for fans on = {response[17]}mV",
            f"EEPROM version = {response[18]}",
            f"PV Charging power 1 = {response[19]}Watt",
            f"Device status = {response[20]}"]
        return qpigs_params
