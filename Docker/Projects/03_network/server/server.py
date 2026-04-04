from http.server import BaseHTTPRequestHandler, HTTPServer
import random

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[SERVIDOR] Recebeu requisição: {self.path}")
        print(f"[SERVIDOR] {self.client_address} -> {self.path}")
        if self.path == "/moeda":
            resultado = random.choice(["Cara", "Coroa"])
        elif self.path == "/dado":
            resultado = random.randint(1, 6)
        else:
            resultado = "Rota inválida"

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