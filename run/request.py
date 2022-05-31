from time import sleep

from PyQt6.QtWidgets import QApplication
from requests import post


def translation(jar, word, authToken):
    header = {
        'Content-Type': 'application/json;charset=utf-8'
    }
    params = {
        'from': 'en',
        'to': 'zh',
        'q': word
    }
    transHost = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + authToken
    for i in range(3):
        transResponse = post(transHost, headers=header, params=params)
        if transResponse.status_code != 200:
            jar.addStatus('请求失败，请检查网络情况，5秒后重试...({}/3)'.format(i + 1))
            QApplication.processEvents()
            sleep(5)
            continue
        if 'error_code' in transResponse.json().keys():
            jar.addStatus('翻译错误: {}: {}, 5秒后重试...({}/3)'.format(transResponse.json()['error_code'],
                                                                transResponse.json()['error_msg'], i + 1))
            continue
        return transResponse.json()['result']['trans_result'][0]


def transJson(jar, js, authToken):
    outputJson = {}
    processNow = 0
    for key in js:
        processNow += 1
        jar.addStatus('正在翻译...({}/{})'.format(processNow, len(js)))
        QApplication.processEvents()
        outputJson[key] = translation(jar, js[key], authToken)
    jar.addStatus('翻译完成')
    QApplication.processEvents()
    return outputJson
