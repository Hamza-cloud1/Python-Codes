sentence='he -is @engineer and programmer/'
import re
clean_sentance=re.sub('[^A-Za-z0-9\s]+','',sentence)
print(clean_sentance)
