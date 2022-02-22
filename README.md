# Note: Development is discontinued because I bricked my watch. Word to the wise, don't set up a post-boot script which reboots the watch 10 seconds after booting!

- Need to configure a local DNS server which reports that "api.oliodevices.com" and "www.oliodevices.com" is the address on which this server is running

- Need to add self-signed security certificate to Android: https://aboutssl.org/how-to-create-and-import-self-signed-certificate-to-android-device/
    - Set the common name to *.oliodevices.com
    - Use the generated CA.crt and private key for running the HTTPS app

- Need to port forward incoming traffic on port 443 to whatever port this server is running on

- Need to use DNS Changer app to set local DNS (Changing DHCP or Android wifi settings *does not work* reliably!)

- Launch Server App
  - Verifiy that visiting https://api.oliodevices.com in the moble browser (*NOT* Firefox, which uses its own keystore) works without bypassing a certificate problem

- Launch Olio Assist app and attempt to log in
  - Can use any email/password combination. It is not checked nor stored.

- Accept the "EULA"

- At this point, can actually pair and get into the app by:
    - Select the watch to pair
      - If you have already paired via Bluetooth, can probably skip this step
      - App crashes
    - Clear Olio Assist app data (from Android settings)
      - Probably sane to force kill it as well
    - Go back to step 1 and re login, etc.
    - When you get to the list of devices DO NOT pick one. Instead, push "Skip" in the top right and set up the assistant
    - Set up Olio Assistant
    - When finished, you will be back to the watch selection screen without a skip button. Pick your watch.
    - App is non-functional, and watch still hasn't detected the pairing, but it's one step closer...

- After pairing the watch and seeing non-functional app, if you restore the app's data partition (via Titanium Backup, etc.) from a backup where the watch was previously working, the watch works again!
