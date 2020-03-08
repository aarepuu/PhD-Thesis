#!/usr/bin/env python3

import sys
import os
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

register_matplotlib_converters()

# Annotation style
style = dict(size=5, color='black')

# ticks formaters
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
weeks =  mdates.WeekdayLocator() # every week
monthFmt = mdates.DateFormatter('%d-%m-%Y')

# read data
data = pd.read_csv(sys.stdin,sep=' ', header=0)
data['date'] = pd.to_datetime(data['date'])

# the plot
plt.figure()
plt.plot(data['date'], data['words'], color='r')
plt.xlabel('TIME')
plt.ylabel('THESIS WORD COUNT')
plt.title('THESIS WORD COUNT vs. TIME')
plt.axhline(y=80000,color='green',linestyle='--')

#plt.text(data['date'].head(1), data['words'].head(1), 'CREATED THESIS FILE', horizontalalignment='center', verticalalignment='center', size='small', color='black')


# format the ticks
ax = plt.gca()
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthFmt)
# Annotations
# https://jakevdp.github.io/PythonDataScienceHandbook/04.09-text-and-annotation.html
#ax.text('2019-02-04', 200, "Writing Retreat", ha='center', **style)

ax.annotate('Skiing', xy=('2019-01-23', 2000), xycoords='data', ha='center',
            xytext=(0, -10), textcoords='offset points',**style)         
ax.annotate('', xy=('2019-01-19', 1200), xytext=('2019-01-29', 1200),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', }) 

ax.annotate("Writing retreat", xy=('2019-02-04', 2000),  xycoords='data',
            xytext=(-20, 30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.2"), **style)            

ax.annotate('Holiday', xy=('2019-07-16', 28000), xycoords='data', ha='center',
            xytext=(0, -10), textcoords='offset points',**style)         
ax.annotate('', xy=('2019-07-10', 28000), xytext=('2019-07-25', 28000),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', }) 

ax.annotate("Took a job at UO", xy=('2019-09-01', 45000),  xycoords='data',
            xytext=(-20, 30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.2"), **style) 

ax.annotate("Funding stopped", xy=('2019-09-25', 47000),  xycoords='data',
            xytext=(20, -30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=-0.2"), **style)                             

ax.annotate("Focused writing", xy=('2019-11-18', 52000),  xycoords='data',
            xytext=(-20, 35), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.2"), **style)

ax.annotate('Panic?', xy=('2020-01-10', 62000), xycoords='data', ha='center',
            xytext=(0, -10), textcoords='offset points',**style)                                       
ax.annotate('', xy=('2019-12-16', 62000), xytext=('2020-02-01', 62000),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', })

ax.annotate('Christmas & Skiing', xy=('2020-01-10', 75000), xycoords='data', ha='center',
            xytext=(0, -10), textcoords='offset points',**style)         
ax.annotate('', xy=('2019-12-20', 75000), xytext=('2020-01-24', 75000),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', }) 

ax.annotate("Final Push", xy=('2020-02-25', 75000),  xycoords='data',
            xytext=(10, -30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=-0.2"), **style)                                         


plt.gcf().autofmt_xdate() # Rotation
plt.savefig('word_count.png')
os.system("git commit -m 'Progress...' -- word_count.png; git push")
