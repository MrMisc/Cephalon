import re
from turtle import position
import discord
import numpy as np
import pandas as pd
import string
import numexpr as ne
from sympy import Derivative, Symbol, symbols
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands, tasks
import datetime
import itertools
from datetime import datetime, timezone, date
import matplotlib.pyplot as plt
from matplotlib import colors
from plotly.offline import plot
from matplotlib.ticker import PercentFormatter
import os
import requests
import schedule
import asyncio
import time
import random
import queue
from urllib.request import Request, urlopen
import sched
from bs4 import BeautifulSoup
import numexpr as ne

from urllib.request import Request, urlopen
from urllib.error import HTTPError ####
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from PIL import Image
import seaborn as sns
import math
import matplotlib as faggot
import pickle

from threading import Thread



intents = discord.Intents.default()
intents.members = True


Bot = discord.Client(intents=intents)

client = commands.Bot(command_prefix = '$', intents = discord.Intents.default())

colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
async def click():
    await client.wait_until_ready()
    while not client.is_closed():
        animalswikia = f'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=SGD'
        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        txt = soup.find('p',{'class':"result__BigRate-sc-1bsijpp-1 iGrAod"}).text
        rate = float(txt.split(' S')[0])           
        print(f"Conversion rate from 1 USD to SGD is {rate}")
        def notin(x,list):
            index=1
            for i in list:
                if i.lower().__contains__(x.lower()):
                    index*=0
                else:
                    pass
            return index!=0        
        channel = client.get_channel(620972804040556556)  
        naughtychannel = client.get_channel(1025006103400042537)        
        if True: 
            #Drop check
            link_template = f"https://drop.com/mechanical-keyboards/drops/newest?"
            Req = Request(link_template)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')
            IMG=[x.find('img')['data-src'] for x in soup.find('div',{'class':'massdrop__scroll_loader'}).find_all('div',{'class':'DropCard__drop_img__nAn9b'})]
            ListofNames = [x.div.div.div.text for x in soup.find('div',{'class':'massdrop__scroll_loader'}).find_all('div',{'class':'DropCard__body_container__3N3Sy'})]
            _Prices_ = [x.div.div.find_all('div')[2].text.split('$')[1] if len(x.div.div.find_all('div'))>1 else "Fuck this product. They don't want to show their price because of their mini peenie." for x in soup.find('div',{'class':'massdrop__scroll_loader'}).find_all('div',{'class':'DropCard__body_container__3N3Sy'}) ]
            LINKS = ['https://drop.com'+x.find('a')['href'] for x in soup.find('div',{'class':'massdrop__scroll_loader'}).find_all('div',{'class':'Grid__gridItemInner__1hwGE'})]
            #Now that the information has been gathered we are to compare it and store with previous dives
            OLD = [[ListofNames[i],_Prices_[i],IMG[i],LINKS[i]] for i in range(len(ListofNames))]
            print("Here is DROP's current list of products...")
            print(OLD)
            try:
                importedpickle = open('drop1','rb')
                NEW = pickle.load(importedpickle)
                importedpickle.close()
            except:
                os.makedirs(os.dirname('drop1'), exist_ok=True)
                importtopickle = open('drop1','wb')
                pickle.dump(OLD,importtopickle)
                importtopickle.close()            
                print("The above appears to be an empty list")
                NEW=OLD
            ##COMPARISON
            print(f"Length of drop site entry list now is {len(OLD)}, as possibly opposed to {len(NEW)}")
            backuppickle = open('drop2','wb')        
            pickle.dump(NEW, backuppickle)
            backuppickle.close()
            print("Now when we attempt to sort this list, we get...")
            NEW.sort()
            OLD.sort()         
            NEW_ListofNames = [x[0] for x in NEW]
            new_entries = [x for x in OLD if notin(x[0],NEW_ListofNames)==True]
            # new_entries = set(OLD).difference(set(NEW))
            print(new_entries)   
            #Save the new entries
            uwupickle = open('dropdifference','wb')
            pickle.dump(new_entries,uwupickle)
            uwupickle.close()
            rewritetoimportedpickle = open('drop1','wb')
            print("Going to dump into sample here")
            pickle.dump(OLD,rewritetoimportedpickle)
            rewritetoimportedpickle.close()    
            #Let's write the messages inside new_entries_list_ :D     
            for i in new_entries:
                colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
                colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
                colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]            
                emb_message = discord.Embed(title = i[0], color = random.choice(colours))      
                emb_message.set_author(name = "Drop New Arrivals", icon_url = "https://cdn.discordapp.com/attachments/891562421221732363/1020943653058916392/drop.PNG")
                stringofprice = ''
                try:stringofprice+=f"{float(i[1])*rate}"+' '
                except:stringofprice+=f"{i[1]}"+' '
                emb_message.add_field(name = 'Price', value = f"{float(i[1])*rate:.2f}")         
                try:emb_message.set_thumbnail(url = i[2])
                except:pass
                emb_message.add_field(name = 'LINK', value = i[3])
                await channel.send(content = None, embed = emb_message)         
        # except Exception as e:
        #     await channel.send(f"Error received for Drop search @ {datetime.now()}")
        #     await channel.send(e)
        # try:
        #     #KBDFans general new entries
        #     link_template = f"https://kbdfans.com/collections/new-arrival"
        #     Req = Request(link_template)
        #     uClient = urlopen(Req)
        #     soup = BeautifulSoup(uClient.read(), 'html5lib')
        #     try:IMG = ["https:"+x.find('div',{'class':'rimage-background'}).find('noscript').find('img')['src'] for x in soup.find_all('div',{'class':'product-block'})]
        #     except:IMG = ['','','']
        #     ListofNames = [x.find('div',{'class':'product-block__title'}).text.split('\n')[1] for x in soup.find_all('div',{'class':'product-block'})]
        #     _Prices_ = [[y.text for y in x.find('div',{'class':'product-price'}).find_all('span')] for x in soup.find_all('div',{'class':'product-block'})]
        #     LINKS = ["https://kbdfans.com"+x.find('a')['href'] for x in soup.find_all('div',{'class':'product-block'})]
        #     #Now that the information has been gathered we are to compare it and store with previous dives
        #     OLD = [[ListofNames[i],_Prices_[i],IMG[i],LINKS[i]] for i in range(len(ListofNames))]
        #     try:
        #         importedpickle = open('kbd1_newarrival','rb')
        #         NEW = pickle.load(importedpickle)
        #         importedpickle.close()
        #     except:
        #         importtopickle = open('kbd1_newarrival','wb')
        #         pickle.dump(OLD,importtopickle)
        #         importtopickle.close()            
        #         print("The above appears to be an empty list")
        #         NEW=OLD
        #     ##COMPARISON
        #     backuppickle = open('kbd2_newarrival','wb')        
        #     pickle.dump(NEW, backuppickle)
        #     backuppickle.close()
        #     print("Now when we attempt to sort this list, we get...")
        #     NEW.sort()
        #     OLD.sort()         
        #     NEW_ListofNames = [x[0] for x in NEW]
        #     new_entries = [x for x in OLD if notin(x[0],NEW_ListofNames)==True]
        #     # new_entries_list=[x for x in new_entries]
        #     # new_entries_list_Names = [x[0] for x in new_entries_list]
        #     # new_entries_list_=[]
        #     # new_entries_list_ = [x for x in new_entries_list if x[0] not in new_entries_list_Names]  #to remove duplicates
        #     print(new_entries)   
        #     #Save the new entries
        #     uwupickle = open('kbddifference_newarrival','wb')
        #     pickle.dump(new_entries,uwupickle)
        #     uwupickle.close()
        #     rewritetoimportedpickle = open('kbd1_newarrival','wb')
        #     print("Going to dump into sample here")
        #     pickle.dump(OLD,rewritetoimportedpickle)
        #     rewritetoimportedpickle.close()    
        #     #Let's write the messages inside new_entries_list_ :D     
        #     for i in new_entries:
        #         colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
        #         emb_message = discord.Embed(title = i[0], color = random.choice(colours))      
        #         emb_message.set_author(name = "KBDFans New Arrivals", icon_url = "https://cdn.shopify.com/s/files/1/1473/3902/files/logo_6th_aa1039bc-a5a2-495f-aeaf-ad4f2d2a6fcb_180x.png?v=1662700576")
        #         stringofprice = ''
        #         for j in i[1]:stringofprice+=j+' '  
        #         print(i[1])
        #         emb_message.add_field(name = 'Price', value = f"{float(i[1].split(' ')[0])*rate:.2f}")         
        #         emb_message.set_thumbnail(url = i[2])
        #         emb_message.add_field(name = 'LINK', value = i[3])
        #         await channel.send(content = None, embed = emb_message)       
        # except Exception as e:
            # await channel.send(f"Error when diving for KBDfans site general new entries @ {datetime.now()}")
            # await channel.send(e)
        # try:
        #     #KBDFans attempt - searching for SA specifically
        #     # try:
        #     searchphrase = "SA"
        #     pageno = 1
        #     rarity = 0
        #     link_template = f"https://kbdfans.com/search?options%5Bprefix%5D=last&page={pageno}&q={searchphrase.replace(' ','+')}&type=product"
        #     #https://kbdfans.com/search?options%5Bprefix%5D=last&page=1&q=sa&type=product
        #     Req = Request(link_template)
        #     uClient = urlopen(Req)
        #     soup = BeautifulSoup(uClient.read(), 'html5lib')
        #     IMG = ["https:"+x.find('div',{'class':'rimage-background'}).find('noscript').find('img')['src'] for x in soup.find_all('div',{'class':'product-block'})]
        #     ListofNames = [x.find('div',{'class':'product-block__title'}).text.split('\n')[1] for x in soup.find_all('div',{'class':'product-block'})]
        #     _Prices_ = [[y.text for y in x.find('div',{'class':'product-price'}).find_all('span')] for x in soup.find_all('div',{'class':'product-block'})]
        #     LINKS = ["https://kbdfans.com"+x.find('a')['href'] for x in soup.find_all('div',{'class':'product-block'})]
        #     #Now that the information has been gathered we are to compare it and store with previous dives
        #     OLD = [[ListofNames[i],_Prices_[i],IMG[i],LINKS[i]] for i in range(len(ListofNames))]
        #     try:
        #         importedpickle = open('kbd1','rb')
        #         NEW = pickle.load(importedpickle)
        #         importedpickle.close()
        #     except:
        #         importtopickle = open('kbd1','wb')
        #         pickle.dump(OLD,importtopickle)
        #         importtopickle.close()            
        #         print("The above appears to be an empty list")
        #         NEW=OLD
        #     ##COMPARISON
        #     backuppickle = open('kbd2','wb')        
        #     pickle.dump(NEW, backuppickle)
        #     backuppickle.close()
        #     print("Now when we attempt to sort this list, we get...")
        #     NEW.sort()
        #     OLD.sort()         
        #     NEW_ListofNames = [x[0] for x in NEW]
        #     new_entries = [x for x in OLD if notin(x[0],NEW_ListofNames)==True]
        #     new_entries_list=[x for x in new_entries]
        #     new_entries_list_Names = [x[0] for x in new_entries_list]
        #     new_entries_list_=[]
        #     new_entries_list_ = [x for x in new_entries_list if x[0] not in new_entries_list_Names]  #to remove duplicates
        #     print(new_entries_list_)   
        #     #Save the new entries
        #     uwupickle = open('kbddifference','wb')
        #     pickle.dump(new_entries_list_,uwupickle)
        #     uwupickle.close()
        #     rewritetoimportedpickle = open('kbd1','wb')
        #     print("Going to dump into sample here")
        #     pickle.dump(OLD,rewritetoimportedpickle)
        #     rewritetoimportedpickle.close()    
        #     #Let's write the messages inside new_entries_list_ :D     
        #     for i in new_entries_list_:
        #         emb_message = discord.Embed(title = i[0], color = random.choice(colours))      
        #         emb_message.set_author(name = "KBDFans New SA keycap arrivals", icon_url = "https://cdn.shopify.com/s/files/1/1473/3902/files/logo_6th_aa1039bc-a5a2-495f-aeaf-ad4f2d2a6fcb_180x.png?v=1662700576")
        #         stringofprice = ''
        #         for j in i[1]:stringofprice+=i+' '
        #         emb_message.add_field(name = 'Price', value = stringofprice)         
        #         try:emb_message.add_field(name = 'Price', value = stringofprice)
        #         except:emb_message.set_thumbnail(url = i[2])
        #         emb_message.add_field(name = 'Price', value = i[3])
        #         await channel.send(content = None, embed = emb_message)
        # except Exception as e:
            # print(f"Dive into KBDfans failed for SA keycaps specifically @ {datetime.now()}. Sorry shisho :c")
            # await channel.send(f"Dive into KBDfans failed @ {datetime.now()}. Sorry shisho :c")        
            # await channel.send(e)
        #Etsy attempt
        if True:   #Replace with try again when you done with error handling
            client_search_term = "SA keycaps"
            keyword = " SA"
            pageno = 1
            rarity = 0
            link_template = f"https://www.etsy.com/market/{client_search_term.lower().replace(' ','_')}?ref=pagination&page={pageno}&order=date_desc"   #But this is the search results ordered by time
            Req = Request(link_template)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')
            # print([x.text for x in soup.find(id="search-results").find_all('li')][0])
            # print(soup.find_all('li',{'class':'wt-list-unstyled wt-grid__item-xs-6 wt-grid__item-md-4 wt-grid__item-lg-3 wt-order-xs-2 wt-order-md-2 wt-order-lg-0 wt-show-xs wt-show-md wt-show-lg wt-position-relative'}))

            print(soup.find(id="search-results").find_all('li')[0].find('a')['href'])
            LINKS = [x.find('a')['href'] for x in soup.find(id="search-results").find_all('li')]
            # print(f"Title should be: {soup.find(id='search-results').find_all('li')[4].find('div',{'class':'v2-listing-card__info'}).h2.text}")
            no=5

            #Early version of attempt at printing titles
            # print(f"First {no} Titles should be: {[x.find('div',{'class':'v2-listing-card__info'}).h2.text for x in soup.find(id='search-results').find_all('li')][:no]}")
            Products_ = [x.find('div',{'class':'v2-listing-card__info'}).h2.text for x in soup.find(id='search-results').find_all('li')]
            TOTAL_NO = len(soup.find(id='search-results').find_all('li'))

            print("--------")
            print("Prices would be...")

            Prices = [[y.text for y in x.find('div',{'class':'v2-listing-card__info'}).find('div',{'class':'n-listing-card__price'}).find_all('p')] for x in soup.find(id='search-results').find_all('li')]
            # Prices1 = [[y.text for y in x.find('div',{'class':'v2-listing-card__info'}).find('div',{'class':'n-listing-card__price'}).find_all('span',{'class':'currency-value'})] for x in soup.find(id='search-results').find_all('li')]
            print("***")
            #Hardcore price list is Prices1
            Prices1 = [[y.text for y in x.find('div',{'class':'v2-listing-card'}).find('div',{'class':'n-listing-card__price'}).find_all('span',{'class':'currency-value'})] for x in soup.find(id='search-results').find_all('li')]
            PriceSymbols = [[y.text for y in x.find('div',{'class':'v2-listing-card'}).find('div',{'class':'n-listing-card__price'}).find_all('span',{'class':'currency-symbol'})] for x in soup.find(id='search-results').find_all('li')]

            # Price = [[value+' '+currency for value in values for currency in currencies] for values in Prices1 for currencies in PriceSymbols]
            # Price = [[value+' '+currency for value in values for currency in currencies] for values,currencies in zip(Prices1,PriceSymbols)]
            Price = [[value+' '+currency for value,currency in zip(values,currencies)] for values,currencies in zip(Prices1,PriceSymbols)]
            print(Price)
            # print(Prices1[:no])
            A_Price = [["Sale Price:"+x[0],"Original Price:"+x[1]] for x in Price if len(x)==2]  #honestly probablky not going to use this in case we end up recording entries taht do not have 2 prices
            #THEN IT WOULDNT MATCH UP WITH Products!!!
            #This kind of worked for selenium version but lets try finding a more general version
            # try:Products = [x.split("\n                        ")[1].split("\n                ")[0] for x in Products]
            # except:pass
            # print("Checkllist for Products_")
            # for i in Products_:print(i)
            Products_ = [x.split('\n')[1] for x in Products_]
            Products = []
            for s in Products_:
                for i,x in enumerate(s):
                    if x.isalpha():         #True if its a letter
                        pos = i                   #first letter position
                        break
                new_str = s[pos:]
                Products.append(new_str)        
            # print("Check for Products")
            # for i in Products:print(i)
            Concat_prices = []
            for price_list in Price:
                if len(price_list)==2:
                    Concat_prices.append("Sale Price:"+price_list[0]+" Original Price:"+price_list[1])
                else:
                    buffet = ''
                    for i in price_list:
                        buffet+=i
                    Concat_prices.append(buffet)


            #let's add links and time (filter out posts that are not even posted within the current month)
            #Current month
            currentMonth = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(datetime.now().month)-1]
            currentDay = str(datetime.now().day)
            currentDay_=str(datetime.now().day-1)

            current = currentDay+' '+currentMonth
            current_ = currentDay_+' '+currentMonth
            currentURL = currentMonth+' '+currentDay
            current_URL = currentMonth+' '+currentDay_

            Date = []   #List of booleans
            # IMG = []  #List to contain the image of all pages
            #We go into the first link for now and try to retrieve the date 
            Sales = []
            Reviews = []
            for i in LINKS:
                link_template = i  #But this is the search results ordered by time
                Req = Request(link_template)
                uClient = urlopen(Req)
                soup = BeautifulSoup(uClient.read(), 'html5lib')
                try:Datestring = soup.find('div',{'class':'wt-display-flex-xs wt-justify-content-space-between wt-align-items-baseline wt-flex-direction-row-xs wt-mb-md-4'}).find('div',{'class':'wt-text-caption'}).text
                except:Datestring = '35 Jun, 200000'
                print(f"Needs to contain {current}")
                #Record booleans as to whether entry in question is even of today!  - feel free to adjust this condition if you are looking for more rare items!!
                if rarity == 0:
                    print(Datestring.lower().__contains__(current.lower()))
                    print(Datestring.lower().__contains__(current_.lower()))
                    print(Datestring.lower().__contains__(currentURL.lower()))
                    print(Datestring.lower().__contains__(current_URL.lower()))                
                    if datetime.now().hour<6.:  #If it is before 3am in the current day, then include previous day
                        if Datestring.lower().__contains__(current.lower()) or Datestring.lower().__contains__(current_.lower()) or Datestring.lower().__contains__(currentURL.lower()) or Datestring.lower().__contains__(current_URL.lower()):
                            Date.append(True)
                        else:
                            Date.append(False)
                    else:
                        if Datestring.lower().__contains__(current.lower()) or Datestring.lower().__contains__(currentURL.lower()):
                            Date.append(True)
                        else:
                            Date.append(False)                            
                try:Sales.append(soup.find(id='listing-page-cart').div.find('div',{'class':'wt-display-inline-flex-xs'}).find('span',{'class':'wt-text-caption'}).text)
                except:Sales.append("No sales. Product probably sucks.")
                try:reviews = [x for x in soup.find_all('div') if x.has_attr('data-reviews')][0]
                except:reviews = []
                if isinstance(reviews, list):pass
                else:
                    if len(reviews.find_all('button',{'id':'same-listing-reviews-tab'}))>0:
                        stringo = ''
                        for i in range(4):  #it is 4 because there are up to 4 reviews for each page of self reviews that we have observed
                            try:
                                stringo+="\n"+soup.find(id = 'same-listing-reviews-panel').find(id = f'review-preview-toggle-{i}').text+'\n\n'
                            except:pass
                        Reviews.append(stringo)
                    else:
                        Reviews.append("No reviews for this product")
                # IMG.append(soup.find('img')['data-src-zoom-image'])
            FinalePrices = [Prices1[i][0] for i in range(len(Prices1)) if Date[i] if Products[i].lower().__contains__(keyword.lower())]
            print(len(Products))
            print(len(Concat_prices))
            print(len(LINKS))
            print(len(Date))
            print(Date)
            OLD = ["Name:" + Products[i]+"\n"+"Price(s): "+Concat_prices[i]+"\nLink|"+LINKS[i] + "\nSales:"+Sales[i]+"\nReviews on Product|"+Reviews[i] for i in range(len(Products)) if Date[i] if Products[i].lower().__contains__(keyword.lower())]       

            try:
                importedpickle = open('n1','rb')
                NEW = pickle.load(importedpickle)
                importedpickle.close()
            except:
                while True:
                    try:
                        importtopickle = open('n1','wb')
                        break
                    except:pass
                pickle.dump(OLD,importtopickle)
                importtopickle.close()            
                print("The above appears to be an empty list")
                NEW=OLD
            ##COMPARISON
            backuppickle = open('n2','wb')        
            pickle.dump(NEW, backuppickle)
            backuppickle.close()
            print("Now when we attempt to sort this list, we get...")
            NEW.sort()
            OLD.sort()
            NEW__=[]
            OLD__=[]
            NEW__= [x for x in NEW if x.split('\n')[0] not in NEW__]
            OLD__= [x for x in OLD if x.split('\n')[0] not in OLD__]
            def notin(x,list):
                index=1
                for i in list:
                    if i.lower().__contains__(x.lower()):
                        index*=0
                    else:
                        pass
                return index!=0
            new_entries = [x for x in OLD__ if notin(x.split('\n')[0],NEW__)==True]
            new_entries_list=[x for x in new_entries]
            new_entries_list_=[]
            new_entries_list_ = [x for x in new_entries_list if x.split('\n')[0] not in new_entries_list_]  #to remove duplicates
            print(new_entries_list_)
            #Save the new entries
            uwupickle = open('ndifference','wb')
            pickle.dump(new_entries_list_,uwupickle)
            uwupickle.close()
            rewritetoimportedpickle = open('n1','wb')
            print("Going to dump into sample here")
            pickle.dump(OLD__,rewritetoimportedpickle)
            rewritetoimportedpickle.close()
            #check against etsy_megalibrary
            # while True:
            #     try:
            #         importedpickle = open('etsy_megalibrary','rb')
            #         NEW = pickle.load(importedpickle)
            #         importedpickle.close()
            #         break
            #     except Exception as e:print(e)
            importedpickle = open('etsy_megalibrary','rb')
            try:NEW = pickle.load(importedpickle)
            except:pass
            importedpickle.close()            
            NEW_ = [x for x in new_entries_list_]     
            BACKUP = np.copy(NEW_)       
            new_entries_list_=[]
            new_entries_list_ = [x for x in NEW_ if x.split('\n')[0] not in NEW]  #to remove entries that have already been recorded     
            NEW_ = new_entries_list_
            #Naughty repeats
            print("New entries are...")
            print(NEW_)
            print("vs what we think are the repeated sneaky entries")
            N = [x for x in BACKUP if x.split('\n')[0] in NEW_] 
            print(N)                    
            for i in N:
                await naughtychannel.send("NAUGHTY REPEAT ITEMS FOUND! ALERT! DON'T BUY!")
                await naughtychannel.send(i.split('\n')[0])   
            #Update etsy megalibrary
            for i in NEW_:NEW.append(i)
            # print("Mega list now is")
            # print(NEW)            
            importedpickle = open('etsy_megalibrary','wb')
            pickle.dump(NEW,importedpickle)
            importedpickle.close()                       
            colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
            stringo = ''
            count=0         
            NN=[]  #list of links we are keeping
            for x in NEW_:
                Sections = x.split('\n')
                stringo+='\n'+f"[{count}.]"
                ETSY = discord.Embed(title = f"{Sections[0].split(':')[1]}", color = random.choice(colours))
                for i in Sections[0].split(':')[1].split(' ')[:4]:
                    stringo+=i+' '
                stringo+=' '*(50-len(stringo.split('\n')[-1])) 
                if Sections[1][10].isdigit():
                    ETSY.add_field(name = 'Price', value = f"{float(Sections[1][10:].split(' ')[0])*rate} SGD" )
                    stringo+=f"{float(Sections[1][10:].split(' ')[0])*rate} SGD"
                else:
                    # print(Sections[1][21:].split(' ')[0])
                    ETSY.add_field(name = 'Price', value = f"{float(Sections[1][21:].split(' ')[0])*rate} SGD" )
                    stringo+=f"{float(Sections[1][21:].split(' ')[0])*rate} SGD"
                #Extracting link
                stringo+='     '
                if len(Sections[2].split('|')[1])<2000:
                    try:ETSY.add_field(name = 'Link', value = f"{Sections[2].split('|')[1]}" )
                    except:pass
                # stringo+=Sections[2].split('|')[1]+'        '
                stringo+='\n'
                ETSY.set_author(name = "Etsy", icon_url = "https://th.bing.com/th/id/OIP.fMDcFM0oJwZgykDHz6CTogHaHa?pid=ImgDet&rs=1")
                noofsales=Sections[3].split(':')[1]
                if noofsales!=None and noofsales!= '':ETSY.add_field(name = 'No of Sales by Seller', value = noofsales )
                else:ETSY.add_field(name = 'No of Sales by Seller', value = "Probably none" )
                #We do not use the variables sections for the reviews because the reviews in particular are the only section thus far that contains
                #\n s. The Sections list is obtained by splitting each entry by '\n' which means that we are now rendering our split useless for the 
                #reviews and so instead, we choose to just split each entry, named x in each loop, by the title we give for the Reviews
                ETSY.add_field(name = 'Reviews on Product', value = x.split('Reviews on Product|')[1][:1000])  
                # if len(NEW_)<6:
                print(f"The data that we are trying to print from etsy is from:{Sections}")
                print("To be specific")
                print(x.split('Reviews on Product|')[1][:1980])
                print(ETSY)
                print("Trying to find out which one is the empty value")
                print(f"No of sales : {noofsales}")
                print("or is it...")
                print(f"the link itself: {Sections[2].split('|')[1]}")
                await channel.send(content = None, embed = ETSY)
                count+=1
            if len(stringo)>2000:
                for i in range(0,len(stringo),1900):
                    await channel.send('```'+stringo[i:i+1900]+'```')
            else:
                await channel.send('```'+stringo+'```')

        # except Exception as e:
        #     print(f"Dive for etsy failed @ {datetime.now()}. Sorry master :c")             
        #     await channel.send(f"Dive for etsy failed @ {datetime.now()}. Sorry master :c")            
        #     await channel.send(f"Error recieved arised because {e}.")
        searchterms = open('pricewatch','rb')
        whattosearch = pickle.load(searchterms)
        searchterms.close()
        what = []
        for i in whattosearch:
            if i not in what:
                what.append(i)
        whattosearch = what     #The entries are duplicated because echo is buggy and a cunt. Instead of fixing that somehow with tradeoffs, lets just let cephy clean it!
        print(whattosearch)
        uwupickle = open('pricewatch','wb')
        pickle.dump(whattosearch,uwupickle)
        uwupickle.close()          
        for i in whattosearch:          
            try:
                print("Price point of interest is")
                print(i[1])
                Req = Request(i[0])
                uClient = urlopen(Req)
                soup = BeautifulSoup(uClient.read(), 'html5lib')
                trim = re.compile(r'[^\d.,]+')
                mystring = soup.find('p',{'class':'wt-text-title-03'}).find_all('span')[-1].text
                result = trim.sub('', mystring)
                if float(result)<i[1]-1.:
                    await channel.send(f"``` The product {soup.find('h1').text} has dropped below price point of interest - ${i[1]}! \n It stands at ${result} currently! \n Over at : {i[0]} ```")
            except:
                pass
            
        
        await asyncio.sleep(.05*60**2)


client.loop.create_task(click())










@client.event
async def on_ready():
    print("Click!")






@client.command()
@commands.has_role("Duke")
async def stop(ctx):
    await client.logout()

@client.command()
async def react(ctx):
    choices = ["┌─┐\n┴─┴\nಠ_ರೃ \n Oh, why...Hello to you too, good sir!", '{◕ ◡ ◕}']
    await ctx.send(random.choice(choices))


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()




@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return


    if 'uwu' in message.content.lower():
        choices = [ '(◯Δ◯∥)', '∑(ΦдΦlll', '（∂△∂；）', '(;Ⅲ□Ⅲ;)', '(=￣▽￣=)Ｖ', '(^ー^)ｖ', '(○ﾟε＾○)v', ':thumbsup:', 'ಠ‸ಠ', '(◎_◎;)?', '(⊙.☉)7', 'סּ_סּ' ]
        if np.random.normal()>-.8:await channel.send(random.choice(choices))



    await client.process_commands(message)

client.run('###YOUR TOKEN HERE#####')

