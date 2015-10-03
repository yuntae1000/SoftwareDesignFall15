# cord to politically analyze contents of each urls
# using indicoio API to analyze political bias

import indicoio
indicoio.config.api_key = '8d05933c4c2ca769d1e064dfbea1fe8a'
#save the results of the analysis in the "stats.txt" file.
f_stats=open("stats.txt", "w")

#mini project open the url file which we saved from harvesting and execute political analysis*/
##########################################
folder=["url_nytimes.txt", "url_cbsnews.txt", "url_wsj.txt", "url_foxnews.txt"]

#for each files split the string by comma from the array
for textfiles in folder:
	# textfile might be a better name than textfiles -- if you're looping through all of
	# the textfiles in the folder, you're only getting one textfile at a time
	f= open(textfiles, 'r')

	line=f.readline()
	url_dummy=line.split(',') # why? what is url_dummy? Could use a comment here

	## get all urls from the saved file
	i=0
	for i in range(len(url_dummy)-1):
		# get rid of useless html.
		url_dummy[i]=url_dummy[i][3:-1]
		print url_dummy[i]
		i=i+1

	## because last url has on more ' , get rid of it
	url_dummy[-1]=url_dummy[-1][3:-2]
	print len(url_dummy)

	## do political analysis using indicoio using the API and apped it to the array
	analysis=[]
	j=0
	# You could also use "for item in url_dummy" syntax here, like you did
	# with "for textfiles in folder"
	for j in range(len(url_dummy)):
		analysis.append(indicoio.political(url_dummy[j]))
		j=j+1 # you shouldn't do this -- the for loop already increments j


	## get the average of the analysis
	## add all the results of the urls and divide with the number of urls

	sum_stats=[0,0,0,0]  #sum of all stats gained from indicoio
	for i in range(len(analysis)):
		sum_stats[0]=sum_stats[0]+analysis[i]["Libertarian"]
		sum_stats[1]=sum_stats[1]+analysis[i]["Green"]
		sum_stats[2]=sum_stats[2]+analysis[i]["Liberal"]
		sum_stats[3]=sum_stats[3]+analysis[i]["Conservative"]
		i=i+1 # again, you shouldn't do this
	print sum_stats
	aver_stats=[0,0,0,0]
	for i in range(4):
	 	aver_stats[i]=sum_stats[i]/float(len(analysis)) # too much for one line -- break the calculation up and explain it


	print "[Libertarian   ,   Green   ,   Liberal   ,  Conservative]"
	print aver_stats

	## move the stats to the text local text file
	## write the political analysis results to stats file line by line
	f_stats.write(textfiles+" polytical analysis stat \n [ Libertarian:    ,   Green   ,   Liberal   ,  Conservative] \n")
	print >>f_stats, aver_stats
	f_stats.write("\n" )
	f.close()

f_stats.close()

# Again, this all belongs in a function
