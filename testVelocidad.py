#!/usr/bin/python2
# coding=UTF-8

import ushlex as shlex
import os, sys, subprocess
import sqlite3
from collections import namedtuple

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
	return 	"Ping: 88.273 ms \n"\
	"Download: 9.23 Mbit/s \n" \
	"Upload: 3.01 Mbit/s"

def insertarMedicion(ping, bajada, subida):
	t_ins=(ping,bajada,subida)
	c=db_execute('insert into anotacion (ping, bajada, subida) values (?,?,?)',t_ins)

insertarMedicion("73 ms","12.72 Mbits/s","2.34 Mbits/s")	
quit()

rsdo=mock_invocarComando("speedtest"," --simple --server 7385")

for r in rsdo.rstrip().split('\n'):
	valor=r.split(":")[1].strip()
	print ">>> {L}".format(L=valor)
