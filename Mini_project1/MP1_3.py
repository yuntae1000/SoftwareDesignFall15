import indicoio
indicoio.config.api_key = '8d05933c4c2ca769d1e064dfbea1fe8a'
f_stats=open("stats_positive3.txt", "w")
#mini project open the url file which we saved from harvesting and execute political analysis*/
##########################################
folder=["url_nyt3.txt", "url_cbs3.txt", "url_wsj3.txt", "url_fox3.txt"]
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

	## do sentiment analysis using indicoio
	analysis_nyt=[]
	j=0
	for j in range(len(url_nyt)):
		analysis_nyt.append(indicoio.sentiment(url_nyt[j]))
		#print analysis_nyt[j]
		j=j+1

	#print analysis_nyt[0]["Liberal"]

	## get the average of the analysis
	sum_stats_nyt=[0]  #sum of all stats gained from indicoio
	for i in range(len(analysis_nyt)):
		sum_stats_nyt[0]=sum_stats_nyt[0]+analysis_nyt[i]
		
	print sum_stats_nyt	

	aver_stats_nyt=[0]
	aver_stats_nyt[0]=sum_stats_nyt[0]/float(len(analysis_nyt))


	
	print aver_stats_nyt

#move the stats to the text local text file
	
	f_stats.write(textfiles+" sentiment analysis stat \n [ positivity] \n")
	print >>f_stats, aver_stats_nyt
	f_stats.write("\n" )
	f.close()

f_stats.close()
