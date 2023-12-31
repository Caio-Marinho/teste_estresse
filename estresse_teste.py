import requests
from concurrent.futures import ThreadPoolExecutor
import time
import ipaddress
import random

# Função que gera um IP aleatório
def generate_random_ip():
    return str(ipaddress.IPv4Address(random.randint(2**24, 2**32 - 1)))

# Função que faz uma solicitação HTTP e retorna o código de status
def make_request(url):
    # Gerando um IP aleatório
    ip = generate_random_ip()
    # Usando o IP na solicitação
    response = requests.get(url, headers={'X-Forwarded-For': ip})
    return response.status_code

# Função de teste de estresse que utiliza threads para realizar solicitações concorrentes
def stress_test(url, num_requests, num_concurrent):
    # Usando ThreadPoolExecutor para criar um pool de threads
    with ThreadPoolExecutor(max_workers=num_concurrent) as executor:
        # Registrando o tempo de início para medir o desempenho
        start_time = time.time()

        # Criando uma lista de objetos Future representando as solicitações
        futures = [executor.submit(make_request, url) for _ in range(num_requests)]

        # Obtendo os resultados das solicitações
        results = [future.result() for future in futures]

    # Registrando o tempo total e calculando as métricas de desempenho
    end_time = time.time()
    total_time = end_time - start_time

    # Exibindo os resultados e métricas
    print(f"Total Requests: {num_requests}")
    print(f"Concurrent Requests: {num_concurrent}")
    print(f"Total Time: {total_time} seconds")
    print(f"Requests per Second: {num_requests / total_time}")
    print(f"Results: {results}")
    print(f"Results: {len(results)}")


if __name__ == "__main__":
    # Substitua a URL pelo seu endpoint real
    target_url = "<URL>"
    num_requests = 100  # Número total de solicitações
    num_concurrent = 10  # Número de solicitações simultâneas

    # Chamando a função de teste de estresse
    stress_test(target_url, num_requests, num_concurrent)
