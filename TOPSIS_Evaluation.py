# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:09:24 2019

@author: achuo
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:50:53 2019

@author: Shyamala J
"""

from skcriteria import Data, MIN, MAX
from skcriteria.madm import closeness, simple
import matplotlib.pyplot as plt
import datetime as dt
import skcriteria
print("Scikit-Criteria version:", skcriteria.VERSION)
print("Running datetime:", dt.datetime.now())

print(skcriteria.Data)
# 2 alternatives by 3 criteria
mtx = [
[27672,174,29.78,34251,80.79,36,156,107,2604,311,242,28130,853,32.97,5.05,39.1,17,12],
[28318,264,34.7,32777,86.39,50,153,89,2695,440,274,29502,889,33.18,5.19,38.2,25,5],
[22140,140,27.53,28529,77.6,21,128,80,1928,340,221,22762,711,32.01,4.78,40.1,18,8],
[21842,158,30.67,26177,83.43,26,113,65,1891,282,186,22936,675,33.97,5.19,39.2,21,6],
[22510,185,32.29,26691,84.33,27,128,47,1952,379,184,21246,681,31.19,4.99,37.4,25,11],
[20233,150,33.66,23568,85.84,41,101,48,1744,249,188,18419,669,27.53,4.87,33.8,25,6],
[17696,169,26.53,22673,78.04,22,84,85,1505,499,163,18880,565,33.41,4.99,40.1,24,5],
[15246,189,27.92,18439,82.68,21,76,55,1341,324,141,16263,502,32.39,5.1,38,21,3],
[13538,120,25.49,18126,74.68,10,80,56,1261,161,158,14963,469,31.9,4.96,38.5,18,5],
[11613,145,23.5,16290,71.28,6,65,59,1001,167,106,14453,313,46.17,5.3,52.2,6,4],
[4268,116,22.46,5909,72.22,6,14,21,404,57,49,4739,143,33.13,4.75,41.8,2,0],
[1103,98,15.98,1871,58.95,0,5,14,95,16,12,1734,39,44.46,5.52,48.3,0,0]
]
mtx

# let's says the first two alternatives are
# for maximization and the last one for minimization
criteria = [MAX, MAX,MAX,MAX,MAX,MAX,MAX,MIN,MAX,MAX,MAX,MIN,MAX,MIN,MIN,MIN,MAX,MAX]
criteria

# we use the built-in function as aliases
data = Data(mtx, [max, max,max,max,max,max,max,min,max,max,max,min,max,min,min,min,max,max])



data = Data(mtx, criteria,
anames=["SriLanka", "India","Pakistan","England","Australia","South Africa","West Indies","Newzealand","Bangladesh","Zimbabwe","Ireland","Kenya"],
cnames=["Run", "HS","Average","BF","Strikerate","Centuries","Fifties","zeros","Fours","Sixes","Maiden","Runs_bowl","Wickets","Average_bowling","Economical","Strikerate_bowl","4wickets","5wickets"])


data = Data(mtx, criteria,
#weights=[0.04, .3, .4,0.01,0.02,0.025,0.044,0.0234,0.1330,0.0046],
weights=[0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556],
anames=["SriLanka", "India","Pakistan","England","Australia","South Africa","West Indies","Newzealand","Bangladesh","Zimbabwe","Ireland","Kenya"],
cnames=["Run", "HS","Average","BF","Strikerate","Centuries","Fifties","zeros","Fours","Sixes","Maiden","Runs_bowl","Wickets","Average_bowling","Economical","Strikerate_bowl","4wickets","5wickets"])




#data.plot();
#data.plot("box");
#data.plot.violin();
#data.plot.radar(cmap="inferno", show_criteria=False);

# first create the decision maker
# (with the default hiper parameters)
dm = simple.WeightedSum()   
print(dm)
 # Now lets decide the ranking
dec = dm.decide(data)
print(dec)


print(dec.e_)
print(dec.e_.points)


print("Generate a ranking of alternatives?", dec.alpha_solution_)
print("Generate a kernel of best alternatives?", dec.beta_solution_)
print("Choose the best alternative?", dec.gamma_solution_)

#The rank as numpy array (if this decision is a 𝛼-solution)

print(dec.rank_)


#The index of the row of the best alternative (if this decision is a 𝛾-solution)
print(dec.best_alternative_, data.anames[dec.best_alternative_])

#And the kernel of the non supered alternatives (if this decision is a 𝛽-solution)
# this return None because this
# decision is not a beta-solution
print(dec.kernel_)

dm = simple.WeightedProduct()
print(dm)

dec = dm.decide(data)
print(dec)

#TOPSIS
dm = closeness.TOPSIS()
print(dm)

dec = dm.decide(data)
print(dec)


#The TOPSIS add more information into the decision object.
print(dec.e_)
print("Ideal:", dec.e_.ideal)
print("Anti-Ideal:", dec.e_.anti_ideal)
print("Closeness:", dec.e_.closeness)

#Finally we can change the normalization criteria of the alternative matric to sum (divide every value by the sum opf
#their criteria) and check the result:
#dm = closeness.TOPSIS(mnorm="sum")
dm = closeness.TOPSIS()
print(dm)


print(dm.decide(data))


f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.set_title("Sum Norm")
data.plot.violin(mnorm="sum", ax=ax1);
ax2.set_title("Vector Norm")
data.plot.violin(mnorm="vector", ax=ax2);
f.set_figwidth(15)
