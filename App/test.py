from SerialComms import Connection
from CalculateCommands import ConvertCommand
from ParseCommands import ParseResponse

#command = [0x51, 0x50, 0x49, 0x47, 0x53, 0xB7, 0xA9, 0x0D]
print("Please enter a command >> ")
command = input()
qpigs = ConvertCommand(command)
qpigs.build_command()
Inverter = Connection("COM4", "2400", qpigs.hex_command)
Inverter.establish_connection()
inverter_response = Inverter.send_command()
parser = ParseResponse(inverter_response, command)
parsed_response = parser.parse_command()
print(parsed_response)
