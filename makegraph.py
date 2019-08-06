#!/usr/bin/env python3

import sys
import os
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv(sys.stdin,sep=' ', header=0)

plt.plot(data['date'], data['words'], color='r', label='PhD Progress')
plt.xlabel('Date')
plt.ylabel('Word Count')
plt.title('Phd Progress')
plt.savefig('word_count.png')