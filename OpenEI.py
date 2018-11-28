import requests # If you have a dependency do download it from <<insert link>>
import pandas as pd 
import io
import urllib

"""
We will cteate an object call OpenEIData that will take as input a subset of the parameters
available from the OpenEI API. 
 The response requested will be in the form of a csv, as this is the format of choice for most researchers.
 The parameters are:
 1. version
 2. api_key
 3. eia (the EIA ID)
 4. offset (to limit when to start retrieving record)
 5. detail (by default it set to the value full to get rates data) 
 6. sector (by default it has the value "Industrial" )

The object will also have a method called get_csv, which when called will download the csv into the local directory.

If you run into SSL issues while using requests, consider doing
pip install pyOpenSSL ndg-httpsclient pyasn1
"""

class OpenEIData(object):
	def __init__(self,eia,offset,sector='Industrial',version='latest',api_key='',detail='full'): #edit and add your api key here
		self.version = version # by default we use the latest version but this can be overriden
		self.api_key = api_key
		self.eia = str(eia) 
		self.offset = str(offset)
		self.detail = detail
		self.sector = sector
		self.url = 'https://api.openei.org/utility_rates?version={0}&format=csv&eia={1}&offset={2}&detail={3}&sector={4}&api_key={5}'.format(self.version,self.eia,self.offset,self.detail,self.sector,self.api_key)
		self.data =  requests.get(self.url)
		self.buf = io.StringIO(self.data.text)
		self.df_csv = pd.read_csv(self.buf,index_col = 0 )
		#print self.url

	def get_csv(self):
		self.filename = '{0}.csv'.format(self.eia)
		self.out = open(self.filename,"wb")
		self.df_csv.to_csv(self.filename,index=True)
		self.out.close()
