import dns.resolver
import socket

dns.resolver.Timeout = 3

class checkertools:
    def google(domain_url,type):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =["8.8.8.8"]
        if type == "ptr" or "PTR":
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip)
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers

    def cloudflare(domain_url,type):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =["1.1.1.1"]
        if type == "ptr" or "PTR":
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip)
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers

    def opendns(domain_url,type):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =["208.67.222.220"]
        if type == "ptr" or "PTR":
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip)
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers
    
    def quad9(domain_url,type):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =["9.9.9.9"]
        if type == "ptr" or "PTR":
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip[0])
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers
    
    def turktelekom(domain_url,type):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =["212.175.192.114"]
        if type == "ptr" or "PTR":
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip)
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers

    def comodo(domain_url,type):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =["8.26.56.26"]
        if type == "ptr" or "PTR":
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip)
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers

    def verisign(domain_url,type):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =["64.6.64.6"]
        if type == "ptr" or "PTR":
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip)
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers

    def customdns(domain_url,type,customdns):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers =[customdns]
        if type == "ptr" or "PTR" :
            try:
                domain_ip = socket.gethostbyname(domain_url)
                result_ptr = socket.gethostbyaddr(domain_ip)
                return result_ptr[0]
            except:
                return "['Hatalı işlem hostname bulunamadı']" # Bazı IP hostname bulunmadığı için hata vermektedir.
        else:
            result  = res.resolve(domain_url, type)
            nameservers = [ns.to_text() for ns in result]
        return nameservers