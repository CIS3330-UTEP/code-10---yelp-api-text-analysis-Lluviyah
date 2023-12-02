import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cars.csv')

car_brands = ['Honda','Toyota','Mazda']

df = df.query("Identification_Make == @car_brands")

print(df.groupby('Identification_Make').describe())


selected_columns = ["Dimensions_Height",'Fuel_Information_Highway_mpg','Engine_Information_Engine_Statistics_Torque']

corr_matrix = df[selected_columns].corr(numeric_only=True).round(2)

sns.heatmap(corr_matrix, annot=True, vmax = 1 , vmin= -1, cmap = 'coolwarm')
plt.show()

i = 0
while i < len(selected_columns):
    df.boxplot(column=selected_columns[i],by='Identification_Make')
    plt.show()
    i +=1


