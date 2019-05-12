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
[25373,161,27.88,30110,84.26,28,142,94,2431,372,142,27410,694,39.49,5.72,41.3,16,4],
[26500,264,41.21,29169,90.84,64,129,56,2485,522,174,25063,812,30.86,5.18,35.7,27,7],
[25572,180,35.46,26833,95.3,51,136,68,2376,523,143,25704,705,36.45,5.62,38.8,29,9],
[24993,185,37.98,26987,92.61,56,117,47,2353,446,181,23290,788,29.55,5.22,33.9,27,5],
[24175,179,33.95,26579,90.95,42,133,67,2197,451,165,24537,743,33.02,5.43,36.4,20,10],
[23742,237,34.76,26012,91.27,38,124,67,2192,494,165,23438,719,32.59,5.43,35.9,15,11],
[21264,210,32.71,24938,85.26,33,120,67,1846,348,116,21443,570,37.61,5.29,42.6,18,9],
[15080,215,26.69,17900,84.24,22,60,58,1194,497,81,17610,407,43.26,5.8,44.7,9,5],
[14415,144,29.9,17600,81.9,23,80,53,1411,224,105,15052,455,33.08,5.09,38.9,16,5],
[12451,138,22.31,16881,73.75,12,54,58,1145,191,94,15439,323,47.79,5.44,52.6,4,1],
[4257,112,20.17,5671,75.06,3,18,27,408,66,29,6032,124,48.64,5.88,49.6,4,0]
]
mtx

# let's says the first two alternatives are
# for maximization and the last one for minimization
criteria = [MAX, MAX,MAX,MAX,MAX,MAX,MAX,MIN,MAX,MAX,MAX,MIN,MAX,MIN,MIN,MIN,MAX,MAX]
criteria

# we use the built-in function as aliases
data = Data(mtx, [max, max,max,max,max,max,max,min,max,max,max,min,max,min,min,min,max,max])



data = Data(mtx, criteria,
anames=["SriLanka", "India","England","South Africa","Australia","NewZealand","Pakistan","West Indies","Bangladesh","Zimbabwe","Ireland"],
cnames=["Run", "HS","Average","BF","Strikerate","Centuries","Fifties","zeros","Fours","Sixes","Maiden","Runs_bowl","Wickets","Average_bowling","Economical","Strikerate_bowl","4wickets","5wickets"])


data = Data(mtx, criteria,
#weights=[0.04, .3, .4,0.01,0.02,0.025,0.044,0.0234,0.1330,0.0046],
weights=[0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556,0.0555555555555556],
anames=["SriLanka", "India","England","South Africa","Australia","NewZealand","Pakistan","West Indies","Bangladesh","Zimbabwe","Ireland"],
cnames=["Run", "HS","Average","BF","Strikerate","Centuries","Fifties","zeros","Fours","Sixes","Maiden","Runs_bowl","Wickets","Average_bowling","Economical","Strikerate_bowl","4wickets","5wickets"])




#data.plot();
data.plot("box");



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

dm = closeness.TOPSIS(mnorm="sum")
dm
print(dm)
print(dm.decide(data))

#The TOPSIS add more information into the decision object.
print(dec.e_)
print("Ideal:", dec.e_.ideal)
print("Anti-Ideal:", dec.e_.anti_ideal)
print("Closeness:", dec.e_.closeness)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.set_title("Sum Norm")
data.plot.violin(mnorm="sum", ax=ax1);
ax2.set_title("Vector Norm")
data.plot.violin(mnorm="vector", ax=ax2);
f.set_figwidth(50)
