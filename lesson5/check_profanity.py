import urllib

def read_text():
        #To Open Text form PC
    quotes = open("E:\Programming\UdacityCource\Python\Python 2.7_Tasks\lesson5\move_quotes.txt")
    contents_of_file = quotes.read()  #To Read The Text Whose Opened
    print(contents_of_file)         #to print contentes of text          
    quotes.close()          #to close the file whose opened

    check_profanity(contents_of_file)
    

    #To Check if exist words cuse or not
    #If Result =(true)there is cause words  #If Result =(false)there is not cause words  
def check_profanity(text_to_checked):
    #(urllib()) => function get information from internet
    #(urlopen()) =>function open url website  **  ** 
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text_to_checked)
    output = connection.read()
    if("true" in output):
        print("Profanity Alert !!")
    elif("false" in output):
        print("This Document has no cause words!")
    else:
        print("Could not scan this document propertl.")
    connection.close()


read_text()
