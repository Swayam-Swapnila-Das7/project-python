#import all libraries needed
import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt

try :
    #import both shapefile and data set
    data = pd.read_csv("Covid-19_status_of_india.csv")
    indian_map = gpd.read_file("India.geojson")

except FileNotFoundError as e :
    print(f"Error : {e} . ensure that file is at right directory.")
    exit( )

#make two column names equal , one from each
indian_map = indian_map.rename(columns = {"STNAME" : "State"})
data = data.rename(columns={"State/UTs":"State"})

#ensure consistent spellingand casing
indian_map["State"] = indian_map["State"].str.upper().str.strip()
data["State"] = data["State"].str.upper().str.strip()

#merged the data sets
merge_data = indian_map.merge(data,on = "State",how = "left")

fig,ax = plt.subplots(1,1,figsize = (15,15))

merge_data.plot(
    column = "Discharge Ratio",
    ax = ax ,
    #edgecolor="black",  use if needed
    legend = True ,
    cmap = "berlin",
    missing_kwds = {"color":"green",
                    "edgecolor":"red",
                    "hatch":" ",
                    "label":"missing values"
    })
ax.set_title(f"Analysis of COVID-19 Patient Discharge Rates : \nA State-Level Geospatial Study using Python\n(Green fill with red border indicates missing data)",
                fontdict = {"fontsize":"20",
                         "fontweight":"7",
                         "color":"indigo",
                         "fontweight" : "bold"
                         })

ax.axis("off")
plt.show()
plt.savefig("covid-19_data analysis.png",dpi = 300)

