import random
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[SERVIDOR] Recebeu requisição: {self.path}")
        print(f"[SERVIDOR] {self.client_address} -> {self.path}")
        match self.path:
            case '/moeda':
                result = random.choice(["Cara", "Coroa"])
            case '/dado':
                result = random.randint(1, 6)
            case _:
                print('Invalid Option.')

        print(f"[SERVIDOR] Respondendo com: {resultado}")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(str(resultado).encode())

def run():
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Servidor rodando na porta 8000...")
    server.serve_forever()

if __name__ == "__main__":
    run()