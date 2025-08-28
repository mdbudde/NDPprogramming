import os
import pandas as pd
import numpy as np


# Example usage
dataHeaders =  ["AnimalID", "Group", "Trial", "Active Time", "Total Time"]


groups = ['Control', 'Treatment']
times = [300, 400]
for i in range(1, 30):
    data = pd.DataFrame(columns=dataHeaders)
    for s in range(1, 6):
        if i > 15:
            active_time = np.random.normal(loc=times[0], scale=50)  # Random number with mean 300 and std deviation 50
            group = groups[0]
        else:
            active_time = np.random.normal(loc=times[1], scale=50)
            group = groups[1]

        data.loc[s] = {"AnimalID": i, "Group": group, "Trial": s, "Active Time": active_time, "Total Time": 500}

    print(data)
    filename = f"animal_data_{i}.xlsx"
    fileout = os.path.join("AnimalData",filename)
    print(fileout)
    data.to_excel(fileout, index=False)
