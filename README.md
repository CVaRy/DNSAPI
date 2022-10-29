# DNSAPI

#Flush DNS Global Server

// CloudFlare

""/api/dnsflush/cloudflare"" - POST
Body:
{
    "domain":"example.com",
    "type":"NS"
}

Type DNS List:
NS
A
MX
SRV
TXT
..

// IP Whois 

""/api/ipwhois"" - POST
Example
Body:
{
    "ip":"9.9.9.9"
}
