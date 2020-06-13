#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

r = norm.rvs(loc=0, scale=1, size=1000)

x = np.linspace(norm.ppf(0.01), #ppf stands for percentiles.
                norm.ppf(0.99), 100)

fig, ax = plt.subplots(1, 1)
ax.plot(x, norm.pdf(x),
        'blue', lw=5, alpha=0.6, label='norm pdf')
plt.show()


# In[2]:


fig, ax = plt.subplots(1, 1)
ax.hist(r, normed=True, histtype='stepfilled', alpha=1, label='...')
ax.legend(loc='best', frameon=False)
plt.show()


# In[3]:


from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# create a line chart, years on x-axis, gdp on y-axis
fig = plt.figure()
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# add a title
plt.title("Nominal GDP")
# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()


# In[4]:


from scipy import special
def drumhead_height(n, k, distance, angle, t):
   kth_zero = special.jn_zeros(n, k)[-1]
   return np.cos(t) * np.cos(n*angle) * special.jn(n, distance*kth_zero)
theta = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r * np.cos(theta) for r in radius])
y = np.array([r * np.sin(theta) for r in radius])
z = np.array([drumhead_height(1, 1, r, theta, 0.5) for r in radius])


# In[5]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


# In[6]:


import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt


# In[7]:


import seaborn as sns
sns.set(color_codes=True)
np.random.seed(sum(map(ord, "distributions")))


# In[8]:


x = np.random.normal(size=100)
sns.distplot(x);


# In[9]:


sns.distplot(x, kde=False, rug=True);


# In[10]:





# In[11]:


mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])


# In[12]:


sns.jointplot(x="x", y="y", data=df, kind="kde");


# In[13]:


f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df.x, df.y, ax=ax)
sns.rugplot(df.x, color="g", ax=ax)
sns.rugplot(df.y, vertical=True, ax=ax);


# In[14]:


g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$X$", "$Y$");


# In[16]:





# In[17]:





# In[ ]:




