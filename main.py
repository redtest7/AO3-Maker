from gtts import gTTS
import AO3
import re

Filename = input('Video name?' )
Filename = Filename + '.mp3'
url = input('type URL for AO3 ')
cnum = input('Chapter starting from 0? ')
workid = AO3.utils.workid_from_url(url)
print(f"Work ID: {workid}")
work = AO3.Work(workid)
print(f"Chapters: {work.nchapters}")

print(work.chapters[int(cnum)].title)
text = work.chapters[int(cnum)].text

Author = str(work.authors)
Author_clean = re.search('<User (.*)>', Author)
Author_clean = str(Author_clean.group(1))

opener = work.title + ' by ' + Author_clean
tts_open = gTTS(opener, lang='en', tld='ca')
tts_chap = gTTS(text, lang='en', tld='ca')
with open(Filename, 'wb') as f:
    tts_open.write_to_fp(f)
    tts_chap.write_to_fp(f)