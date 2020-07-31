import requests


class Byhylogin():
    def __init__(self,s):
        self.s = s

    def login(self,user,pwd):
        url = 'http://127.0.0.1/api/mgr/signin'
        body = {
            "username":user,
            "password":pwd
        }

        res = self.s.post(url=url,data=body)
        return res

if __name__ == '__main__':
    s = requests.session()
    a = Byhylogin(s)
    b = a.login('byhy',88888888)
    print(b.text)

