
import pandas as pd, numpy as np, matplotlib.pyplot as plt, os
df = pd.read_csv("ai4i2020.csv")
df["Temperature Difference"] = df["Process temperature [K]"] - df["Air temperature [K]"]
df["Mechanical Power"] = df["Torque [Nm]"] * df["Rotational speed [rpm]"] * (2*np.pi/60)
os.makedirs("images", exist_ok=True)
df["Machine failure"].value_counts().sort_index().plot(kind="bar")
plt.title("Machine failure distribution"); plt.xlabel("Machine failure"); plt.ylabel("Count")
plt.tight_layout(); plt.savefig("images/failure_distribution.png", dpi=150); plt.close()
print("Saved to images/")
