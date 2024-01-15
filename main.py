from datetime import datetime
import pandas as pd
import subprocess
import matplotlib.pyplot as plt

from clean_data.clean_technologies import (
    split_technologies,
    transform_technologies,
    exclude_technologies
)


def get_exclude_technologies():
    technologies_input = input(
        "Enter the technologies, comma separated \n"
        "(leave blank if nothing to exclude): \n"
    )
    technologies_list = technologies_input.split(",")
    technologies_list = list(
        filter(lambda x: x != "", map(lambda x: x.strip(), technologies_list))
    )

    df = pd.DataFrame({"technologies": technologies_list})

    df.to_csv("clean_data/exclude.csv")


get_exclude_technologies()

subprocess.run(['scrapy', 'crawl', 'djinni_spider', '-O', 'djinni.csv'])

df = pd.read_csv("djinni.csv")

technologies_series = df['technologies'].apply(split_technologies).explode()

trasformed = technologies_series.apply(transform_technologies)
trasformed = trasformed.apply(exclude_technologies)
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
