import indicoio
indicoio.config.api_key = '8d05933c4c2ca769d1e064dfbea1fe8a'
f_stats=open("stats.txt", "w")
#mini project open the url file which we saved from harvesting and execute political analysis*/
##########################################
folder=["url_nyt.txt", "url_cbs.txt", "url_wsj.txt", "url_fox.txt"]
for textfiles in folder:
	f= open(textfiles, 'r')

	line=f.readline()
	url_nyt=line.split(',')

	## get all urls from the saved file
	i=0
	for i in range(len(url_nyt)-1):
		url_nyt[i]=url_nyt[i][3:-1]
		print url_nyt[i]
		i=i+1

	## because last url has on more ' 
	url_nyt[-1]=url_nyt[-1][3:-2]
	print len(url_nyt)

	## do political analysis using indicoio
	analysis_nyt=[]
	j=0
	for j in range(len(url_nyt)):
		analysis_nyt.append(indicoio.political(url_nyt[j]))
		#print analysis_nyt[j]
		j=j+1

	#print analysis_nyt[0]["Liberal"]

	## get the average of the analysis
	sum_stats_nyt=[0,0,0,0]  #sum of all stats gained from indicoio
	for i in range(len(analysis_nyt)):
		sum_stats_nyt[0]=sum_stats_nyt[0]+analysis_nyt[i]["Libertarian"]
		sum_stats_nyt[1]=sum_stats_nyt[1]+analysis_nyt[i]["Green"]
		sum_stats_nyt[2]=sum_stats_nyt[2]+analysis_nyt[i]["Liberal"]
		sum_stats_nyt[3]=sum_stats_nyt[3]+analysis_nyt[i]["Conservative"]
		i=i+1
	print sum_stats_nyt	
	aver_stats_nyt=[0,0,0,0]
	for i in range(4):
	 	aver_stats_nyt[i]=sum_stats_nyt[i]/float(len(analysis_nyt))


	print "[Libertarian   ,   Green   ,   Liberal   ,  Conservative]"
	print aver_stats_nyt

#move the stats to the text local text file
	
	f_stats.write(textfiles+" polytical analysis stat \n [ Libertarian:    ,   Green   ,   Liberal   ,  Conservative] \n")
	print >>f_stats, aver_stats_nyt
	f_stats.write("\n" )
	f.close()

f_stats.close()
