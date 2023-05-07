from requests import Session, get

# com tor
session = Session()
session.proxies = {'http': 'socks5://127.0.0.1:9050'}

tor = session.get('http://httpbin.org/ip')
print(f'Tor IP: {tor.json()}')


# sem tor
normal = get('http://httpbin.org/ip')
print(f'Normal IP: {normal.json()}')