def NetDrop(url,filename):
	from requests import get
	import os
	pmlfile = get(url, verify=False)
	pmlout = os.path.join(os.getcwd(),filename)
	f = open(pmlout,'w')
	f.write(pmlfile.content)
	f.close()
	return()
