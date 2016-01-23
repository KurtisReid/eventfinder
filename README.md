# Some Title

Some description ....

## Instructions

To get the python dependencies go into you terminal,
**cd** into the project's root directory and run

    pip install -r requirements.txt

To get the front-end dependencies I used a package system named bower,
which is installable through NodeJS npm. So if you don't have Node installed
on your system either download it from their site or if you're on a debian-based OS
run

    sudo apt-get install nodejs

After you download node, you'll have npm along with it, which will allow you to download bower and gulp, 2 tools we'll be using. So to do that run

    sudo npm i -g bower && sudo npm i -g gulp && sudo npm i -g stylus

Now that we have the 2 packages installed we can download the front-end dependencies through bower. Make sure you're in the project's root directory and run

    npm install && bower install

To compile the Stylus code into CSS you'll need to to use gulp, and the command to do that is

    cd static/stylus && stylus -w index.styl

    //Temporary, I'm working on a shorter way with gulp but this will work for now...


Finally, with all the setting up out of the way, you can run the app from the  root directory using

    python __init__.py

Go to port localhost:5000 in your browser, and you should be able to see the site in progress.

### Made by:
===========

  + Kurtis

  + Dor

  + Fernando

  + Dusan

  + Mike

For PennApps Winter 2016.
