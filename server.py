
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.parse import urlparse, parse_qs
import json

HOST = "127.0.0.1"
PORT = 8000
API = "https://price.hns.dev"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/latest":
            params = parse_qs(parsed.query)
            currency = params.get("currency", ["usd"])[0]
            api_url = f"{API}/latest?currency={currency}"

        elif parsed.path == "/api/historical":
            params = parse_qs(parsed.query)
            date = params.get("from", [""])[0]
            currency = params.get("currency", ["usd"])[0]

            if (
                len(date) != 10
                or date[4] != "-"
                or date[7] != "-"
                or currency not in ("usd", "btc")
            ):
                self.send_error(400, "Invalid date or currency")
                return

            api_url = f"{API}/historical?from={date}&currency={currency}"

        else:
            # Serve the existing website and its assets.
            if parsed.path == "/":
                self.path = "/index.html"
            return super().do_GET()

        if currency not in ("usd", "btc"):
            self.send_error(400, "Unsupported currency")
            return

        try:
            request = Request(
                api_url,
                headers={"User-Agent": "HNS-Price-Calculator/1.0"}
            )

            with urlopen(request, timeout=15) as response:
                body = response.read()

            # Validate JSON for historical data.
            if parsed.path == "/api/historical":
                json.loads(body)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "null")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        except Exception as exc:
            print("Upstream API error:", exc)
            self.send_error(502, "Unable to retrieve HNS prices")

    def log_message(self, fmt, *args):
        print(fmt % args)


# Serve static website files from this project directory.
import os
from http.server import SimpleHTTPRequestHandler

class WebsiteHandler(Handler, SimpleHTTPRequestHandler):
    pass


print(f"Open http://{HOST}:{PORT}")
HTTPServer((HOST, PORT), WebsiteHandler).serve_forever()
