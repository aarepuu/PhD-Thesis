#!/usr/bin/env python3

import datetime
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

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
plt.plot(data['date'], data['words'], color='r', label='PhD Progress')
plt.xlabel('Date')
plt.ylabel('Word Count')
plt.title('Phd Progress')

# format the ticks
ax = plt.gca()
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthFmt)
plt.gcf().autofmt_xdate() # Rotation
plt.savefig('word_count.png')
