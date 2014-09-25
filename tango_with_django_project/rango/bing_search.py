import json
import urllib, urllib2
from keys import BING_API_KEY

def run_query(search_terms):
    # specifying the base
    root_url = 'https://api.datamarket.azure.com/bing/search/v1/'
    source = 'Web'
    
    # specify the amoutn of results you wish to be returned per page.
    # offset specifies where in the result list to start from
    # e.g.: results_per_page = 10, offset = 11 --> starting from page 2
    results_per_page = 10
    offset = 0
    
    # wrap queries terms in double quotes as require by the Bing API
    # the query you'll use is stored in the query variable
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)
    
    # construct the latter part of the request's URL
    # sets the format of the response to JSON and sets other properties.
    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)
        
    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''
    # Add your BING_API_KEY to a file called keys, which will not be commited to the repo
    bing_api_key = BING_API_KEY
    
    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, bing_api_key)
    
    # Create our results list which we'll populate.
    results = []
    
    try:
        # Prepare for connecting to Bing's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        
        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()
        
        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)
        
        # Loop through each page returned, populating out results list.
        for result in json_response['d']['results']:
            results.append({
                'title': result['Title'],
                'link': result['Url'],
                'summary': result['Description']})
                
    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError, e:
        print "Error when querying the Bing API: ", e
        
    # Return the list of results to the calling function.
    return results
    
    def main():
        # Query, get the results and create a variable to store rank.
        query = raw_input("Please enter a query: ")
        results = run_query(query)
        rank = 1
        
        # Loop through our results.
        for result in results:
            # Print details.
            print "Rank {0}".format(rank)
            print result['title']
            print result['link']
            print
        
        # Increment our rank counter by 1.
        rank += 1
        
    if __name__ == '__main__':
        main()
 
