import os
import time
import webbrowser
import pyperclip


                      ###ПРОСТО НЕФ ДЕЛАТЬ)###
print("////         ////            //////          //////////////////////         /////        /////")
print("////         ////           ////////          //////////////////////         /////       /////")
print("////         ////          ////  ////         /////            /////         /////      /////")
print("////         ////         ////    ////        /////            /////         /////     /////")
print("/////////////////        ////      ////       /////                          /////    /////")
print("/////////////////       ////        ////      /////                          //////////////")
print("////         ////      //////////////////     /////                          //////////////")
print("////         ////     ////////////////////    /////              /////       /////     /////")
print("////         ////    ////              ////   /////             /////        /////      /////")
print("////         ////   ////                ////  //////////////////////         /////       /////")
print("////         ////  ////                  //// /////////////////////          /////        /////")
print("")
print("")
print("")
print("")



                     ###Выбор###
print("    1. IP    (Информация Об Ip)")
print("    2. IpTorrent (Просмотр загрузок)")
print("    3. BSSID (Идентификация базового набора услуг) ")
print("    4. IPLogger (регистрация IP-адреса)")
print("    5. Остановить программу")
print("")


#Выбрать номер 1 или 2
choose=input (":")

#Проверка номера 1
if choose=="1":

       #Очистить
        os.system('CLS')



        #Инфа
        print("")
        print("                 Введи ip в строку ниже ")
        print("")




        #Написать ip
        ip = input ("   IP адрес: ")

        time.sleep(2)

        #Вывести ip'шник на экран
        print("")
        print("   [+] - Выбранный IP адрес:", ip)

        print("")
        print("")
        print("")

        time.sleep(4)

        #Найти инфу ip
        webbrowser.open('https://ru.infobyip.com/ip-'+ ip +'.html')

        time.sleep(5)

        #Инфа
        print("Created by Shurup")
        time.sleep(2)

#Проверить номер 2
if choose=="2":

        #Очистить
         os.system('CLS')



         #Инфа
         print("")
         print("                 Введи ip в строку ниже ")
         print("")




         torrent = input ("  Выбранный ip адрес: ")


         time.sleep(2)

         #Показ ip'шника
         print("")
         print("   [+] - Выбранный ip адрес:", torrent)



         time.sleep(4)

         #Сайт
         webbrowser.open('https://iknowwhatyoudownload.com/ru/peer/?ip='+ torrent)


         time.sleep(5)

         #Инфа
         print("Created by Shurup")
         time.sleep(2)

#Проверка номера 3
if choose=="3":

     #Очистка
      os.system('CLS')



      #Инфа
      print("")
      print("                 Введите ip в строку ниже ")
      print("")



      #BSSID
      bssid = input ("   BSSID: ")

      #Вывести BSSID
      print("")
      print("   [+] - BSSID выбран:", bssid)
      print("")

      time.sleep(2)



      #Сайт BSSID адрес
      webbrowser.open('http://api.mylnikov.org/geolocation/wifi?bssid='+ bssid)

      time.sleep(5)

      #Инфа
      print("Created by shurup")
      time.sleep(2)

#Проверка номера 4
if choose=="4":

        #Очистка
        os.system('CLS')


        #Инфа
        print("")
        print("                     Запуск службы IPLogger")
        print("")



        #Сайт
        pyperclip.copy('https://2no.co/1pnm37.js')

        print(" [*] - Link copied: https://2no.co/1pnm37.js")

        time.sleep(4)

        #Начать IPLogger
        webbrowser.open("http://iplogger.ru/logger/67aktn1pnm37/")


        time.sleep(5)

        #Инфа
        print("Created by Shurup")
        time.sleep(2)
#проверка номера 5
if choose=="5":
               os.system('CLS')
               print("Остановка скрипта...")
               time.sleep(1)
               #Остановка скрипта
               exit(0)
