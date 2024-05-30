from pymodbus.client import ModbusTcpClient     #pip install pymodbus
from pymodbus.exceptions import ModbusException
from tabulate import tabulate                   #pip install tabulate


def verificarConexao(cliente):
    return cliente.is_socket_open()             #Retorna True quando a conexão estiver aberta

def encerrarConexao(cliente):
    cliente.close()

def conectar(ip_clp: str, porta: int):
    cliente=ModbusTcpClient(host=ip_clp, port=porta)
    print(f'Porta {porta}: ', end='')
    cliente.connect()
    if verificarConexao(cliente):
        print(f'Conexão estabelecida com sucesso.')
        
    return cliente

def imprimirClientes(CLPs_dados, qtd_CLPs):
    tabela=[['', 'Nome CLP', 'IP', 'Porta', 'Status']]
    for i in range(1, qtd_CLPs+1):
        tabela_linha=[i]
        clp=CLPs_dados[i]
        tabela_linha.append(clp["nome"])
        tabela_linha.append(clp["ip"])
        tabela_linha.append(clp["porta"])
        if clp["status"]: 
            tabela_linha.append('Conectado')
        else:
            tabela_linha.append('Desconectado')
        tabela.append(tabela_linha)
    print(tabulate(tabela, headers='firstrow', tablefmt='pretty'))

def lerValorCLP(clp):
    a=clp.read_holding_registers(address=0, count=3)
    return a.registers

def imprimirCLP(clp_dados, clp):
    valores=lerValorCLP(clp)
    temperatura=valores[0]
    vazao=valores[1]
    pressao=valores[2]
    tabela=[
        ['Temperatura', str(temperatura)+' °C'],
        ['Vazão', str(vazao)+' m³/s'],
        ['Pressão', str(pressao)+' Pa']
    ]
    print(f"{clp_dados['nome']}")
    print(f"IP: {clp_dados['ip']}")
    print(f"Porta: {clp_dados['porta']}")
    print(tabulate(tabela, tablefmt='pretty', numalign='left', stralign='left'))