#Attaching packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1. Importing dataset
DT = pd.read_csv("FACS_cell_RNA_yield_data.csv")
#2. Converting dataset to dataframe
DT = pd.DataFrame(DT)
#3. Converting RH.index to categorical
DT['RH.index'] = DT['RH.index'].astype('category')

#4. Plotting Cell yield
#4.1 Melting data and preserving only
cell_plot_data = pd.melt(DT.iloc[:,:3], id_vars=['RH.index'])
#4.2 Creating the actual plot
cell_plot = sns.violinplot(x='variable', y='value', data=cell_plot_data, palette=sns.color_palette('Paired'))
cell_plot.set(xlabel='mCherry+IDmBMSC type', ylabel="Number of cells", title="Cell yield (FACS)")
#plt.savefig('cell_plot.jpg')

#5. Plotting RNA yield
#5.1 Creating new variables with total RNA
DT['mCherry+CD45+ [RNA]'] = DT['RNA_CD45+']*DT['ul']
DT['mCherry+CD45- [RNA]'] = DT['RNA_CD45-']*DT['ul']
#5.2 Creating the actual plot
RNA_plot_data = pd.melt(DT.iloc[:,[0,7,8]], id_vars=['RH.index'])
RNA_plot = sns.violinplot(x='variable', y='value', data=RNA_plot_data, palette=sns.color_palette('Paired')[4:6])
RNA_plot.set(xlabel='mCherry+IDmBMSC type', ylabel='ng', title="RNA yield (FACS)")
#plt.savefig('RNA_plot.jpg')

