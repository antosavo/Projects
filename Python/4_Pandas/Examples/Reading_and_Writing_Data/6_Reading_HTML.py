import numpy as np
import pandas as pd

web_frames = pd.read_html('myFrame.html')
print "html frame:\n", web_frames[0]

#from website
ranking = pd.read_html('http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')
print "web frame:\n", ranking[0]
