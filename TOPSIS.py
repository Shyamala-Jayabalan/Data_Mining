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
[18,30,15,179,4,6,116,62,38,11],
[31,69,40,346,14,3,113,39,61,20],
[4,12,7,129,5,4,50,65,35,2],
[12,39,29,201,7,5,97,48,52,12],
[26,48,36,296,9,0,60,58,42,15],
[25,58,32,298,12,3,122,53,57,17],
[21,41,35,196,9,6,79,38,62,16],
[10,25,18,198,5,8,185,55,45,9],
[9,27,7,206,7,5,243,58,42,5]
]
mtx

# let's says the first two alternatives are
# for maximization and the last one for minimization
criteria = [MAX, MAX, MAX,MIN,MIN,MIN,MAX,MIN,MIN,MAX]
criteria

# we use the built-in function as aliases
data = Data(mtx, [max,max,max,min,min,min,max,min,min,max])



data = Data(mtx, criteria,
anames=["Pakistan", "India","Afghanistan","New zealand","England","South Africa","Australia","West Indies","Bangladesh"],
cnames=["Centuries", "Fifties", "Chased","Total Wickets","Series Won","Series Loss","Catches Drop","Played on side","Played offside","Allout"])


data = Data(mtx, criteria,
weights=[0.04, .3, .4,0.01,0.02,0.025,0.044,0.0234,0.1330,0.0046],
anames=["Pakistan", "India","Afghanistan","New zealand","England","South Africa","Australia","West Indies","Bangladesh"],
cnames=["Centuries", "Fifties", "Chased","Total Wickets","Series Won","Series Loss","Catches Drop","Played on side","Played offside","Allout"])




#data.plot();
#data.plot("box");
#data.plot.violin();
#data.plot.radar(cmap="inferno", show_criteria=False);

# first create the decision maker
# (with the default hiper parameters)
dm = simple.WeightedSum()

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
dm = closeness.TOPSIS(mnorm="sum")
print(dm)

print(dm.decide(data))


f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.set_title("Sum Norm")
data.plot.violin(mnorm="sum", ax=ax1);
ax2.set_title("Vector Norm")
data.plot.violin(mnorm="vector", ax=ax2);
f.set_figwidth(15)
