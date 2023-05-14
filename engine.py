import webbrowser

from config import *
def open_help_link():
    browser_pos = 0
    def open_browser(pos = browser_pos):
        try:
            webbrowser.get(BROWSERS[pos]).open(HELP_LINK)
        except:
            if pos <= len(BROWSERS) - 1:
                pos += 1
                open_browser(pos)
            else:
                return None
    
    open_browser(browser_pos)