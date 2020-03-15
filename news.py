# importing requests package 
import requests	 

def NewsFromBBC(): 
	
    # BBC news api 
    main_url = " http://newsapi.org/v2/top-headlines?country=in&apiKey=5fafae06e4544462bd4802b75572a053"

    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 

    # getting all articles in a string article 
    article = open_bbc_page["articles"]["author"] 
    

	# empty list which will 
	# contain all trending news 
    results = [] 

	
    for ar in article: 
        results.append(ar["title"]) 
		
    for i in range(len(results)): 
		
        # printing all trending news 
        print(i + 1, results[i])				 

# Driver Code 
if __name__ == '__main__': 
	
	# function call 
	NewsFromBBC() 
