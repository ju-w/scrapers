data={'fsaldu':'V0H1T0','deviceID':'Web','key': '<<SECRET>>'}
proxies={'https':'socks5://187.23.136.94:18597'}

requests.post('https://prizm5lb.prizm5api.com/getPrizm2.php', data=data, proxies=proxies).text
