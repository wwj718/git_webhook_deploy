#!/usr/bin/env python
# encoding: utf-8
import subprocess
import os
from flask import Flask, request
import logging


app = Flask(__name__)

# setting 从环境变量里拿到
WEBHOOK_PASSWORD = os.environ.get('WEBHOOK_PASSWORD')
print({"WEBHOOK_PASSWORD":WEBHOOK_PASSWORD})


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    '''
    test repo
        http://git.oschina.net/wuwenjie/webhook_test

    http post 127.0.0.1:5000 hook_name=push_hooks password=xxx
    ngrok test
        ./ngrok --config ./ngrok.cfg --subdomain webhook 5000
        http://webhook.tunnel.phpor.me
    '''
    r_json = request.get_json()
    print(r_json)

    # 判断合法性
    if r_json:
        if r_json.get("hook_name") == "push_hooks" and r_json.get("password") == WEBHOOK_PASSWORD:

            cmd = "bash deploy.sh"
            # subprocess模块的Popen对象可能以非阻塞的方式调用外部可执行程序
            subprocess.Popen(cmd,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            print('run deploy.sh(go on...)')
            return "ok"
    return 'error request!'


if __name__ == '__main__':
    # export FLASK_DEBUG=1
    # nginx webhook2 #ok
    #gunicorn -w 4 -b 127.0.0.1:5005 git_webhook_server:app
    app.run()
