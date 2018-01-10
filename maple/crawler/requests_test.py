
import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'


def use_simple_requests():
    response = requests.get(URL_IP)
    print('Response Headers>>>')
    print(response.headers)
    print('Response Body>>>')
    print(response.text)


def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    response = requests.get(URL_IP, params=params)
    print('Headers: ', response.headers)
    print('Status Code: ', response.status_code)
    print('Body: ', response.json())


if __name__ == '__main__':

    # use_simple_requests()
    use_params_requests()

    # r = requests.get("http://www.baidu.com")
    # print(r.status_code)
    # r.encoding= 'utf-8'
    # print(r.text)


