#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys,os,argparse
from IPython.display import HTML
CONFIG_FILE = '.config_ipynb'
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE) as f:
        sys.argv = f.read().split()
else:
    sys.argv = ['test_args.py', 'input_file', '--int_param', '12']

parser = argparse.ArgumentParser()
parser.add_argument("input_file",help="Input image, directory, or npy.")
parser.add_argument("--int_param", type=int, default=4, help="an optional integer parameter.")
args = parser.parse_args()
p = args.int_param
print(args.input_file,p)


# In[1]:


from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('text to render'))


# In[ ]:




