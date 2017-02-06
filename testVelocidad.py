#!/usr/bin/python2
# coding=UTF-8

import ushlex as shlex
import os, sys, subprocess

def invocarComando(comando, params, **sustituciones):
	vals=shlex.split(params)
	if len(sustituciones)>0:
		vals=[x.format(**sustituciones) for x in vals]	
	convert = subprocess.check_call([comando]+vals)
	return str(convert)

invocarComando("speedtest","--list")
