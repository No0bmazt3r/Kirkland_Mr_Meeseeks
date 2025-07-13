import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_un_security_council():
    print("📘 Scraping UN Security Council Consolidated List...")
    url = "https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list"

    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print("✅ Fetched UN SC page successfully!\n")
            soup = BeautifulSoup(response.content, "html.parser")
            print("🔗 Links on UN SC page:")
            for a_tag in soup.find_all("a"):
                text = a_tag.get_text(strip=True)
                href = a_tag.get("href")
                if href and text:
                    print(f"- {text} ➜ {href}")
        else:
            print(f"❌ UN SC page failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error scraping UN SC: {e}")

def scrape_moha_page():
    print("\n📘 Scraping MOHA Page...")
    url = "https://www.moha.gov.my/index.php/en/senarai-kementerian-dalam-negeri"

    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print("✅ Fetched MOHA page successfully!\n")
            soup = BeautifulSoup(response.content, "html.parser")
            print("🔗 Links on MOHA page:")
            for a_tag in soup.find_all("a"):
                text = a_tag.get_text(strip=True)
                href = a_tag.get("href")
                if href and text:
                    print(f"- {text} ➜ {href}")
        else:
            print(f"❌ MOHA page failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error scraping MOHA: {e}")

def run_web_scraping():
    print("\n🌐 Launching Dual Website Scraper...\n")
    scrape_un_security_council()
    scrape_moha_page()
