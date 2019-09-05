import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sys
import pickle

dataset = sys.argv[1]

mf = pickle.load(open("../data/"+str(dataset)+"/mf_result.dat","rb"))
ripple = pickle.load(open("../data/"+str(dataset)+"/ripple_result.dat","rb"))
df = pd.concat([mf,ripple])

precison = df[df.Measure=="Precision"]
precison["Value"] = precison["Value"]/4
recall = df[df.Measure=="Recall"]
recall["Value"] = recall["Value"]/4
F1 = df[df.Measure=="F1"]
F1["Value"] = F1["Value"]/4

sns.set(style='darkgrid')
sns.pointplot(x="K", y="Value",hue="Method", data=precison,legend=False,
palette={"Ripple": "r", "MF": "b"},
markers=["^", "o"], linestyles=["-", "--"],capsize=0.1)
plt.ylabel("Precision@K")
plt.grid(True)
plt.gca().legend().remove()
plt.savefig("Precision_"+str(dataset))

plt.clf()
sns.set(style='darkgrid')
ax = sns.pointplot(x="K", y="Value",hue="Method", data=recall,
palette={"Ripple": "r", "MF": "b"},
markers=["^", "o"], linestyles=["-", "--"],capsize=0.1,legend=False)
plt.ylabel("Recall@K")
plt.grid(True)
plt.gca().legend().remove()
plt.savefig("Recall_"+str(dataset))

plt.clf()
sns.set(style='darkgrid')
sns.pointplot(x="K", y="Value",hue="Method", data=F1,
palette={"Ripple": "r", "MF": "b"},
markers=["^", "o"], linestyles=["-", "--"],capsize=0.1,legend=False)
plt.ylabel("F1@K")
plt.grid(True)
plt.gca().legend().remove()
plt.savefig("F1_"+str(dataset))