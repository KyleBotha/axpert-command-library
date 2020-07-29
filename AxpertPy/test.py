from SerialComms import Connection
from CalculateCommands import Command
from ParseCommands import Parser

command = input("Please enter a command >> ")
qpigs = Command(command)
qpigs.build_command()
Inverter = Connection("COM4", "2400", qpigs.hex_command)
Inverter.establish_connection()
inverter_response = Inverter.send_command()
parser = Parser(inverter_response, command)
parsed_response = parser.parse_command()
print(parsed_response)
