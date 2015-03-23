# -*- coding: utf-8 -*-

"""
Author: Gustavo Vargas <xgvargas@gmail.com>
Repositorie and issues: https://github.com/xgvargas/sublime-ascii-art

Font BIG
           _____  _____ _____ _____             _____ _______
    /\    / ____|/ ____|_   _|_   _|      /\   |  __ \__   __|
   /  \  | (___ | |      | |   | |______ /  \  | |__) | | |
  / /\ \  \___ \| |      | |   | |______/ /\ \ |  _  /  | |
 / ____ \ ____) | |____ _| |_ _| |_    / ____ \| | \ \  | |
/_/    \_\_____/ \_____|_____|_____|  /_/    \_\_|  \_\ |_|


Font DOOM
  ___   _____ _____ _____ _____       ___  ______ _____
 / _ \ /  ___/  __ \_   _|_   _|     / _ \ | ___ \_   _|
/ /_\ \\ `--.| /  \/ | |   | |______/ /_\ \| |_/ / | |
|  _  | `--. \ |     | |   | |______|  _  ||    /  | |
| | | |/\__/ / \__/\_| |_ _| |_     | | | || |\ \  | |
\_| |_/\____/ \____/\___/ \___/     \_| |_/\_| \_| \_/


Font SMALL
   _   ___  ___ ___ ___     _   ___ _____
  /_\ / __|/ __|_ _|_ _|   /_\ | _ \_   _|
 / _ \\__ \ (__ | | | |   / _ \|   / | |
/_/ \_\___/\___|___|___|_/_/ \_\_|_\ |_|
                      |___|

"""

import sublime, sublime_plugin
import urllib, urllib2
import re
import HTMLParser


def getArt(text):
    url = 'http://www.network-science.de/ascii/ascii.php'
    data = urllib.urlencode({
                            'TEXT': text.strip(' \t\n\r'),
                            'FONT': 'big',  #also good: doom and small
                            'RICH': 'no',
                            'FORM': 'left',
                            'STRE': 'no',
                            'WIDT': 80
                            })
    try:
        request = urllib2.Request(url+'?'+data, headers={})
        http_file = urllib2.urlopen(request, timeout=15)
        full = http_file.read()
        m = re.search(r'(?is)<tr><td><pre>(.+?)</pre>', full)
        if m:
            return HTMLParser.HTMLParser().unescape(m.group(1))
    except:
        pass

    return False

class AsciiArtCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty(): #sem texto selecionado...
                line = self.view.line(region)
                line_content = self.view.substr(line)
                art = getArt(line_content)
                if art:
                    self.view.replace(edit, line, art)
                    self.view.sel().add(sublime.Region(line.begin(), line.begin()+len(art)))
                    self.view.run_command('toggle_comment')
                    self.view.sel().clear()
                    self.view.erase_status('ascii')
                else:
                    self.view.set_status('ascii', 'Ascii-Art generator failed!')
            else: #texto selecionado...
                pass

