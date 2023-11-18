from datetime import datetime
import pandas as pd
import subprocess
import matplotlib.pyplot as plt

from clean_data.clean_technologies import (
    split_technologies,
    transform_technologies
)

subprocess.run(['scrapy', 'crawl', 'djinni_spider', '-O', 'djinni.csv'])

df = pd.read_csv("djinni.csv")

technologies_series = df['technologies'].apply(split_technologies).explode()

trasformed = technologies_series.apply(transform_technologies)
trasformed.replace('', pd.NA, inplace=True)
trasformed.drop(trasformed[trasformed == "fullstack"].index, inplace=True)
trasformed.dropna(inplace=True)

fig, ax = plt.subplots()
fig.set_size_inches(15, 12)
ax.bar(trasformed.value_counts()[1:21].index, trasformed.value_counts()[1:21])
ax.set_title("Top 20 Technologies for Python Developers (Python excluded)")
ax.set_xlabel("Technologies")
ax.set_ylabel("Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.savefig(f"results/top-20-technologies-{datetime.now().date()}.png")
