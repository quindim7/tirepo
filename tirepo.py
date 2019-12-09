import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

def start(port):
    with socketserver.TCPServer(("", port), Handler) as tirepo:
        tirepo.serve_forever()

print("Tirepo server listening on IP localhost and port " + start.port + " started (Type localhost:" + start.port + " in your browser to load your Tirepo server)")
start(7134)
