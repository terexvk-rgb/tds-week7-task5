import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Generate synthetic data with correct mapping
np.random.seed(42)
channels = ["Email", "Chat", "Phone", "Social Media"]

data = []
data.extend([("Email", rt) for rt in np.random.normal(loc=30, scale=10, size=150)])
data.extend([("Chat", rt) for rt in np.random.normal(loc=5, scale=2, size=150)])
data.extend([("Phone", rt) for rt in np.random.normal(loc=15, scale=5, size=150)])
data.extend([("Social Media", rt) for rt in np.random.normal(loc=45, scale=15, size=150)])

df = pd.DataFrame(data, columns=["Channel", "ResponseTime"])

# 2. Professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# 3. Create figure (512x512 pixels)
plt.figure(figsize=(8, 8))

# 4. Violinplot
sns.violinplot(
    x="Channel",
    y="ResponseTime",
    data=df,
    palette="Set2",
    inner="quartile"
)

# 5. Labels and title
plt.title("Customer Support Response Time Distribution by Channel", fontsize=14)
plt.xlabel("Support Channel")
plt.ylabel("Response Time (minutes)")

# 6. Save as PNG with exact 512x512 output
plt.savefig("chart.png", dpi=64)
plt.close()
