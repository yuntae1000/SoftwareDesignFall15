<<<<<<< HEAD
=======
import indicoio
indicoio.config.api_key = '8d05933c4c2ca769d1e064dfbea1fe8a'
f_stats=open("stats_positive3.txt", "w")
#mini project open the url file which we saved from harvesting and execute political analysis*/
##########################################
# I had to fix these txt file names to get your code to run
folder=["url_nytimes.txt", "url_cbsnews.txt", "url_wsj.txt", "url_foxnews.txt"]
for textfiles in folder:
	# again, "textfile" might be a better name than "textfiles"
	f= open(textfiles, 'r')

	line=f.readline()
	# url_nyt isn't a good variable name -- you're looping through the news sources,
	# so sometimes this will be a CBS url, sometimes it will be a WSJ url, etc.
	# It's actually misleading to name it url_nyt
	url_nyt=line.split(',')

	## get all urls from the saved file
	i=0
	for i in range(len(url_nyt)-1):
		url_nyt[i]=url_nyt[i][3:-1]
		print url_nyt[i]
		i=i+1 # again, you shouldn't do this

	## because last url has on more '
	url_nyt[-1]=url_nyt[-1][3:-2]
	print len(url_nyt)

	## do sentiment analysis using indicoio
	analysis_nyt=[]
	j=0
	for j in range(len(url_nyt)):
		analysis_nyt.append(indicoio.sentiment(url_nyt[j]))
		#print analysis_nyt[j] # make sure to remove commented-out code when you submit!
		j=j+1 # again, you shouldn't do this

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
>>>>>>> dc64805d6902a0e398c88ab87c38806ad0883c7a
