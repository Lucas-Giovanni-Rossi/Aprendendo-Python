# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests  # acessar HTTP

try:
    requests.get('https://pudim.com.br/', timeout=5)
except requests.RequestException:
    print('❌ Erro!')
else:
    print('✅ Tudo ok')
