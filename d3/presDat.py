import json

presFile = file("presidents.txt", 'r')

pList = []

for t in presFile:
	df = t.split("\t")
	#print df[1],
	fromTo = [int(i) for i in df[2].split('-')]
	if(len(fromTo)==1):
		fromTo = [fromTo[0], fromTo[0]]
	born = int(df[4].split("/")[2])
	try:
		death = int(df[5].split("/")[2])
	except:
		death = 2013
 	#print fromTo, born, death
	startAge = fromTo[0]-born
	finAge =  fromTo[1]-born
	deathAge = death-born
	temp = dict({'name': df[1], 'start': startAge, 'end': finAge, 'death': deathAge})
	pList.append(temp)

print json.dumps(pList, indent=4, separators=(',', ':'))

print max([i['death'] for i in pList])
