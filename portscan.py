from termcolor import colored
import socket
import os

clear = lambda: os.system('clear')


def fanc1():
    clear()
    ui()
    
    color_a = colored("[+] ", 'green')
    print("~"*50)
    host = input(color_a + "Host Name / Имя хоста --> ")
    try:
	    port = int(input(color_a + "Port / порт--> "))
	    print("~"*50)
	
	    scan = socket.socket()
	
	    color_b = colored("[!] ", 'red')
	    color_c = colored("[!] ", 'yellow')
	
	    try:
	        scan.connect((host, port))
	    except socket.error:
	        print(color_b + "Port -- ", port, " -- [CLOSED]")
	    else:
	        print(color_c + "Port -- ", port, " -- [OPEN]")
    except ValueError:
	    	print(colored('Вы ввели не число!', 'red'))
    print('\n')
    again = colored("[1]", 'green')
    home = colored("[2]", 'green')
    exit = colored("[ENTER]", 'green')
    text_a = input(again + ' - Scan another host / сканировать другой хост\n' + home + ' - Back to menu / вернуться в меню\n' + exit + ' - Leave / выйти: ')
    if text_a == '1':
    	fanc1()
    elif text_a == '2':
    	clear()
    	homee()
    elif text_a == '':
    	pass


def fanc2():
    clear()
    ui()
    
    color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    host = input(color_a + "Host adress / Адрес хоста --> ")
    print("\n")
    ports = [21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143, 194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200]

    for i in ports:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print(color_b + "Port -- ", i, " -- [CLOSED]")
        else:
            print(color_c + "Port -- ", i, " -- [OPEN]")
    print('\n')
    again = colored("[1]", 'green')
    home = colored("[2]", 'green')
    exit = colored("[ENTER]", 'green')
    text_a = input(again + ' - Scan another host / сканировать другой хост\n' + home + ' - Back to menu / вернуться в меню\n' + exit + ' - Leave / выйти: ')
    if text_a == '1':
    	fanc2()
    elif text_a == '2':
    	clear()
    	homee()
    elif text_a == '':
    	pass


def help():
	clear()
	ui()
	print(colored("Данная программа помогает посмотреть, открыт ли порт у хоста. Сайты нужно вписывать без HTTPS/HTTP. Например: example.com\n\nThis program helps you to scan host ports are open or close. Sites must be without HTTP or HTTPS. E.g.: example.com", 'yellow'))
	print('~'*50)
	home = colored("[1]", 'green')
	exit = colored("[ENTER]", 'green')
	text_a = input(home + ' - Back to menu / вернуться в меню\n' + exit + ' - Leave / выйти: ')
	if text_a == '1':
		clear()
		homee()
	elif text_a == '':
		pass
    
def news():
	clear()
	ui()
	print(colored('\tПоследние новости', 'green'))
	print('\tДобавлена вкладка новостей')
	print('\tДобавлено больше портов в списке частых портов')
	print('\tДобавлен вариант продолжения после скана')
	print('\tВыход из программы теперь есть в меню')
	#print('\t')
	print('~'*50)
	home = colored("[1]", 'green')
	exit = colored("[ENTER]", 'green')
	text_a = input(home + ' - Back to menu / вернуться в меню\n' + exit + ' - Leave / выйти: ')
	if text_a == '1':
		clear()
		homee()
	elif text_a == '':
		pass


def homee():
	ui()
	home()

def home():	
	print(colored("\t[1]", 'blue') + "--- сканировать один порт")
	print(colored("\t[2]", 'blue') + "--- сканировать список частых портов")
	print(colored("\t[3]", 'blue') + "--- помощь")
	print(colored("\t[4]", 'blue') + "--- новости")
	print(colored("\t[5]", 'blue') + "--- выйти")
	
	print("~"*50, "\n")
	text_a = input("[scan]--> ")
	
	if text_a == "1":
	    fanc1()
	elif text_a == "2":
	    fanc2()
	elif text_a == "3":
		help()
	elif text_a == "4":
		news()
	elif text_a == "5":
		pass
	else:
	    print(input(colored("Параметр введен неправильно! Нажмите ENTER, чтобы вернуться в меню.", 'red')))
	    clear()
	    home()
	    
def ui():
	print(colored("    ____  ____  ____  ______", 'green'))
	print(colored("   / __ \/ __ \/ __ \/_  __/", 'green'))
	print(colored("  / /_/ / / / / /_/ / / /   ", 'green'))
	print(colored(" / ____/ /_/ / _, _/ / /    ", 'green'))
	print(colored("/_/    \____/_/ |_| /_/     ", 'green'))
	
	print(colored("   ____________   _  __", 'green'))
	print(colored("  / __/ ___/ _ | / |/ /", 'green'))
	print(colored(" _\ \/ /__/ __ |/    / ", 'green'))
	print(colored("/___/\___/_/ |_/_/|_/  ", 'green'))
	
	print("\n")
	print("\tversion: 0.4.3")
	print("\tBy Flezzo (vk.com/flezzo)")
	
	print("~"*50)
	    
clear()
homee()