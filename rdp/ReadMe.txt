RDP:
1. Raspberry Pi lite image.
2. sudo apt-get install python3-pip
3. sudo apt-get update
   sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
4 sudo apt-get install freerdp2-x11
5 sudo apt-get lightdm
6 sudo apt-get lxsession
7 make auto run command:  
    - create the .xsession file in /home/pi   sudo nano .xsession
    - input the following command
          #!/bin/sh
            xset s off                  # don't activate screensaver
            xset -dpms                  # disable DPMS (Energy Star) features.
            xset s noblank              # don't blank the video device
            python3 /home/pi/test.py    # now start your script 
8. Disable the boot log text.
/boot/cmdline.txt
consoleblank=1 logo.nologo quiet loglevel=0 plymouth.enable=0 vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fastboot noatime nodiratime noram

# logo.nologo: turns off raspberry(s) at boot
# quiet: hide messages
# console=tty3: hide more messages (redirect boot messages to the third console)
# loglevel=3: hide even more messages (disable non-critical kernel log messages) (Included with default RetroPie image)
# vt.global_cursor_default=0: hide blinking cursor
# plymouth.enable=0: disable plymouth boot text (Included with default RetroPie Image)
 
If using a plymouth bootsplash:
# plymouth.ignore-serial-consoles: ignore serial consoles
# plymouth.enable=0: remove to enable plymouth boot text
# splash: enable plymouth splash

You can add the any of the options to the end of the cmdline.txt file make sure it is all on the same line or else it will break your boot sequence!!!

/boot/config.txt
# disable_splash=1: Disable large rainbow screen on initial boot
# avoid_warnings=1: will disable warnings such as undervoltage/overheating and isn't really recommended.
Autologin Text:
Hide login text:
# touch ~/.hushlogin

Hide/modify message of the day (superseded by .hushlogin if used):

# sudo nano /etc/motd

Hide Autologin Text:

# sudo nano /etc/systemd/system/autologin@.service

change
ExecStart=-/sbin/agetty --autologin pi --noclear %I $TERM
to
ExecStart=-/sbin/agetty --skip-login --noclear --noissue --login-options "-f pi" %I $TERM

Hide Autologin Text: (Raspbian 9 "Stretch" and newer)

#sudo nano /etc/systemd/system/getty@tty1.service.d/autologin.conf

change
ExecStart=-/sbin/agetty --autologin pi --noclear %I $TERM
to
ExecStart=-/sbin/agetty --skip-login --noclear --noissue --login-options "-f pi" %I $TERM

9. Make splash screen.
https://yingtongli.me/blog/2016/12/21/splash.html

Clean up the boot process
- Firstly, we want to remove as much of the text as possible from the boot-up process, to allow for a clean transition.
- Disable the Raspberry Pi ‘color test’ by adding the line disable_splash=1 to /boot/config.txt.
- Disable the Raspberry Pi logo in the corner of the screen by adding logo.nologo to /boot/cmdline.txt.
- Disable the various bits of output from the kernel and friends by adding consoleblank=0 loglevel=1 quiet to /boot/cmdline.txt.
- Disable the login prompt by running systemctl disable getty@tty1 as root.

Set up the splash screen
- Design your splash screen image and place it somewhere easily readable.
- Install fbi, the framebuffer image viewer, by running apt install fbi as root.
- Create the file /etc/systemd/system/splashscreen.service with the following content:
  [Unit] 
  Description=Splash screen
  DefaultDependencies=no
  After=local-fs.target

  [Service]
  ExecStart=/usr/bin/fbi -d /dev/fb0 --noverbose -a /opt/splash.png
  StandardInput=tty
  StandardOutput=tty

  [Install]
  WantedBy=sysinit.target

Remove black borders
 You may run in to the issue where there appears to be a black border drawn around the splash screen. This is in fact a hardware-level black border around the entire framebuffer, and can be          disabled by adding disable_overscan=1 to /boot/config.txt.

Video Splash
 - install the omxplayer: sudo apt-get install omxplayer
 - make the mp4 video file
 - In the service content, run ExecStart=omxplayer /hom