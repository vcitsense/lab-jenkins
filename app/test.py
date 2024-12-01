import pytest
import requests
import xml.etree.ElementTree as ET

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

# Prepare XML structure
testsuites = ET.Element("testsuites")
testsuite = ET.SubElement(testsuites, "testsuite", name="pytest", errors="0", failures="0", skipped="0", tests="21", time="0.181", timestamp="2024-12-01T04:51:11.422039+00:00", hostname="8e83d85069cd")

# Usar parametrize para pasar las rutas de la API a la función de prueba
@pytest.mark.parametrize("api_url", apis)
def test_api(api_url):
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(f"{base_url}{api_url}")
        
         # Add the response details to the testcase
        status_code = str(response.status_code)
        response_text = response.text
        
        # Crear el nombre del caso de prueba
        testcase = ET.SubElement(testsuite, "testcase", classname="test", name=f"test_apiiiiiiiiiiiii{api_url}", time="0.001")
        
        status_ = ET.SubElement(testsuite, "status", classname="test", name=f"status_cod={status_code}", time="0.001")
        
        result_ = ET.SubElement(testsuite, "result", classname="test", name=f"result_={response_text}", time="0.001")

       
        
        # Add status details to the testcase node
        status = ET.SubElement(testcase, "status", code=status_code, response=response_text)
        
        # Update errors and failures based on the response status
        if response.status_code >= 400:
            testsuite.set("failures", str(int(testsuite.attrib["failures"]) + 1))
        elif response.status_code == 0:
            testsuite.set("errors", str(int(testsuite.attrib["errors"]) + 1))

    except requests.exceptions.RequestException as e:
        testcase = ET.SubElement(testsuite, "testcase", classname="test", name=f"test_api{api_url}", time="0.001")
        ET.SubElement(testcase, "status", code="Error", response=str(e))
        testsuite.set("errors", str(int(testsuite.attrib["errors"]) + 1))

# Write the updated XML to file
tree = ET.ElementTree(testsuites)
tree.write("test_result.xml", encoding="UTF-8", xml_declaration=True)
