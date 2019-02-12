from bs4 import BeautifulSoup
import requests
import random


def get_ip_list(url, headers, proxies):
    web_data = requests.get(url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


if __name__ == '__main__':
    urls = 'http://www.xicidaili.com/nn/'+str(i for i in range(5))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/'
                      '24.0.1312.60 Safari/537.17'
    }
    proxy = {"http": "http://proxy-prc.intel.com:911", "https": "https://proxy-prc.intel.com:911"}
    for url in urls:
        ip_list = get_ip_list(url, headers=headers, proxies=proxy)
        proxies = get_random_ip(ip_list)
        print(proxies)
