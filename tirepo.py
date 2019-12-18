import http.server
import socketserver

port = 8080
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",port), handler)
print("tirepo server started at port " + port + ". Type localhost:" + port + " to take a look")
httpd.serve_forever()
