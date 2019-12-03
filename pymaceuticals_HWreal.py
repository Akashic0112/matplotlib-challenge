#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data

mouse_db = pd.read_csv("mouse_drug_data.csv")
clinical_db = pd.read_csv("clinicaltrial_data.csv")


mouse_db.head()


# In[2]:


clinical_db.head()


# In[3]:


# Combine the data into a single dataset
# merged_data = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
# merged_data.head()
mouseClinical_data = pd.merge(clinical_db, mouse_db, how = "left", on=["Mouse ID", "Mouse ID"])

# Display the data table for preview
mouseClinical_data.head()


# ## Tumor Response to Treatment

# In[4]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
mean_tumor_vol = mouseClinical_data.groupby(['Drug', 'Timepoint']).mean()["Tumor Volume (mm3)"]
# Convert to DataFrame
mean_tumor_vol_df = pd.DataFrame(mean_tumor_vol)
# Preview DataFrame
mean_tumor_vol_df = mean_tumor_vol_df.reset_index()
mean_tumor_vol_df.head()


# In[5]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
stderror_tumor_vol = mouseClinical_data.groupby(['Drug', 'Timepoint']).sem()["Tumor Volume (mm3)"]

# Convert to DataFrame
stderror_tumor_vol_df = pd.DataFrame(stderror_tumor_vol)
# Preview DataFrame
stderror_tumor_vol_df = stderror_tumor_vol_df.reset_index()
stderror_tumor_vol_df.head()


# In[6]:


# Minor Data Munging to Re-Format the Data Frames
#Transpose rows into columns
mean_tumor_vol_df_transpose = mean_tumor_vol_df.pivot(index = "Timepoint", columns= "Drug")["Tumor Volume (mm3)"]
stderror_tumor_vol_df_transpose = stderror_tumor_vol_df.pivot(index = "Timepoint", columns="Drug")["Tumor Volume (mm3)"]
# Preview that Reformatting worked
mean_tumor_vol_df_transpose.head()


# In[7]:


stderror_tumor_vol_df_transpose.head()


# In[29]:


# Generate the Plot (with Error Bars)
plt.errorbar(mean_tumor_vol_df_transpose.index, mean_tumor_vol_df_transpose["Capomulin"], yerr=stderror_tumor_vol_df_transpose["Capomulin"], color= 'r', marker= "o")
plt.errorbar(mean_tumor_vol_df_transpose.index, mean_tumor_vol_df_transpose["Ceftamin"], yerr=stderror_tumor_vol_df_transpose["Ceftamin"], color= 'b', marker= "^")
plt.errorbar(mean_tumor_vol_df_transpose.index, mean_tumor_vol_df_transpose["Infubinol"], yerr=stderror_tumor_vol_df_transpose["Infubinol"], color= 'g', marker= "s")
plt.errorbar(mean_tumor_vol_df_transpose.index, mean_tumor_vol_df_transpose["Ketapril"], yerr=stderror_tumor_vol_df_transpose["Ketapril"], color= 'k', marker= "D")
plt.errorbar(mean_tumor_vol_df_transpose.index, mean_tumor_vol_df_transpose["Naftisol"], yerr=stderror_tumor_vol_df_transpose["Naftisol"], color= 'c', marker= "H")

# Format the Figure
plt.ylim(20,80)
plt.xlim(0,45)

#label figure
plt.title("Tumor response to treatment", fontsize = 20)
plt.xlabel("Time (Days) ", fontsize =14)
plt.ylabel("Tumor Volume (mm3) ", fontsize =14)

#Other formating
plt.legend(["Capomulin", "Ceftamin", "Infubinol", "Ketapril", "Naftisol"])
plt.grid(axis = 'y') #(color='r', linestyle='-', linewidth=2)->more options for later

#NEED TO EXPORT GRAPH
plt.savefig("TumorTxResponse.png")

plt.show()


# ## Metastatic Response to Treatment

# In[9]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
mean_met_vol = mouseClinical_data.groupby(['Drug', 'Timepoint']).mean()["Metastatic Sites"]

# Convert to DataFrame
mean_met_vol_df = pd.DataFrame(mean_met_vol)
# Preview DataFrame
mean_met_vol_df.head()


# In[10]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
stderror_met_vol = mouseClinical_data.groupby(['Drug', 'Timepoint']).sem()["Metastatic Sites"]

# Convert to DataFrame
stderror_met_vol_df = pd.DataFrame(stderror_met_vol)
# Preview DataFrame
stderror_met_vol_df.head()


# In[11]:


# Minor Data Munging to Re-Format the Data Frames
mean_met_vol_df = mean_met_vol_df.reset_index()
mean_met_vol_df_transpose = mean_met_vol_df.pivot(index="Timepoint", columns= "Drug")["Metastatic Sites"]

stderror_met_vol_df = stderror_met_vol_df.reset_index()
stderror_met_vol_df_transpose = stderror_met_vol_df.pivot(index="Timepoint", columns= "Drug")["Metastatic Sites"]
# Preview that Reformatting worked
mean_met_vol_df_transpose.head()


# In[12]:


stderror_met_vol_df_transpose.head()


# In[28]:


# Generate the Plot (with Error Bars)
plt.errorbar(mean_met_vol_df_transpose.index, mean_met_vol_df_transpose["Capomulin"], yerr=stderror_met_vol_df_transpose["Capomulin"], color= 'r', marker= "o")
plt.errorbar(mean_met_vol_df_transpose.index, mean_met_vol_df_transpose["Ceftamin"], yerr=stderror_met_vol_df_transpose["Ceftamin"], color= 'b', marker= "^")
plt.errorbar(mean_met_vol_df_transpose.index, mean_met_vol_df_transpose["Infubinol"], yerr=stderror_met_vol_df_transpose["Infubinol"], color= 'g', marker= "s")
plt.errorbar(mean_met_vol_df_transpose.index, mean_met_vol_df_transpose["Ketapril"], yerr=stderror_met_vol_df_transpose["Ketapril"], color= 'k', marker= "D")
plt.errorbar(mean_met_vol_df_transpose.index, mean_met_vol_df_transpose["Ramicane"], yerr=stderror_met_vol_df_transpose["Naftisol"], color= 'c', marker= "H")

# Save the Figure
plt.title("Metastatic response to treatment")
plt.xlabel("Time (Days) ")
plt.ylabel("Tumor Volume (mm3) ")

#Other formating
plt.legend(["Capomulin", "Ceftamin", "Infubinol", "Ketapril", "Ramicane"])
plt.grid(axis = 'y')
plt.ylim(0,4)
#export graph
plt.savefig("MetResponsetoTx.png")

plt.show()


# ## Survival Rates

# In[14]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mice_count = mouseClinical_data.groupby(['Drug','Timepoint']).count()["Tumor Volume (mm3)"]
# Convert to DataFrame
mouse_count_df = pd.DataFrame({"mouse Count": mice_count})
# Preview DataFrame
mouse_count_df.head()


# In[15]:


# Minor Data Munging to Re-Format the Data Frames
mouse_count_df = mouse_count_df.reset_index()
mousecount_df_transpose = mouse_count_df.pivot(index="Timepoint", columns= "Drug")["mouse Count"]
# Preview that Reformatting worked
mousecount_df_transpose.head()


# In[27]:


# Generate the Plot (Accounting for percentages)
plt.plot(100 * mousecount_df_transpose["Capomulin"] / 25, "ro", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Ceftamin"] / 25, "b^", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Infubinol"] / 25, "gs", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Ketapril"] / 25, "kd", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Naftisol"] / 25, "ch", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Placebo"] / 25, "mv", linestyle="solid", markersize=5, linewidth=2)
plt.plot(100 * mousecount_df_transpose["Propriva"] / 26, "y*", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Ramicane"] / 25, "b|", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Stelasyn"] / 26, "gx", linestyle="solid", markersize=5, linewidth=1)
plt.plot(100 * mousecount_df_transpose["Zoniferol"] / 25, "cp", linestyle="solid", markersize=5, linewidth=1)
# Save the Figure
plt.title("Mouse Survival Rates by Treatment ")
plt.xlabel("Time (Days) ")
plt.ylabel("Mouse Survival Rate (%) ")

#Other formating

plt.legend(["Capomulin", "Ceftamin", "Infubinol", "Ketapril", "Naftisol", "Placebo", "Propriva", "Ramicane", "Stelasyn", "Zoniferol"], loc="best", fontsize="x-small", fancybox=True)
plt.grid(True)
plt.ylim(0,110)
plt.xlim(0,45)
#export fig
plt.savefig("MouseSurvivalRate.png")
# Show the Figure
plt.show()



# ## Summary Bar Graph

# In[17]:


# Calculate the percent changes for each drug
tumorPct_change = 100 * (mean_tumor_vol_df_transpose.iloc[-1] - mean_tumor_vol_df_transpose.iloc[0])/ mean_tumor_vol_df_transpose.iloc[0]
tumorPct_change_sem = 100 * (stderror_tumor_vol_df_transpose.iloc[-1] - stderror_tumor_vol_df_transpose.iloc[0])/ stderror_tumor_vol_df_transpose.iloc[0]
# Display the data to confirm
tumorPct_change


# In[23]:


# Store all Relevant Percent Changes into a Tuple
pct_change_t = (tumorPct_change['Capomulin'], 
               tumorPct_change['Ceftamin'],
               tumorPct_change['Placebo'],
               tumorPct_change['Ramicane'])

# print(pct_change_t)
# Splice the data between passing and failing drugs
#Need to get comfortable with both formats

fig, ax = plt.subplots()
ind = np.arange(len(pct_change_t))
width = 1
drugsPass = ax.bar(ind[0],pct_change_t[0],width, color="green")
drugsFail = ax.bar(ind[1:],pct_change_t[1:], width, color="red")
drugsPass = ax.bar(ind[3],pct_change_t[3],width, color="green")

# Orient widths. Add labels, tick marks, etc. 
#additional format, same info as before
#only takes 2-4
ax.set_ylabel('Tumor Volume Change Percentage')
ax.set_title('Tumor Change over 45 day Treatment Period')
ax.set_xticks(ind)
ax.set_xticklabels(('Capomulin', 'Ceftamin', 'Placebo', 'Ramicane'))
ax.set_autoscaley_on(False)
ax.set_ylim([-30,70])
ax.set_xlim([-0.5,3.5])
ax.grid(True)

# Use functions to label the percentages of changes(writes to place % value in visible location)
##GTS all the way...
##need to dig in and be able to replicate this
def autolabelFail(drugs):
    for drug in drugs:
        height= drug.get_height()
        ax.text(drug.get_x()+drug.get_width()/2.,3,
               '%d%%' % int(height),
               ha= 'center', va='bottom',color='white')

def autolabelPass(drugs):
    for drug in drugs:
        height= drug.get_height()
        ax.text(drug.get_x() + drug.get_width()/2.,-8,
               '-%d%%' % int(height),
               ha= 'center', va='bottom',color='white')
# Call functions to implement the function calls
autolabelPass(drugsPass)
autolabelFail(drugsFail)

# Save the Figure
fig.savefig("SummaryBars.png")

# Show the Figure
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




