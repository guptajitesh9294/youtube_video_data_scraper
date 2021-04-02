from requests.sessions import session
from bs4 import BeautifulSoup as bs 
from requests_html import HTMLSession


class getAllVideoTags:
    def __init__(self):
        pass

    @staticmethod
    def getVideoTags(url):
        session = HTMLSession()
        response = session.get(url)
        response.html.render(sleep=2)
        soup = bs(response.html.html, "html.parser")

        # open("video.html", "w", encoding="utf8").write(output.html.html)  
        output = {}

        # Retriving Video title
        output["title"] = soup.find('h1').text.strip()
        # print(output)
        
        # Number of views
        output["views"] = int(''.join([x for x in soup.find("span", attrs={"class": "view-count"}).text if x.isdigit()]))
        
        # Publising date
        output["date_published"] = soup.find("div", {"id": "date"}).text[1:]

        # video description
        output["description"] = soup.find("yt-formatted-string", {"class": "content"}).text

        # Duration
        output["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text

        # Video Tags For video classfication
        output["tags"] = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])

        # Likes
        text_yt_formatted_strings = soup.find_all("yt-formatted-string", {"id": "text", "class": "ytd-toggle-button-renderer"})
        # print(text_yt_formatted_strings)
        output["likes"] = text_yt_formatted_strings[0].text

        # DisLikes
        output["dislikes"] = text_yt_formatted_strings[1].text

        # Channel_Info
        channel_tag = soup.find("yt-formatted-string", {"class": "ytd-channel-name"}).find("a")

        # channel name
        channel_name = channel_tag.text
        
        # channel URL
        channel_url = f"https://www.youtube.com{channel_tag['href']}"
        
        # number of subscribers as str
        channel_subscribers = soup.find("yt-formatted-string", {"id": "owner-sub-count"}).text.strip()
        output["channel_name"] = channel_name
        output["channel_url"] = channel_url
        output["subscribers"] = channel_subscribers
        # output['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

        # # Number of commnets
        # output["comments"] = int(''.join([x for x in soup.find("yt-fomatted-string", attrs={"class": "count-text"}).text if x.isdigit()]))

        # output["comments"] = 

        return output