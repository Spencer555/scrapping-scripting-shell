from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq 



my_url ="https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off"



uClient = uReq(my_url) #opens up the connection 

page_html = uClient.read() #dump all the data collected in the variable
uClient.close()

page_soup = soup(page_html, "html.parser") #we have u parse the html file since it large

#note the classes and ids and tags are gotten when u inspect the page

#first search for the main class which all elements are presents

containers = page_soup.findAll("div", {"class":"col_2-gKeQ"}) #main class which contains elem

print(len(containers))# tells how many products u have on the web page


print(soup.prettify(containers[0]))
#using prettify to beautify html and getting the html first html 
#  view this data in the terminal to scrape

container = containers[0]

#printing the product title based on the class we got 
#print(container.div.img["alt"])

price=container.findAll("div", {"class":"col col-5-12 _2o7WAb"})
#print(price[0]).text getting the price based on class

ratings = container.findAll("div", {"class": "niHOFQ"})
#print(ratings[0]).text

filename="product.csv"

f = open(filename, "w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)

#we are looping through to print 
for container in containers:
    product_name = container.div.img['alt']
    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()#strip eleminate all unnessecary commas and space etc
    
    
    rating_container = container.findAll("div", {"class" : "niHOFQ"})
    
    rating = rating_container[0].text
    
    
    #string parsing to remove unnecessary things 
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.spit("$")#any currency u want
    add_rs_price = "Rs." + rm_rupee[1]
    split_price =  add_rs_price.split('E')
    final_price = split_price[0]
    
    
    split_rating = rating.split(" ")
    final_rating = split_rating[0]
    
    #be sure it has no extra commas cause anytime it finds a comma it create an extra column
    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    
f.close()