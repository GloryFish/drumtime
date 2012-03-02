#! /usr/bin/python

# 
#  drumtimesite.py
#  drumtime
#  
#  Created by Jay Roberts on 2012-03-02.
# 

import cherrypy
from bottle import template
import pymongo
import json
from bson import json_util

class DrumtimeSite:

    def __init__(self):
        connection = pymongo.Connection()
        self.db = connection.drumtime

    @cherrypy.expose
    def index(self):
        return json.dumps(self.db.times.find_one(), default=json_util.default)

cherrypy.quickstart(DrumtimeSite(), '/', 'config.ini')
