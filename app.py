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

@app.route('/api/v1/brands/<int:brand_id>/app_requirements', methods=['GET'])
def get_app_requirements(brand_id: int):
    """
    Tell the app what minimum version it must be in order to run
    """
    response = {"apkMinVersion": "1.0.0"
                , "message": "Your app version did not pass the minimum version check. Please report this."}
    return jsonify(response)


@app.route('/api/v1/settings/<string:setting_name>', methods=['PUT'])
def put_device_profile(setting_name: str):
    """
    Called to get various settings

    Unfortunately, the return shape is pretty free-form and not easy to deduce
    """

    # Basic return type is a "SettingsEnvelope"
    response = {"id": 4567
                , "name": setting_name
                , "value": None  # Should be a MessagePayload
                , "version": "1.10.10"  # java.lang.Object
                }
    return jsonify(response)


@app.route('/api/v1/units/<string:watch_MAC>', methods=['PUT', 'GET'])
def put_watch_MAC(watch_MAC: str):
    """
    This is called immediately after clicking the watch in the "Connect by selecting your watch below" dialogue

    It receives the watch's Bluetooth MAC address. What did Olio want with that?

    Payload contains the user_id again

    This returns a "com.olio.state.Unit" object. Goodness knows what those fields are supposed to contain...
    """
    if len(request.data) > 0:
        user_id = request.json["user_id"]
    else:
        user_id = None

    firmware = {"bluetoothApkHash": "c949a72209ff2f6c10fd2b687615eacb"
                , "bluetoothApkUrl": None
                , "bluetoothApkVersion": "4.4.4"
                , "defaultSettingsCollectionId": 4321
                , "firmwareHash": "15b84af9c937e01cc04b926c763b6e15"  # This corresponds to the last officially-available firmware.zip
                , "firmwareUrl": None
                , "id": user_id
                , "name": "firmware_name"
                , "uiApkHash": "2343b4ed0c0c57b3eac8d97ce9a317a3"
                , "uiApkUrl": None
                , "uiApkVersion": "ui_apk_version"
                , "version": "1.10.221"}

    product = {"band_style": "Steel"
               , "body_style": "Steel"
               , "brand": None
               , "default_firmware": None
               , "id": user_id
               , "name": "product_name"
               , "sku": "product_sku"}
    current_look = {"asset_bundle_url": "looks/Model1_Gold"
                    , "current": True
                    , "id": user_id
                    , "name": "Model1_Gold"
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

    TODO: Make this reply in the proper structure (SettingsEnvelope)

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
    response = {"email": "haha@example.com"  # This ends up in the app's "Account Info" screen
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


@app.route('/EULA_FORM', methods=['GET'])
def get_EULA():
    """
    Hohoho. All ur basez are belong to us
    Note that this is served as www.oliodevices.com NOT api.oliodevices.com
    """
    return 'All your bases are belong to us. Ok?'


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
