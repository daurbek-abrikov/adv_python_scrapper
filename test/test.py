import sys
sys.path.append("src")             
import Web_Scrapper    

scrapper = Web_Scrapper()   #initiating an object of our class


scrapper.set_coin()   #to set which creptocurrency you need
scrapper.print_p()    #to print resulting paragraphs from website related to setted cryptocurrency
