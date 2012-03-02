#! /usr/bin/python

# 
#  cptest.py
#  minecraftsite
#  
#  Created by Jay Roberts on 2010-10-19.
# 

import cherrypy
import telnetlib
from bottle import template

class DrumtimeSite:
    @cherrypy.expose
    def index(self):
        return template('home')

cherrypy.quickstart(DrumtimeSite(), '/', 'config.ini')