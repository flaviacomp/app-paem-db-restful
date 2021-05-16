import requests


class BaseTest:

    URL_BASE = "http://localhost:5000/api.paem{route}"

    @classmethod
    def get_url(cls, route):
        cls.URL_BASE.format(route)

    @classmethod
    def post(self, url, body):

        post = input("\ntesting POST request ?(yes-y/nop-n) ")

        resp_post = requests.post(
            url=url, 
            json=body
        )

        print(resp_post.url)
        print("status_code: ",resp_post.status_code)
        print("headers: ", resp_post.headers)
        print("json: ", resp_post.json())

        id = list(filter(lambda k: 'id_' in k, resp_post.json().keys()))
        resp_post.json().get(id)
        return id

    @classmethod
    def put(self, url, body):

        put = input("\ntesting PUT request ?(yes-y/nop-n) ")

        if put=="n" or put=="nop":
            print("Abort TEST PUT")

        resp_post = requests.put(
            url=url, 
            json=body
        )

        print(resp_post.url)
        print("status_code: ",resp_post.status_code)
        print("headers: ", resp_post.headers)
        print("json: ", resp_post.json())

    @classmethod
    def get(self, url, params):
        
        get = input('\ntesting GET request ?(yes-y/nop-n) ')

        if get=="n" or get=="nop":
            print("Abort TEST GET")
        
        resp_get = requests.get(
            url=url,
            params=params
        )

        print(resp_get.url)
        print("status_code: ",resp_get.status_code)
        print("headers: ", resp_get.headers)
        print("text: ", resp_get.json())

    @classmethod
    def delete(self, url, params):

        delete = input('\ntesting DELETE request ?(yes-y/nop-n) ')

        if delete=="n" or delete=="nop":
            print("Abort TEST DELETE")
            return

        resp_del = requests.delete(
            url=url, 
            params=params
        )

        print(resp_del.request)
        print("status_code: ",resp_del.status_code)
        print("headers: ", resp_del.headers)
        print("text: ", resp_del.text)
