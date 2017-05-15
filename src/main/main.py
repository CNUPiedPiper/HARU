from os.path import abspath
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, abspath('../functions'))
import functions

response = [functions.__dict__.get(func) for func in dir(functions)
                if isinstance(functions.__dict__.get(func), types.FunctionsType)]
