import http.server
import socketserver

# Set the port to 8000 as required by the assignment
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# This line lets you restart the server instantly without port errors
socketserver.TCPServer.allow_reuse_address = True

print(f"Serving HTTP on http://127.0.0.1:{PORT}...")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped manually.")