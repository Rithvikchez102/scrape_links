# from next_button import next_button 

 
def scrape(page):
    with open("get_links.js") as f:
        print("get_links.js")
        get_links_script = f.read()

    # page.evaluate(get_links_script)
    url = input("enter URL : ")
    page.goto(url)
    
    no_of_next = 0
    links_length = 0
    links = []
    pattern_include = input("enter pattern to include : ")
    pattern_exclude = input("enter pattern to exclude : ")
    while True:
        try:
            page.wait_for_timeout(1000)
            page.evaluate(get_links_script)
            temp_links = page.evaluate(
                """([arg1, arg2]) => {
                    return get_links(arg1, arg2);
                }""",
                [pattern_include, pattern_exclude]
            )
            temp_links = list(set(temp_links))
            links.extend(temp_links)
            
            print (len(links) , links_length, no_of_next)
            if len(links) == links_length:
                break

            links_length = len(links)
            print("move")
            from next_button import next_button

            next_button(page)
            # page.get_by_text("Next").click()
            # page.get_by_text("Next", exact=True).click()
            no_of_next +=1
            page.wait_for_timeout(2000)
        except Exception as e:
            print(e)
            break
    
    
    links = list(set(links))

    for link in links[:]:
        if "share" in link or "mailto:?&subject" in link or "sharer" in link or "shareArticle" in link  :
            print("removing share link")
            links.remove(link)
        
        
    return links