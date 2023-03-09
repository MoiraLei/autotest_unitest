# -*- coding: utf-8 -*-
import requests


class OriLoginObj:

    def __init__(self):
        self.url = "http://127.0.0.1:5000/doLogin"
        self.data = {"account": "qihang", "password": "lovePython"}

    def do_login_directly(self):
        res = requests.post(self.url, data=self.data)
        return res.text

