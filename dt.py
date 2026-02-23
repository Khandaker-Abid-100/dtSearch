from http.server import HTTPServer, BaseHTTPRequestHandler
import os, glob

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/open-dtsearch":
            # Search for dtSearch in multiple locations
            paths_to_check = [
                os.path.expanduser(r"~\Desktop\*dtSearch*.lnk"),
                r"C:\Program Files\dtSearch*\dtSearch*.exe",
                r"C:\Program Files (x86)\dtSearch*\dtSearch*.exe"
            ]

            for pattern in paths_to_check:
                matches = glob.glob(pattern)
                if matches:
                    os.startfile(matches[0])
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"dtSearch opened!")
                    return

            # If not found
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"dtSearch not found!")
        else:
            self.send_response(404)
            self.end_headers()

server_address = ('', 8000)  # localhost:8000
httpd = HTTPServer(server_address, Handler)
print("Server running on http://localhost:8000")
httpd.serve_forever()