import simplejson as json
import cgi
from dosql import *

def index(req):
	x = doSql()
	
	receipt_num = x.execqry("select ();", False)
	
	receipt = x.execqry("select ()", False)
	
	result = []
	
	for a in receipt:
		
	