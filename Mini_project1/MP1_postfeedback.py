#code to mining the urls from google and save it to local .txt files
# using patter. to search from Google
# I integrated all files in one single file after the feedback
# Using functions and readable documents

from pattern.web import Google
import indicoio
indicoio.config.api_key = '8d05933c4c2ca769d1e064dfbea1fe8a'
#save the results of the analysis in the "stats.txt" file.


# declare arrays which save raw url mined from pattern.search
# new york times urls, cbs new urls, wallstreet journal urls, foxnew urls
rawurl_nytimes=[]
rawurl_cbsnews=[]
rawurl_wsj=[]
rawurl_foxnews=[]
journal_names=['nytimes', 'cbsnews', 'wsj', 'foxnews']
rawurls=[rawurl_nytimes, rawurl_cbsnews, rawurl_wsj, rawurl_foxnews]
result_page=4

ny_analysis=[]
cbs_analysis=[]
wsj_analysis=[]
foxnews_analysis=[]
analysis=[ny_analysis,cbs_analysis, wsj_analysis,foxnews_analysis]
folders=["url_nytimes.txt", "url_cbsnews.txt", "url_wsj.txt", "url_foxnews.txt"]
g=Google()


#get the New York Times url
def get_articles(journal_num):	
	for i in range(1,result_page):
		# search google results correspoding to the following keyword
		for result in g.search('Donald Trump opinion site:'+journal_names[journal_num]+'.com', start=i):
		    rawurls[journal_num].append(result.url)

	
	# saves the keyword to the local file in order to reduce query
	# we will use this file for analyzing later on
def saveinfile(journal_num):
	f=open('url_'+journal_names[journal_num]+'.txt', "w")
	print >>f, rawurls[journal_num]
	f.close()

def get_save_articles(journal_num):
	get_articles(journal_num)
	saveinfile(journal_num)

# then you can write a "master function" at the end which chains all of the steps
# in your process together
## get and save articles from all 4 medias



#mini project open the url file which we saved from harvesting and execute political analysis*/
##########################################

#for each files split the string by comma from the array
def analyze_text(journal_num):
	f= open(folders[journal_num], 'r')

	line=f.readline()
	url_dummy=line.split(',') # dummy-> lists or urls,get all urls from the saved file
	
	for i in range(len(url_dummy)-1):
		# get rid of useless html.
		url_dummy[i]=url_dummy[i][3:-1]	
	url_dummy[-1]=url_dummy[-1][3:-2] ## because last url has on more ' , get rid of it
	

	## do political analysis using indicoio using the API and apped it to the array
	
	for j in range(len(url_dummy)):
		analysis[journal_num].append(indicoio.political(url_dummy[j]))
	f.close()
	

	## get the average of the analysis
	## add all the results of the urls and divide with the number of urls
def political_analysis(journal_num):
	sum_stats=[0,0,0,0]  #sum of all stats gained from indicoio
	for i in range(len(analysis)):
		sum_stats[0]=sum_stats[0]+analysis[journal_num][i]["Libertarian"]
		sum_stats[1]=sum_stats[1]+analysis[journal_num][i]["Green"]
		sum_stats[2]=sum_stats[2]+analysis[journal_num][i]["Liberal"]
		sum_stats[3]=sum_stats[3]+analysis[journal_num][i]["Conservative"]
		
	aver_stats=[0,0,0,0]
	for i in range(4):
	 	aver_stats[i]=sum_stats[i]/float(len(analysis)) # divide by length to get average


	print journal_names[journal_num]+"  [Libertarian   ,   Green   ,   Liberal   ,  Conservative]"
	print aver_stats


# get_save_articles(0)
# get_save_articles(1)
# get_save_articles(2)
# get_save_articles(3)

for i in range(4):
	get_save_articles(i)
	analyze_text(i)
	political_analysis(i)

		

