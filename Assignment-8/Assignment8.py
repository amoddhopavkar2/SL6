
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Visualize.csv')
df.index = df['Time Stamp']
df.drop('Time Stamp',axis=1,inplace=True)
df.head()
#Plotting temperature against time
plt.plot(df.index[0:100],df['T'][0:100])
plt.title('Temperature Rise')
plt.ylabel('Temp');
plt.show()
plt.plot(df.index[0:1000],df['C6H6(GT)'][0:1000])
plt.title('C6H6')
plt.ylabel('GT level');
plt.show()

var1 = df['CO(GT)']
var2 = df['T']


# In[27]:


plt.plot(df.index[0:1000],df['CO(GT)'][0:1000])
plt.plot(df.index[0:1000],df['PT08.S5(O3)'][0:1000])
plt.title('C6H6')
plt.ylabel('GT level');
plt.show()





