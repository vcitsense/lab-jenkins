import pytest
import requests

base_url = "http://127.0.0.1:5000"

# Lista de las rutas de las APIs a probar
apis = [
    "/calc/add/10/5",
    "/calc/add/abc/5",
    "/calc/add/10/0",
    "/calc/substract/10/5",
    "/calc/substract/abc/5",
    "/calc/substract/10/0",
    "/calc/multiply/10/5",
    "/calc/multiply/abc/5",
    "/calc/multiply/10/0",
    "/calc/divide/10/5",
    "/calc/divide/abc/5",
    "/calc/divide/10/0",
    "/calc/power/2/3",
    "/calc/power/abc/3",
    "/calc/power/2/0",
    "/calc/sqrt/25",
    "/calc/sqrt/abc",
    "/calc/sqrt/-25",
    "/calc/log/100",
    "/calc/log/abc",
    "/calc/log/0",
]

# Usar parametrize para pasar las rutas de la API a la función de prueba
@pytest.mark.parametrize("api_url", apis)
def test_api(api_url):
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(f"{base_url}{api_url}")
        
        # Registrar la URL que se está probando
        print(f"Testing {api_url}:")
        print(f"URL: {base_url}{api_url}")
        
        # Verificar si la respuesta es exitosa (200)
        if response.status_code == 200:
            print(f"Status Code: 200")
            print(f"Response: {response.text}")
            print("Success: The request was successful.")
        elif response.status_code == 400:
            print(f"Status Code: 400")
            print(f"Error Response: {response.text}")
            print("Failure: The request returned a bad request error.")
        elif response.status_code == 500:
            print(f"Status Code: 500")
            print(f"Error Response: {response.text}")
            print("Failure: The request returned an internal server error.")
        else:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        print("\n")
    except requests.exceptions.RequestException as e:
        print(f"Error testing {api_url}: {e}")
        print("\n")
