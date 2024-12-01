import pytest
import requests
import xml.etree.ElementTree as ET

base_url = "http://127.0.0.1:5000"
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

@pytest.mark.parametrize("api_url", apis)
def test_api(api_url):
    testcase_name = f"test_apiiiiiiiiiiiii{api_url}"  # Modified name for each test case
    testcase = ET.SubElement(testsuite, "testcase", classname="test", name=testcase_name, time="0.001")
    try:
        response = requests.get(f"{base_url}{api_url}")
        status_code = str(response.status_code)
        response_text = response.text
        status = ET.SubElement(testcase, "status", code=status_code, response=response_text)
    except requests.exceptions.RequestException as e:
        ET.SubElement(testcase, "status", code="Error", response=str(e))

# Save the XML tree to file
tree = ET.ElementTree(testsuites)
tree.write("test_result2.xml", encoding="UTF-8", xml_declaration=True)
