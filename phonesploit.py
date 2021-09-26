import os
import random
import urllib.request
import sys
import getpass
import time as t
from colorama import Fore, init
import datetime



page_2 = False
arrow = Fore.RED + " └──>" + Fore.WHITE
CurrentDir = os.path.dirname(os.path.abspath(__file__))
load_count = 0
username=getpass.getuser()


def creazione_README():
    with open("README.md", "w") as f:
        f.write(f'Ricordi della mia vita')
        f.write("  ")
    print(f"File chiuso correttamente: {f.closed}")
    t.sleep(1)


def avvio_git(commit):
    os.chdir(f"C:\\Users\\{username}\\Desktop\\Ricordi\\")
    passo1=f"git init"
    os.system(passo1)
    print(Fore.GREEN + "1)Fatto passo 1\n")
    print(Fore.WHITE + " ")
    t.sleep(1)
    passo6="git add ."
    os.system(passo6)
    print(Fore.GREEN + "2)Fatto passo 2\n")
    print(Fore.WHITE + " ")
    t.sleep(1)
    passo2=f"git commit -m {commit}"
    os.system(passo2)
    print(Fore.GREEN + "3)Fatto passo 3\n")
    print(Fore.WHITE + " ")
    t.sleep(1)

    passo4=f"git push -u origin master"
    os.system(passo4)
    print(Fore.GREEN + "4)Fatto passo 4\n")
    print(Fore.WHITE + " ")
    t.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')




logo_design_1 = '''
 {0}______   {1}__  __     ______     __   __     ______     {0}______     {1}______   __         ______     __     ______  
{0}/\  == \ {1}/\ \_\ \   /\  __ \   /\ "-.\ \   /\  ___\   {0}/\  ___\   {1}/\  == \ /\ \       /\  __ \   /\ \   /\__  _\ 
{0}\ \  _-/ {1}\ \  __ \  \ \ \/\ \  \ \ \-.  \  \ \  __\   {0}\ \___  \  {1}\ \  _-/ \ \ \____  \ \ \/\ \  \ \ \  \/_/\ \/ 
 {0}\ \_\    {1}\ \_\ \_\  \ \_____\  \ \_\\"\_\   \ \_____\  {0}\/\_____\  {1}\ \_\    \ \_____\  \ \_____\  \ \_\    \ \_\ 
  {0}\/_/     {1}\/_/\/_/   \/_____/   \/_/ \/_/   \/_____/   {0}\/_____/   {1}\/_/     \/_____/   \/_____/   \/_/     \/_/
'''.format(Fore.WHITE, Fore.GREEN)

logo_design_2 = Fore.GREEN + '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .

'''
logo_design_3 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..              \033[0m Exploit time :) \033[92m
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs'''




def clear1(page):
    global page_2
    os.system('cls')
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3])
    print (Fore.RED + banner_title)    
    print (page)




page_1 = '''\n
{0}[{1}1{0}] {2}Show Connected Devices  
{0}[{1}2{0}] {2}Show real time log of device
{0}[{1}3{0}]{2} Get Battery Status 
{0}[{1}4{0}] {2}Backup photo from phone to pc
{0}[{1}5{0}] {2}Backup music from phone to pc
{0}[{1}6{0}] {2}List all apps on a phone
{0}[{1}7{0}]{2} Show Mac/Inet 
{0}[{1}8{0}] {2}Reboot mobile-phone
{0}[{1}9{0}] {2}Install apk on the phone
{0}[{1}10{0}] {2}Call someone
{0}[{1}11{0}] {2}Problem with the connection  
{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}p{0}] Next Page                      
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)


def ricerca_file(cartella1):
    try:
        name=cartella1
        path1=f"C:\\Users\\{username}\\Desktop"
        count=0
        for root, dirs, files in os.walk(path1):
            if name in files:
                print("\n")
                print("Il file e' stato trovato!!!!\n")
                path=os.path.join(root, name)
                count=count+1
            else:
                pass
        if(count==0):
            print("File non trovato...\n")
            time.sleep(1)
            sys.exit()
        return path

    except UnboundLocalError:
        pass

def main():
    page_num = 1
    option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")
    if option == '1':
        os.system("adb devices -l")
        main()

    elif option == '2':
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name(IP).").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(log) "+Fore.WHITE + "> ")
        os.system('adb -s '+device_name+" logcat ")
        main()

    elif option == '3':
        os.system("adb devices -l")
        device_name= input(("\n[{0}+{1}]Enter a device name(IP): ").format(Fore.RED, Fore.WHITE))
        #device_name = "192.168.1.13"
        os.system("adb -s " +device_name+ " shell dumpsys battery")
        main()

    elif option == '4':
        connect = Fore.RED + "│" + Fore.WHITE
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name(IP).").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
        print (("     "+connect))
        file_location = "/storage/emulated/0/DCIM"
        print (("        "+connect))
        nome=input("Nome cartella dove inserire le foto: ")
        place_location=f"C:\\Users\\{username}\\Desktop\\Ricordi\\" + nome
        os.system("adb -s "+device_name+" pull "+ file_location+" "+ place_location)
        print("Finito passaggio da cellulare a pc\n")
        avvio_git("upload")
        t.sleep(1)
        main()

    elif option == '5':
        connect = Fore.RED + "│" + Fore.WHITE
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name(IP).").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(battery) "+Fore.WHITE + "> ")
        print (("     "+connect))
        file_location = "/storage/emulated/0/Music"
        print (("        "+connect))
        nome1=input("Nome cartella dove inserire la musica: ")
        place_location=f"C:\\Users\\{username}\\Desktop\\Ricordi\\" + nome1
        os.system("adb -s "+device_name+" pull "+file_location+" "+ place_location)
        print("Finito\n")
        t.sleep(1)
        main()

    elif option == '6':
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name(IP).").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(battery) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " shell pm list packages -f")
        main()

    elif option == '7':
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(mac_inet) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " shell ip address show wlan0")
        main()

    elif option == '8':
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(device_reboot) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+ " reboot ")
        print("Dispositivo riavviato\n")
        t.sleep(2)
    #da controllare
    elif option == '9':
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(device_reboot) "+Fore.WHITE + "> ")
        nome=input("Inserisci nome dell apk con anche l'estensione!: ")
        path=ricerca_file(nome)
        installazione="adb" + " " + "install" + " " + "-k" + " " + path 
        os.system(installazione)
        print("Installazione apk completata\n")
        t.sleep(2)
    
    elif option == '10':
        os.system("adb devices -l")
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(device_reboot) "+Fore.WHITE + "> ")
        telefono=input("Inserisci il numero di telefono: ")
        avvio="adb" + " " + "-s" + " " + device_name + " " + "shell" + " " + "am" + " " + "start" + " " + "-a" + " " + "android.intent.action.CALL"  + " " + "-d" + " " + "tel:" + telefono
        os.system(avvio)
        print("Sto chiamando\n")
        t.sleep(2)

    elif option == '11':
        print(Fore.CYAN + "A) Collega il cellulare al computer\n")
        print(Fore.CYAN + "B) Metti opzione 'Trasferisci File' dal cellulare ovviamente :D\n")
        print(Fore.CYAN + "C) Alla fine della procedura dovrebbe comparire il dispositivo con il suo IP\n")
        press=input(" Scrivi una lettera a caso e poi premi invio... quando hai fatto: ")
        dir= "adb" + " "
        tcpip=dir + " " + "tcpip" + " " + "5555"
        connect=dir + " " + "connect" + " " + hostname + ":5555"
        procedura=tcpip + " " + "&&"  + " " + connect
        os.system(procedura)
        os.system("adb devices -l")
        main()

    elif option == '0':
        global page_2
        if page_2 == True:
            clear1(page_2)
            main()
        else:
            clear1(page_1)
            main()

    elif option == '99':
        print("Uscita in corso...\n")
        t.sleep(1)
        exit()


try:
    print(Fore.GREEN + "HINT:\n1) IL CELLULARE E IL PC DEVONO ESSERE CONNESSI SULLA STESSA RETE\n2)DEVI ATTIVARE LA MODALITA' SVILUPPATORE(guarda in internet come fare)\n3)NELL'OPZIONE SVILUPPATORE ATTIVARE LA VOCE DEBUG USB\n4)INSTALLARE adb\n5)FINE\n")
    t.sleep(2)
    hostname=input("Insert IP of the device: ")
    #print(f'\nPingo {hostname} per vedere se è connesso alla stessa rete..\n')
    #r=ping('192.168.1.13', verbose=True)
    t.sleep(1)
    kill= "start" +  " "  + "adb" + " " + "kill-server"
    connect="start"+  " " + "adb" + " " + "connect" + " " + hostname + ":5037"
    print (Fore.RED + "Starting  adb server..")
    os.system(kill)
    t.sleep(5)
    os.system(connect)
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3])
    print (Fore.RED + banner_title)  
    print (page_1)
    main()
except KeyboardInterrupt:
    main()



