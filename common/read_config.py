# -*- coding: utf-8 -*-
"""
配置读取类
@Time ： 2023/3/7
@Auth ： qihang
"""

import os, codecs
import configparser

prodir = os.path.dirname(os.path.abspath(__file__))
conf_prodir = os.path.join(prodir, '../config/conf.ini')


class ReadConfig:
    def __init__(self):
        with open(conf_prodir) as fd:
            data = fd.read()
            # 清空文件信息
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                file = codecs.open(conf_prodir, 'w')
                file.write(data)
                file.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(conf_prodir)

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        return self.cf.get("DATABASE", name)

    def get_db_config(self):
        host = self.get_db("host")
        username = self.get_db("username")
        password = self.get_db("password")
        port = self.get_db("port")
        database = self.get_db("database")

        dbconfig = {
            'host': str(host),
            'user': username,
            'password': password,
            'port': int(port),
            'db': database
        }
        return dbconfig


# if __name__ == '__main__':
#     readconf_obj = ReadConfig()
#     print(readconf_obj.get_db_config())

