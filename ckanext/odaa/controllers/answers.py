import ckan.lib.base as base 
import psycopg2
import urllib
import urllib2
import json
from ckan.common import _, c, request
from datetime import datetime

class AnswersController(base.BaseController):

    def index(self):
        auth_key = 'e3800xxxxxxxxxxxxxxxxxxxxxxxxx7b437'
		i = datetime.now()
		date=i.strftime('%Y/%m/%d %H:%M:%S')
		kommerFra=request.params.get('kommerFra', 'Not present').encode('utf-8')
		spg1=request.params.get('spg1', 'Not present').encode('utf-8')
		spg2=request.params.get('spg2', 'Not present').encode('utf-8')
			spg3=",".join(request.params.getall('spg3')).encode('utf-8')
		spg4=request.params.get('spg4', 'Not present').encode('utf-8')
		spg5=request.params.get('spg5', 'Not present').encode('utf-8')
			spg5=",".join(request.params.getall('spg5')).encode('utf-8')
		str="spg3=" + spg3
		andet=request.params.get('andet', 'Not present').encode('utf-8')
		url = "http://www.odaa.dk/api/3/action/"

			# In python using urllib2 for datastore_create it is..
		
		datastore_structure = """{"resource_id": "e968e61e-eb77-4508-9d4c-d9d3ef8f0daf",
							  "fields":[{"id": "date"},{"id":"kommerFra"}, {"id": "spg1"}, {"id": "spg2"}, {"id": "spg3"}, {"id": "spg4"}, {"id": "spg5"},{"id":"andet"}],
							  "records":[{"date": "%s","kommerFra":"%s", "spg1": "%s", "spg2": "%s", "spg3": "%s", "spg4": "%s", "spg5": "%s","andet":"%s"}],
							  "force":"true"}"""  % (date,kommerFra, spg1, spg2, spg3, spg4, spg5,andet)
		ds = json.loads(datastore_structure)

			headers = {'content-type': 'application/json', 'Authorization': auth_key}	        
			req = urllib2.Request(url + 'datastore_create', data=json.dumps(ds), headers=headers)
			response = urllib2.urlopen(req)
		str="""<script>
					window.close();
					</script>
			"""
		return str

    def submit(self):
        return 'Your email is: %s' % request.params['name']
