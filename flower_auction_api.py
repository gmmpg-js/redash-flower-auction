import datetime
import requests
import time


def get_flower_aution(service_key='서비스key', search_dt=datetime.datetime.today().strftime('%Y-%m-%d'), flower_type=1):
    import datetime
    import requests
    import time

    url = 'https://flower.at.or.kr/api/returnData.api?kind=f001'

    params = {
        'serviceKey': service_key,
        'baseDate': search_dt,
        # 데이터를 일간 단위로 업데이트하는 경우 사용 - application 측면
        # 'baseDate': datetime.datetime.today().strftime('%Y-%m-%d'),
        'flowerGubn': flower_type,  # 1:절화, 2:관엽, 3:난, 4:춘란
        'dataType': 'json',
        'countPerPage': 999999
    }

    response = requests.get(url, params=params)
    response.encoding = 'utf-8'

    response_status = response.json()['response']['items']
    # print(response_status)

    return response_status


input_dt = datetime.datetime.today().strftime('%Y-%m-%d')

input_dt = '2022-03-02'

r = get_flower_aution(search_dt=input_dt)


while True:
    if r != []:
        # print(r[:3])
        result = {
            "columns": [
                {
                    "name": "saleDate",
                    "type": "str",
                    "friendly_name": "saleDate"
                },
                {
                    "name": "flowerGubn",
                    "type": "str",
                    "friendly_name": "flowerGubn"
                },
                {
                    "name": "pumName",
                    "type": "str",
                    "friendly_name": "pumName"
                },
                {
                    "name": "goodName",
                    "type": "str",
                    "friendly_name": "goodName"
                },
                {
                    "name": "lvNm",
                    "type": "str",
                    "friendly_name": "lvNm"
                },
                {
                    "name": "maxAmt",
                    "type": "str",
                    "friendly_name": "maxAmt"
                },
                {
                    "name": "minAmt",
                    "type": "str",
                    "friendly_name": "minAmt"
                },
                {
                    "name": "avgAmt",
                    "type": "str",
                    "friendly_name": "avgAmt"
                },
                {
                    "name": "totAmt",
                    "type": "str",
                    "friendly_name": "totAmt"
                },
                {
                    "name": "totQty",
                    "type": "str",
                    "friendly_name": "totQty"
                }
            ]
        }

        result['rows'] = r

        break
    else:
        yesterday_dt = datetime.datetime.strptime(
            input_dt, '%Y-%m-%d')-datetime.timedelta(1)
        yesterday_dt = yesterday_dt.strftime('%Y-%m-%d')

        r = get_flower_aution(search_dt=yesterday_dt)
