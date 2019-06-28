from __future__ import unicode_literals

import cherrypy

import sideboard.server

if __name__ == '__main__':
    app_conf = {}
    cherrypy.config.update({
        'global': {
             'engine.autoreload.on' : False
         }
    })
    cherrypy.tree.mount(root=None, config=app_conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
