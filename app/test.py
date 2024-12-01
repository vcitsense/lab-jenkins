import requests

# URL base de la API
base_url = "http://127.0.0.1:5000"

# Lista de las rutas de las APIs a probar
apis = [
    "/calc/add/10/5",  # Suma válida
    "/calc/add/abc/5",  # Error 400 (parámetros no válidos)
    "/calc/add/10/0",  # Error 500 (operación con división por cero en algún caso)
    
    "/calc/substract/10/5",  # Resta válida
    "/calc/substract/abc/5",  # Error 400
    "/calc/substract/10/0",  # Error 500
    
    "/calc/multiply/10/5",  # Multiplicación válida
    "/calc/multiply/abc/5",  # Error 400
    "/calc/multiply/10/0",  # Error 500
    
    "/calc/divide/10/5",  # División válida
    "/calc/divide/abc/5",  # Error 400
    "/calc/divide/10/0",  # Error 500 (división por cero)
    
    "/calc/power/2/3",  # Potencia válida
    "/calc/power/abc/3",  # Error 400
    "/calc/power/2/0",  # Error 500
    
    "/calc/sqrt/25",  # Raíz cuadrada válida
    "/calc/sqrt/abc",  # Error 400
    "/calc/sqrt/-25",  # Error 500 (si se considera que no puedes obtener la raíz cuadrada de un número negativo)
    
    "/calc/log/100",  # Logaritmo válido
    "/calc/log/abc",  # Error 400
    "/calc/log/0",  # Error 500 (logaritmo de cero)
]

# Función para realizar las solicitudes a la API
def test_api(api_url, file):
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(f"{base_url}{api_url}")
        
        # Registrar la URL que se está probando
        file.write(f"Testing {api_url}:\n")
        file.write(f"URL: {base_url}{api_url}\n")
        
        # Verificar si la respuesta es exitosa (200)
        if response.status_code == 200:
            file.write(f"Status Code: 200\n")
            file.write(f"Response: {response.text}\n")
            file.write("Success: The request was successful.\n")
        elif response.status_code == 400:
            file.write(f"Status Code: 400\n")
            file.write(f"Error Response: {response.text}\n")
            file.write("Failure: The request returned a bad request error.\n")
        elif response.status_code == 500:
            file.write(f"Status Code: 500\n")
            file.write(f"Error Response: {response.text}\n")
            file.write("Failure: The request returned an internal server error.\n")
        else:
            file.write(f"Status Code: {response.status_code}\n")
            file.write(f"Response: {response.text}\n")
        file.write("\n")
    except requests.exceptions.RequestException as e:
        file.write(f"Error testing {api_url}: {e}\n")
        file.write("\n")

# Función principal para recorrer todas las APIs y realizar las pruebas
def run_tests():
    with open("api_test_results.txt", "w") as file:
        # Iterar sobre todas las rutas de la API
        for api_url in apis:
            test_api(api_url, file)

# Ejecutar las pruebas
if __name__ == "__main__":
    run_tests()
