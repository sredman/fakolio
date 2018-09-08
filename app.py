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


@app.route('/api/v1/settings/PairedDeviceProfile', methods=['PUT'])
def put_device_profile():
    """
    Called immediately after put_watch_MAC

    For real, don't ask me what this is supposed to do, though
    """
    return


@app.route('/api/v1/units/<string:watch_MAC>', methods=['PUT'])
def put_watch_MAC(watch_MAC: str):
    """
    This is called immediately after clicking the watch in the "Connect by selecting your watch below" dialogue

    It receives the watch's Bluetooth MAC address. What did Olio want with that?

    Payload contains the user_id again

    This returns a "com.olio.state.Unit" object. Goodness knows what those fields are supposed to contain...
    """
    user_id = request.json["user_id"]
    firmware = {"bluetoothApkHash": None
                , "bluetoothApkUrl": None
                , "bluetoothApkVersion": "bt_apk_version"
                , "defaultSettingsCollectionId": 4321
                , "firmwareHash": None
                , "firmwareUrl": None
                , "id": user_id
                , "name": "firmware_name"
                , "uiApkHash": None
                , "uiApkUrl": None
                , "uiApkVersion": "ui_apk_version"
                , "version": "firmware_version"}

    product = {"band_style": "Steel"
               , "body_style": "Steel"
               , "brand": None
               , "default_firmware": None
               , "id": user_id
               , "name": "product_name"
               , "sku": "product_sku"}
    current_look = {"asset_bundle_url": None
                    , "current": True
                    , "id": user_id
                    , "name": "Look_name"
                    , "product": product
                    , "sample_watch_face": None}
    user = {"email": "email@example.com"
            , "firstName": "FirstName"
            , "lastName": "LastName"
            , "id": user_id}

    response = {"current_look": current_look
                , "firmware": firmware  # Could we fake a firmware update by punching this?
                , "id": user_id
                , "product": product
                , "user": user}
    return jsonify(response)


@app.route('/api/v1/users/<int:user_id>/settings')
def get_settings(user_id: int):
    """
    Handle a settings request
    :param user_id: Whatever we sent the device as the reply to its get_me request
    """
    response = {}
    return jsonify(response)


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


@app.route('/')
def test_SSL():
    """
    The Olio app GUI does not do a very nice job of reporting specifically what went wrong when an
    API call fails. If you are able to view https://api.oliodevices.com in the phone's browser without
    accepting a security certificate override, then we know the certificate and DNS are working
    """
    return "If you see this page as https://api.oliodevices.com without having to accept an SSL certificate, you have properly configured your device!"


if __name__ == '__main__':
    key = 'pki/privkey.key'
    cert = 'pki/CA.crt'
    app.run(host='0.0.0.0'
            , ssl_context=(cert, key)
            , debug=True)
