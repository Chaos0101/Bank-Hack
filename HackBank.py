import webbrowser
import time

time.sleep(1)
print ('Enable VPN...')
time.sleep(2)
print ('VPN Enabled Successfuly!')
time.sleep(1)
print (' ')
bank123 = input('Enter Website Of The Bank: ')
money123 = input('Enter amount: ')
time.sleep(2)
print ('Bank: '+ bank123)
time.sleep(1)
print ('Amount: '+ money123)
time.sleep(3)
print (" ")
print ('Finding The Password Of The WiFi From The Bank...')
time.sleep(4)
print ('Password Found Successfuly!')
print ('Password: ')
sure123 = input('Are you sure for this attack [Y/n]: ')
if sure123 == "Y":
     time.sleep(2)
     print ('Hacking The Password Of The Bank...')
     time.sleep(15)
     print ('[!] Failed To Find The Password !!!')
     time.sleep(2)
     bruteforce123 = input('Do you want to Brute Force The Password In Seconds? [Y/n]: ')
     if bruteforce123 == 'Y':
          print ('Brute Force The Password...')
          time.sleep(30)
          print ('Password Found Successfuly!')
          time.sleep(4)
          print ('Create a Account For The Bank To Add The Money In Your Bank Account!')
          username123 = input('Enter a Username: ')
          email123 = input('Enter a email: ')
          pass123 = input('Enter a Password: ')
          pass1234 = input('Retype The Same Password: ')
          if pass1234 == (pass123):
               print ('You Created A Account Successfuly !')
               time.sleep(2)
               print ('Adding The Money To Your Bank Account...')
               time.sleep(20)
               print ('Details:')
               print (" ")
               print ('Username: '+ username123)
               print ('Email: '+ email123)
               print ('Password: '+ pass123)
               print ('Bank Account: '+ bank123)
               print ('Amount: '+ money123)
               print ('')
               print ('Press Enter To Steal The Money')
               url = ('https://www.tomorrowtides.com/iambankhackerbruterlolstealmoneycom.html')
               webbrowser.open_new(url)
               time.sleep(1)
               print ('You Just Got...')
               time.sleep(2)
               print ('''





















                   ''')

               time.sleep(1)
               print ('You Just Got Rick Rolled!')
               time.sleep(1)
               print (':(')
               time.sleep(3)
               exit()



          else:
               print ('Wrong Password')
               time.sleep(2)
               exit()
     if bruteforce123 == 'n':
           print ('Exiting...')
           time.sleep(1)
           exit()

if sure123 == "n":
     time.sleep(1)
     print ('ByeBye')
     time.sleep(2)
     exit()