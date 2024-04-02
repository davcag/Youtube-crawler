# collects youtube links and titles and writes them to txt file


import requests, bs4

query = "" #add the search query here
search = "https://www.youtube.com/results?search_query=" + query

res = requests.get(search)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

title = soup.select("h3 a")

f = open("videos.txt", "a", encoding = "utf-8")

for tit in title:
    f.write(tit.get("title") + "\n")
    f.write("https://www.youtube.com" + tit.get("href") + "\n")
    print(tit.get("title"))
    print(tit.get("href"))


f.close()
