import requests
import datetime

URLS = [
    "https://www.google.com",
    "https://github.com"
]

ARQUIVO_LOG = "registro_monitoramento.txt"

def verificar_site(url):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            mensagem = f"[{data_hora}] SUCESSO: {url} está online\n"
            print(f"✅ {url} OK")
        else:
            mensagem = f"[{data_hora}] ALERTA: {url} status {resposta.status_code}\n"
            print(f"⚠️ {url} problema")

    except Exception as e:
        mensagem = f"[{data_hora}] ERRO: {url} - {e}\n"
        print(f"❌ erro em {url}")

    with open(ARQUIVO_LOG, "a") as f:
        f.write(mensagem)


if __name__ == "__main__":
    for site in URLS:
        verificar_site(site)
