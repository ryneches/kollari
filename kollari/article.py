import json

class Article(object) :
    def __init__( self ) :
        self.name = ''
        self.sections = []

    def read_notebook( self, notebook ) :
        nb = json.read( notebook )
        for cell in nb.items()[2][1][0]['cells'] :
            self.section = { 'type'     : cell['cell_type'],
                             'language' : cell['language'] }
        
