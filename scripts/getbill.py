from dosql import *
import cgi
import simplejson as json


def index(req, pldtNum):	
	pldtNum = cgi.escape(pldtNum)
	
	
	x = doSql()	
	res = x.execqry("select * from pldtaccount where pldtacct = '" + pldtNum + "';", False)
	result = []
	for a in res:
		stringed = map(str, a)
		result.append(stringed)


	return json.dumps(result)