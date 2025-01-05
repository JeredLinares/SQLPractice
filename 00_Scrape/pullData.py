'''
Pull Data from SEC Website
JD Linares
Created: 2025 01 04
'''

from requests import Request
from bs4 import BeautifulSoup
import time

# Pull first page of results from SEC search for SIC 8050
# Manual search: https://www.sec.gov/cgi-bin/browse-edgar?company=&match=starts-with&filenum=&State=&Country=&SIC=8050&myowner=exclude&action=getcompany

url_sic_search = "https://www.sec.gov/cgi-bin/browse-edgar?company=&match=starts-with&filenum=&State=&Country=&SIC=8050&myowner=exclude&action=getcompany"

# Add a typical user-agent
header = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }


result = requests.get(url_sic_search)

print(BeautifulSoup(result.text))

# Direct download to avoid 403
