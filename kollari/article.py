import json

class Article(object) :
    def __init__( self ) :
        self.name = ''
        self.sections = []

    def read_notebook( self, notebook ) :
        nb = json.load( notebook )
        for cell in nb['worksheets'][0]['cells'] :
            self.sections.append(cell)
        
