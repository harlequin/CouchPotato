from app.lib.plugin.bones import PluginBones
import cherrypy
from app.core import getLogger
from app.core import env_

log = getLogger(__name__)
class Frontend(PluginBones):
    '''
    Provides an interterface for plugins to register with the frontend
    '''


    def postConstruct(self):
        self.tabs = {}
        self._listen('frontend.route.register', self.registerRoute)
        self.frontend = env_.get('frontend')

    def registerRoute(self, event, config):
        route = event.input
        self.frontend.addRoute(route)


    def export(self):
        return {
            'frontend' : (
                          'discoverTabs'
                          )
                }

    def addTab(self, name, title, controller):
        pass

    def addSmallTab(self, name, title, controller):
        pass

