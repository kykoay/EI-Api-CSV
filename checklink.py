import requests # If you have a dependency do download it from <<insert link>>
import pandas as pd 
import io
import urllib

offset = str(0)
sector='Industrial'
version='latest'
api_key='' #add api key here 
detail='full'
eia = str(963)
link = 'https://api.openei.org/utility_rates?version={0}&format=csv&eia={1}&offset={2}&detail={3}&sector={4}&api_key={5}'.format(version,eia,offset,detail,sector,api_key)
data = pd.read_csv(io.StringIO(requests.get(link).text))

filename = '{0}newtest.csv'.format(eia)
out = open(filename,"wb")
data.to_csv(filename,index=True)
out.close()

