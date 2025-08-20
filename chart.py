import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Generate synthetic data
np.random.seed(42)
channels = ["Email", "Chat", "Phone", "Social Media"]
data = {
    "Channel": np.random.choice(channels, size=600),
    "ResponseTime": np.concatenate([
        np.random.normal(loc=30, scale=10, size=150),   # Email
        np.random.normal(loc=5, scale=2, size=150),     # Chat
        np.random.normal(loc=15, scale=5, size=150),    # Phone
        np.random.normal(loc=45, scale=15, size=150)    # Social Media
    ])
}
df = pd.DataFrame(data)

# 2. Styling for professional look
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

# 6. Save as PNG with 512x512 resolution
plt.savefig("chart.png", dpi=64)
plt.close()
