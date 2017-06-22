print ("Module is imported")
print ("Module version2")
print ('__name__: ',__name__)
def hello():
	print ("hellow world")

if __name__ == "__main__":
	print ("This is run by python direct")
else:
	print ("This module is imported")
