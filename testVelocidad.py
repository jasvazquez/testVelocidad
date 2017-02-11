#!/usr/bin/python2
# coding=UTF-8

import ushlex as shlex
import os, sys, subprocess

import sqlite3
from collections import namedtuple

import simplejson as json

import pygal
import datetime

def getDirectorioEjecucionScript():
	return os.path.dirname(os.path.abspath(__file__))
	
## FICHERO BD (SqLite) con datos de la aplicación
FICHERO_BD=getDirectorioEjecucionScript()+'/velocidades.db'
	
def namedtuple_factory(cursor, row):
    """
    Uso:
    con.row_factory = namedtuple_factory
    """
    fields = [col[0] for col in cursor.description]
    Row = namedtuple("Row", fields)
    return Row(*row)
    
def db_execute(sql, datos):
	
	con = sqlite3.connect(FICHERO_BD)
	con.row_factory = namedtuple_factory
	cur = con.cursor()
	
	cur.execute(sql, datos)	
	con.commit()

# Invocar un servidor concreto de SpeedTest (7685) --> invocarComando("speedtest"," --json --server {S}", S=7385) 

def invocarComando(comando, params, **sustituciones):
	
	# IDEA patrón decorador
	if config['entorno']=='D':
		rsdo='{"download": 37788675.986478955, "timestamp": "2017-02-06T18:55:18.024380", "ping": 88.011, "upload": 2796322.6507512033, "server": {"latency": 88.011, "name": "Sevilla", "url": "http://speedtest.sev.adamo.es/speedtest/upload.php", "country": "Spain", "lon": "-5.9869", "cc": "ES", "host": "speedtest.sev.adamo.es:8080", "sponsor": "Adamo", "url2": "http://speed.sev.adamo.es/speedtest/upload.php", "lat": "37.3772", "id": "5487", "d": 41.073372033169306}}'
	else:
		vals=shlex.split(params)
		if len(sustituciones)>0:
			vals=[x.format(**sustituciones) for x in vals]	
		convert = subprocess.check_output([comando]+vals)
		rsdo=str(convert)
		
	return json.loads(rsdo)

def getAnotacionesSemanales():
	# TODO implementar 'select' a la BD
	return 	[
				{ "dia" : """2017-02-07""", "max_ping" : """113.771""", "avg_ping" : """90.6546666666667""", "min_ping" : """81.384""", "max_bajada" : """24.4781403170456""", "avg_bajada" : """20.2730597238812""", "min_bajada" : """13.2055103784335""", "max_subida" : """3.09292332230586""", "avg_subida" : """2.96405310906295""", "min_subida" : """2.81179095514377""" },
				{ "dia" : """2017-02-08""", "max_ping" : """114.991""", "avg_ping" : """91.9907777777778""", "min_ping" : """78.938""", "max_bajada" : """46.0563639650376""", "avg_bajada" : """24.0650956913638""", "min_bajada" : """6.80702860741628""", "max_subida" : """3.35004730077555""", "avg_subida" : """2.87022332932429""", "min_subida" : """2.41445603005469""" },
				{ "dia" : """2017-02-09""", "max_ping" : """120.304""", "avg_ping" : """88.3216666666667""", "min_ping" : """78.147""", "max_bajada" : """45.703996606504""", "avg_bajada" : """26.3445890659491""", "min_bajada" : """7.96970023204263""", "max_subida" : """3.35515793642163""", "avg_subida" : """2.84024639108092""", "min_subida" : """1.99096124551157""" },
				{ "dia" : """2017-02-10""", "max_ping" : """165.028""", "avg_ping" : """95.706""", "min_ping" : """75.985""", "max_bajada" : """45.8590445983241""", "avg_bajada" : """22.0138659418411""", "min_bajada" : """8.06844512621522""", "max_subida" : """3.26924579763993""", "avg_subida" : """2.92126476368912""", "min_subida" : """2.76515263362812""" },
			]

def insertarMedicion(ping, bajada, subida, servidor):
	
	# IDEA patrón decorador
	if config['entorno']=='D':
		print("Anotamos ID: {S} -- {P} ms -- {D} Mbits/s -- {U} ".format(S=servidor,P=ping,D=bajada,U=subida))
		
	t_ins=(ping,bajada,subida,servidor)
	c=db_execute('insert into anotacion (ping, bajada, subida, server) values (?,?,?,?)',t_ins)

def setConfig(nombFichero):
	global config
	with open(nombFichero) as data_file:    
		config = json.load(data_file)

dia=[]
max=[]
min=[]
avg=[]

anotaciones=getAnotacionesSemanales()

for a in anotaciones:
	
	# IDEA traducir día de la semana (Monday, Tuesday, ...) al castellano
	
	dia.append(datetime.datetime.strptime(a['dia'], "%Y-%m-%d").strftime("%a %d/%b"))
	max.append(float(a['max_bajada']))
	min.append(float(a['min_bajada']))
	avg.append(float(a['avg_bajada']))


from pygal.style import CleanStyle

chart = pygal.Line(fill=True)
chart.title = 'BAJADA semanal'
chart.x_labels = dia #map(str, range(2002, 2013))
chart.add('Max', max)
chart.add('Avg', avg)
chart.add('Min', min)
chart.render()

chart.render_to_file('chart.svg')  

quit()
		
setConfig('./config.json')
r=invocarComando("speedtest"," --json")
insertarMedicion(r['ping'],r['download']/10**6,r['upload']/10**6,r['server']['id'])
