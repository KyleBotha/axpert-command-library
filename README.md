# Axpert Inverter Communication Library

## Dependencies

- pySerial
- crc16
  - _crc16 is ported from C++, so MS C++ 14.00 is required to be installed on device_

## Usage

```
from SerialComms import Connection
from CalculateCommands import Command
from ParseCommands import Parser

#Ask user to enter a command to send to the Axpert Inverter
command = input("Please enter a command >> ")
PORT = input("Please enter the Communication Port i.e. COM4 >> ")


#Initialize Command class
qpigs = Command(command)

#Build the command, converts it from String to a Integer value that can be read by the inverter <command><crc><cr>
qpigs.build_command()

#Initializes the Connection class
Inverter = Connection(PORT, "2400", qpigs.hex_command)

#Establishes the connection to the Communications Port
Inverter.establish_connection()

#Sends the command to the Inverter and retrieves a response
inverter_response = Inverter.send_command()

#Initializes the Parser class
parser = Parser(inverter_response, command)

#Uses the parser to parse the response depending on what command was used
parsed_response = parser.parse_command()

#Prints the final parsed response to the terminal
print(parsed_response)
```
