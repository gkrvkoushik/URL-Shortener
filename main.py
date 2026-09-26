from urlshortener import URLShortener

exit=False
app=URLShortener()
while True:
    inp=int(input("Enter user's choice :1.Url-Shortener\n2.Redirect-to-Url\n3.Exit\n"))
    match inp:
        case 1:
            query=input("Enter url to be shortened :")
            short_url=app.shorten_url(query)
            print("URL :",query," ","\nShortened Version :",short_url,end='\n')
            

        case 2:
            query=input("Enter shortened url :")
            long_url=app.redirect(query)
            print("Shorten URL :",query," ","\nOriginal Version :",long_url,end='\n')
            

        case 3:
            exit=True  
            

    if exit:
        break