# -*- coding: utf-8 -*-
# author: llx

import uuid
import hmac
import hashlib
import base64
import time

from flask import Flask
from flask import jsonify

app = Flask(__name__)

static_secret = 'test_secret'
turn_uri = 'turn:xxx.xxx.xxx.xxx'

@app.route("/turn")
def turn_api():

    userid = uuid.uuid4().hex
    username = '%d:%s' % (int(time.time()) + 24*3600, userid)

    digest = hmac.new(static_secret,username,digestmod=hashlib.sha1).digest()
    credential = base64.b64encode(digest)

    return jsonify({
            'username':username,
            'url':turn_uri,
            'credential':credential
        })


if __name__ == "__main__":
    app.run()
