import urllib.request
#pip install urllib3

def check_connect(web='http://youtube'):
    try:
        urllib.request.urlopen(web) 
        return True
    except:
        return False
# Print the output 
print( "Internet is active" if check_connect() else "There is no internet" )


    




