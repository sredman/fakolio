- Need to configure a local DNS server which reports that "api.oliodevices.com" is the address on which this server is running

- Need to port forward incoming traffic on port 443 to whatever port this server is running on

- Need to add self-signed Certificate to Android: https://aboutssl.org/how-to-create-and-import-self-signed-certificate-to-android-device/
    - Incidentally, use the generated CA.crt and private key for running the HTTPS app

- Need to use DNS Changer app to set local DNS (Changing DHCP or Android wifi settings *does not work* reliably!)

- Launch Server App
  - Verifiy that visiting https://api.oliodevices.com in the moble browser (*NOT* Firefox, which uses its own keystore) works without bypassing a certificate problem

- Launch Olio Assist app and attempt to log in
  - Can use any email/password combination. It is not checked nor stored.

- Bypass the EULA screen by killing the app and relauncing
  - TODO: This may be a cause of the app crashing later. I don't know.

- Can see the watch in the list of devices and attempt to pair, but the app crashes, presumably due to a malformed response from put_watch_MAC (/api/v1/units/<string>)
