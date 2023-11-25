import webbrowser

links = []


links.append("https://github.com/")
links.append("https://neetcode.io/")
links.append("https://www.notion.so/")

firefox = webbrowser.get('Firefox')

for link in links:
    firefox.open(link)
