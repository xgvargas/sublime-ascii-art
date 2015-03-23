import sublime, sublime_plugin
import urllib, urllib2
import re
import HTMLParser


def getArt(text):
    url = 'http://www.network-science.de/ascii/ascii.php'
    data = urllib.urlencode({
                            'TEXT': text.strip(' \t\n\r'),
                            'x': 38,
                            'y': 7,
                            'FONT': 'big',
                            'RICH': 'no',
                            'FORM': 'left',
                            'STRE': 'no',
                            'WIDT': 80
                            })
    try:
        request = urllib2.Request(url+'?'+data, headers={})
        http_file = urllib2.urlopen(request, timeout=10)
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
                    # self.view.sel().clear()
                else:
                    self.view.set_status('ascii', 'Ascii-Art generator failed!')
            else: #texto selecionado...
                pass

