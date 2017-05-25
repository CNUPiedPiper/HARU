from os.path import abspath
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import functions
import types

response = [functions.__dict__.get(func) for func in dir(functions)
                if isinstance(functions.__dict__.get(func), types.FunctionType)]
