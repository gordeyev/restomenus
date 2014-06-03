#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from menu.models import MenuRuUrls, NovikovUrls, AllResto

from grab import Grab

def home(request):
	context = {}
	return render(request, 'menu/home.html', context)

def menu_ru_urls(request):
	menu_ru = MenuRuUrls.objects.all()
	context = {'menu_ru': menu_ru}
	return render(request, 'menu/test.html', context)

def novikov_urls(request):
	menu_ru = NovikovUrls.objects.all()
	context = {'menu_ru': menu_ru}
	return render(request, 'menu/test.html', context)

def menu_ru_to_db():
	f = open("menu/menu_urls/menu_from_google.txt", "r")
	for k in f:
		menu_ru = MenuRuUrls(url=k)
		menu_ru.save()

	f.close()

def novikov_to_db():
	f = open("menu/menu_urls/novikov_from_google.txt", "r")
	for k in f:
		menu_ru = NovikovUrls(url=k)
		menu_ru.save()

	f.close()

def parse_menu_ru_page(page_url='http://menu.ru/places/menu/place/633279'):
	g = Grab()
	g.go(page_url)
	menu = g.doc.select("//*[@id='results_menu']/div").selector_list[1].select("//div[contains(@class, 'dishes_item')]").selector_list[0]
	f = open("menu_html.html", "w")
	f.write(menu.html().encode('utf8'))
	print "Ok"

	