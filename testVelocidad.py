#!/usr/bin/python2
# coding=UTF-8

import ushlex as shlex
import os, sys, subprocess

import sqlite3
from collections import namedtuple

import simplejson

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

def invocarComando(comando, params, **sustituciones):
	vals=shlex.split(params)
	if len(sustituciones)>0:
		vals=[x.format(**sustituciones) for x in vals]	
	convert = subprocess.check_output([comando]+vals)
	return str(convert)

def mock_invocarComando(comando, params, **sustituciones):
	return 	'{"download": 37788675.986478955, "timestamp": "2017-02-06T18:55:18.024380", "ping": 88.011, "upload": 2796322.6507512033, "server": {"latency": 88.011, "name": "Sevilla", "url": "http://speedtest.sev.adamo.es/speedtest/upload.php", "country": "Spain", "lon": "-5.9869", "cc": "ES", "host": "speedtest.sev.adamo.es:8080", "sponsor": "Adamo", "url2": "http://speed.sev.adamo.es/speedtest/upload.php", "lat": "37.3772", "id": "5487", "d": 41.073372033169306}}'

def insertarMedicion(ping, bajada, subida, servidor):
	t_ins=(ping,bajada,subida,servidor)
	c=db_execute('insert into anotacion (ping, bajada, subida, server) values (?,?,?,?)',t_ins)

# TODO recuperar trigger e ID autonumerico

rsdo=mock_invocarComando("speedtest"," --json --server {S}", S=7385)
r = simplejson.loads(rsdo)
print "Anotamos ID: {S} -- {P} ms -- {D} Mbits/s -- {U} ".format(S=r['server']['id'],P=r['ping'],D=r['download']/10**6,U=r['upload']/10**6)
insertarMedicion(r['ping'],r['download']/10**6,r['upload']/10**6,r['server']['id'])
