Notice that, in Olio's olio-firmware.zip, there are two shell files, update.sh and update_2.sh

At the end of update.sh, it does some weird mess where the downloaded files are deleted and update_2.sh takes the place of update.sh

Notice that update_2.sh is responsible for deleting itself

This all appears to be because update.sh is run *on every boot*. If you want to fake a firmware update, be sure to save these two pieces or you could end up in a bootloop!
