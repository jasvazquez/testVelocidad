#!/usr/bin/python2
# coding=UTF-8

import ushlex as shlex
import os, sys, subprocess

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

rsdo=mock_invocarComando("speedtest"," --simple --server 7385")

for r in rsdo.rstrip().split('\n'):
	print ">>> {L}".format(L=r)
