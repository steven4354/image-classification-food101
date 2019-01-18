
# coding: utf-8

# In[1]:


# Put these at the top of every notebook, to get automatic reloading and inline plotting
get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('matplotlib', 'inline')


# Here we import the libraries we need.

# In[2]:


# This file contains all the main external libs we'll use
from fastai.imports import *


# In[3]:


from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *


# In[4]:


PATH = "fastai/food-101"


# I will use a few shell commands to see the data organization

# In[5]:


get_ipython().system('ls {PATH}')

