#!/usr/bin/env python3

# Reproduce the Olio REST API so that devices may be reenabled
#
# Copyright (C) 2018 Simon Redman <simon@ergotech.com>
#
# This file is part of Fakolio
#
# Fakolio is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.

# Fakolio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar. If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/v1/me', methods=['GET'])
def get_me():
    """
    Handle a "me" request (Some naming convention, eh?)

    I literally have no idea what this does except we get the ID back later
    """
    response = {"email": "haha@example.com"
                , "id" : "1234"}
    return jsonify(response)


@app.route('/oauth/token', methods=['POST'])
def login():
    """
    Handle a login request by returning an "auth token"
    """
    response = {"accessToken": "blarghaha"
                ,"errorDescription": "Everything is good"}
    return jsonify(response)


if __name__ == '__main__':
    key = 'pki/privkey.key'
    cert = 'pki/CA.crt'
    app.run(host='0.0.0.0'
            , ssl_context=(cert, key)
            , debug=True)
