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
        connection = pymongo.Connection('jericho.gloryfish.org')
        self.db = connection.drumtime

    @cherrypy.expose
    def index(self):
        return template('home')
        
    @cherrypy.expose
    def times(self, tag = None):
        times = None
        if tag:
            times = self.db.times.find({"tags": tag}).sort("date")
        else:
            times = self.db.times.find().sort("date")
            
        response = []
        for time in times:
            response.append(time)
            
        if len(response) == 0:
            raise cherrypy.HTTPError(404)
        else:
            return json.dumps(response, default=json_util.default)

    @cherrypy.expose
    def tags(self):
        tags = dict()
        tag_groups = self.db.times.distinct("tags")
        for tag_group in tag_groups:
            for tag in tag_group:
                tags[tag] = tag
        tags = tags.keys()
        tags.sort()
        return json.dumps(tags, default=json_util.default)

cherrypy.quickstart(DrumtimeSite(), '/', 'config.ini')
