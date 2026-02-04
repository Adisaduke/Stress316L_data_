import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/data.csv')

# clean
df = df.dropna()
df = df[(df["strain"] >= 0) & (df["stress"] >= 0)]

# 🔴 SORT FIRST
df = df.sort_values(by="strain").reset_index(drop=True)

# 🔴 THEN SMOOTH
df["stress_smooth"] = df["stress"].rolling(window=50).mean()

# plot
plt.figure(figsize=(6, 4))
plt.plot(df["strain"], df["stress"], alpha=0.3, label="Raw data")
plt.plot(df["strain"], df["stress_smooth"], label="Smoothed curve")
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.legend()
plt.savefig("images/stress_strain_curve.png", dpi=300, bbox_inches="tight")
plt.show()


max_stress = df["stress"].max()
max_stress
strain_at_max_stress = df.loc[df["stress"].idxmax(), "strain"]
strain_at_max_stress

print(f"Maximum stress: {max_stress:.2f}")
print(f"Strain at maximum stress: {strain_at_max_stress:.4f}")

