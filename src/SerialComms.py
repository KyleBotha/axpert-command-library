import serial
#!Establish Connection----
PORT = "COM4"
baud = 2400
isConnected = False
try:
    ser = serial.Serial(PORT, baudrate=baud, timeout=1)
    isConnected = True
    print("Serial connection established")
except:
    print("Serial connection failed")
#!------------------------

user_command = input()


#!Command Calculation Function
def calculate_command(command):
    QPIGS_COMMAND = [0x51, 0x50, 0x49, 0x47, 0x53, 0xB7, 0xA9, 0x0D]
    return QPIGS_COMMAND
#!------------------------

#!Send Command Function


def send_command(command):
    ser.write(serial.to_bytes(calculate_command(command)))
    response_bytes = ser.readline()
    response_decoded = response_bytes.decode("ISO-8859-1")
    if (user_command == "QPIGS"):
        response_parsed = response_decoded[1:-1]
        response = response_parsed.split()
        return parse_qpigs(response)
    else:

        return "Invalid Command"


def print_qpigs(processed_command):
    print('\n'.join(str(x) for x in processed_command))
#!------------------------

#!Multiplier Function


def multiplier(value, multiplier):
    val = float(value)
    calc = val*multiplier
    return str(calc)
#!-----------------------


#!QPIGS Parser Function
def parse_qpigs(response):
    qpigs_params = [
        f"Grid voltage = {response[0]}V",
        f"Grid frequency = {response[1]}Hz",
        f"AC output voltage = {response[2]}V",
        f"AC output frequency = {response[3]}Hz",
        f"AC output apparent power = {multiplier(response[4], 1)}VA",
        f"AC output active power = {multiplier(response[5], 1)}VA",
        f"Output load percent  = {multiplier(response[6], 1)}%",
        f"BUS voltage = {response[7]}V",
        f"Battery voltage = {response[8]}V",
        f"Battery charging current = {response[9]}A",
        f"Battery capacity = {multiplier(response[10], 1)}%",
        f"Inverter heat sink temperature = {multiplier(response[11], 1)}{chr(176)}C",
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
#!-----------------------


print_qpigs(send_command(user_command))
