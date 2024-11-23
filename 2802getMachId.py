from urllib.parse import urljoin

import  requests

# __host = 'sit-api-2.dbsportxxxifbdxm2.com'
__host = 'api.sportxxxyp7.com'

def  getMachId():
    url = "http://{}/yewu30/v1/m/queryWebMatchResult".format(__host)
    header_m = {"Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "68",
                "Content-Type": "application/json",
                "Host": "{}".format(__host),
                # "Origin": "http://test-match-result-official-website.dbsportxxxifbdxm2.com",
                # "Referer": "http://test-match-result-official-website.dbsportxxxifbdxm2.com/",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

    data_m = {"pageNo":1,"pageSize":50,"langType":"zh","matchStatus":"FINISHED,CANCELLED"}

    # print(url)
    # print(header_m)

    re_data = requests.post(url=url, headers=header_m, json=data_m)

    # print(re_data.text)
    data_json = re_data.json()

    print(data_json)
    records_list_data = data_json.get('data').get('records')
    matchId_list = []
    for records in records_list_data:
        matchId_list.append(records.get('matchId'))

    print(matchId_list)


if __name__ == '__main__':
    getMachId()