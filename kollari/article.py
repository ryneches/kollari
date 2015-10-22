import json
import markdown
import jinja2 
import sys
from os.path import islink, realpath, dirname, abspath, join
from os import listdir

def find_templates() :
    try:
        root = __file__
        if islink( root ) :
            root = realpath( root )
        basedir = dirname( abspath( root ) )
    except:
        print "Can't find templates."
        sys.exit()

    files = listdir( join( basedir, 'templates' ) )
    types = map( lambda f : f.split('.')[-1].lower(), files )
    paths = map( lambda f : join( join( basedir, 'templates' ), f) , files )
    return dict( zip( types, paths ) )



class Article(object) :
    def __init__( self, name ) :
        self.name = name
        self.sections = []
        self.templates = find_templates()

    def read_notebook( self, notebook ) :
        nb = json.load( notebook )
        for cell in nb['worksheets'][0]['cells'] :
            self.sections.append(cell)
    
    def make_html( self ) :
        with open( self.templates['html']) as f :
            T = jinja2.Template( f.read() )
        md = ''
        for section in self.sections :
            if section['cell_type'] == 'markdown' :
                md = md + '\n'.join(section['source'])
                md = md + '\n'
        return T.render( name = self.name,
                         content = markdown.markdown( md ) )

    def make_latex( self ) :
        # LaTeX clashes with Jinja's defalt delimiters, so...
        loader = jinja2.PackageLoader('kollari', 'templates')
        env = jinja2.Environment(   loader                  =   loader,
                                    trim_blocks             =   True,
                                    block_start_string      =   '@@',
                                    block_end_string        =   '@@',
                                    variable_start_string   =   '@=',
                                    variable_end_string     =   '=@',
                                    comment_start_string    =   '@#',
                                    comment_end_string      =   '#@', )
        T = env.get_template( 'article.tex' )
        md = ''
        for section in filter( lambda x : x['cell_type'] == 'markdown',  self.sections ) :
            md = md + '\n'.join( section['source'] )
            md = md + '\n'
        return T.render( name = self.name,
                         content = md )
