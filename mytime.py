import datetime

def fgettime(d=0,h=0):
	temp=(datetime.datetime.now()+datetime.timedelta(days=d,hours=h)).strftime('%Y-%m-%d %H:%M:%S')
	print(temp)
	return temp

def fnow():
	temp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print(temp)
	return temp

def ftoday():
	temp=datetime.datetime.now().strftime('%Y-%m-%d')
	print(temp)
	return temp
