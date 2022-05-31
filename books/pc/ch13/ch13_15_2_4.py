import webbrowser

url = "http://www.baidu.com/"

c = webbrowser.get("google-chrome")
c.open(url)
c.open_new_tab(url)
