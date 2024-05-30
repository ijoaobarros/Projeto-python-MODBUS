from pymodbus.client import ModbusTcpClient 
import keyboard

def verificarConexao(cliente):
    return cliente.is_socket_open()

cliente=ModbusTcpClient(host='localhost', port=502)
cliente.connect()
print(verificarConexao(cliente))
a=cliente.read_holding_registers(address=0, count=3)
print('Valores: ',a.registers)

while True:
    if keyboard.is_pressed('esc'):
        break

cliente.close()