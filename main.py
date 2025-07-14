import requests
import xmltodict
import json

url = "https://scsanctions.un.org/resources/xml/en/consolidated.xml"
xml_raw = requests.get(url, timeout=10).content
root = xmltodict.parse(xml_raw)

for ind in root['CONSOLIDATED_LIST']['INDIVIDUALS']['INDIVIDUAL']:
    first  = ind.get('FIRST_NAME', '')
    second = ind.get('SECOND_NAME', '')
    nat    = ind.get('NATIONALITY', {}).get('VALUE', 'N/A')
    print("Name:", first, second)
    print("Nationality:", nat)
    print("-" * 30)

with open('sanctions_list.json', 'w') as f:
    json.dump(root, f, indent=4)

print("Sanctions list saved to sanctions_list.txt")

date = root['CONSOLIDATED_LIST']['@dateGenerated']
print("Data generated on:", date)