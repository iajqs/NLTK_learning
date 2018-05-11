from nltk.corpus import gutenberg, nps_chat
import nltk
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print(moby.findall(r"<a><.*><man>"))
print(moby.findall(r"<a>(<.*>)<man>"))

chat = nltk.Text(nps_chat.words())
print(chat.findall(r"<l.*>{3,}"))