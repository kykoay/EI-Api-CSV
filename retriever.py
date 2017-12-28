from OpenEI import *
import pandas as pd

eia = [
	'15477',
	'14940',
	'14715',
	'1167',
	'9726',
	'12390',
	'14711',
	'15270',
	'963',
	'5027',
	'16213',
	'332',
	'4110',
	'4062',
	'4922',
	'5487',
	'3542',
	'56162',
	'5580',
	'19876'
	]



for id in eia:
	data = OpenEIData(id,0)
	data.get_csv()
	print "Just finished dowloading id :" + str(id)

