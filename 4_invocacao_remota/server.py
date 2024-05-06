from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8005),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def adder_function(x, y):
        print(f'Somando {x} com {y}: {x + y}')
        return x + y
    server.register_function(adder_function, 'add')

    def multiplier_function(x, y):
        print(f'Multiplicando {x} com {y}: {x * y}')
        return x * y
    server.register_function(multiplier_function, 'mul')

    def power_function(x, y):
        print(f'Elevando {x} a {y}: {x ** y}')
        return x ** y
    server.register_function(power_function, 'pow')

    def division_function(x, y):
        print(f'Dividindo {x} por {y}: {x / y}')
        return x / y
    server.register_function(division_function, 'div')

    def subtraction_function(x, y):
        print(f'Subtraindo {x} de {y}: {x - y}')
        return x - y
    server.register_function(subtraction_function, 'sub')

    server.serve_forever()