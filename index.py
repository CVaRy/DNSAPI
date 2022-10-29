import selenium
import requests
import json
import dns
import socket
import dns.resolver
from flask import Flask, jsonify
from flask import make_response
from flask import request
import dns.reversename
from ipwhois import IPWhois
from pprint import pprint
app = Flask(__name__)



@app.route("/api/dnsflush/cloudflare", methods=["POST"])
def cloudflareapi():
    data=request.json
    api_url="https://1.1.1.1/api/v1/purge"
    a = requests.post(url=api_url,data=data)
    return a.text

@app.route("/api/dns",methods=["POST"])
def dns_checker():
    data=request.json
    records = []
    if data["record"] == "PTR":
        domain_ip = socket.gethostbyname(data["domain"])
        result_ptr=socket.gethostbyaddr(domain_ip)
        records.append(result_ptr[0])
        return records
    result = dns.resolver.resolve(data["domain"], data["record"])
    for IPval in result:
        records.append(IPval.to_text())
    return records

@app.route("/api", methods=["GET"])
def get():
    return {
        "msg":"DNS TOOLS API v0.1 Alfa"
    }

@app.route("/api/ipwhois",methods=["POST"])
def post():
    data=request.json
    ip_whois_result = IPWhois(data["ip"])
    return ip_whois_result.lookup_whois()
    

if __name__ == '__main__':
    app.run(debug=True)