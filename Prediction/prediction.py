"""
@author: Vivsvaan Sharma
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('sentiment_data_2019.csv')
'''
    assuming that all these hashtags are of BJP
'''

pos = 0
neg = 0
total = 0
compound_val = dataset.iloc[:, 5]
compound_val = list(compound_val)
total = len(compound_val)
'''
    neg < -0.5 = neu = 0.5 < pos
    but here we're taking 0.2
'''


for i in compound_val:
    j = float(i)
    if (j < -0.2):
        neg = neg + 1
    elif (j > 0.2):
        pos = pos + 1

print()
print('{:>15}'.format("candidate"), end="")
print('{:>15}'.format("Positive"), end="")
print('{:>15}'.format("Negative"), end="")
print('{:>15}'.format("Total"), end="")
print('{:>15}'.format("PvT ratio"))
print()

#for BJP
bjp_pvt = pos/total
print('{:>15}'.format("BJP"), end="")
print('{:>15}'.format(pos), end="")
print('{:>15}'.format(neg), end="")
print('{:>15}'.format(total), end="")
print('{:>15}'.format("%.2f" % bjp_pvt))

#for cong
cong_pvt = neg/total
print('{:>15}'.format("Congress"), end="")
print('{:>15}'.format(neg), end="")
print('{:>15}'.format(pos), end="")
print('{:>15}'.format(total), end="")
print('{:>15}'.format("%.2f" % cong_pvt))
print()

print('{:>15}'.format("Prediction is:"), end="")
if bjp_pvt < cong_pvt:
    print('{:>15}'.format("CONGRESS will Win"))
else:
    print('{:>15}'.format("BJP will Win"))


