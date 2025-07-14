import pdfplumber, json, requests, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://moha.gov.my/images//SENARAI_KDN_2025_UPDATE.pdf"
response = requests.get(url, verify=False)
with open("file.pdf", "wb") as f:
    f.write(response.content)

tables = []
with pdfplumber.open("file.pdf") as pdf:
    for page in pdf.pages:
        extracted = page.extract_tables()
        if extracted:
            tables.extend(extracted)

if tables:
    headers = tables[0][0]
    cleaned = []
    for table in tables:
        for row in table[1:]:
            cleaned.append(dict(zip(headers, row)))
    with open("tables.json", "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)
else:
    text = ""
    with pdfplumber.open("file.pdf") as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    with open("tables.json", "w", encoding="utf-8") as f:
        json.dump({"text": text.strip()}, f, indent=2, ensure_ascii=False)

print("Done")
