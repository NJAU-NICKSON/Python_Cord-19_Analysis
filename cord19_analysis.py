# Part 1: Data Loading and Basic Exploration
import os
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import streamlit as st

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# Load the metadata.csv file (must be in the same directory as this script)
df = pd.read_csv("metadata.csv")

# Show basic information
print("Data dimensions:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum().head(20))
print("\nBasic statistics:\n", df.describe())


# Part 2: Data Cleaning and Preparation

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract year
df["year"] = df["publish_time"].dt.year

# Create a column for abstract word count (if available)
df["abstract_word_count"] = df["abstract"].astype(str).apply(lambda x: len(x.split()))

# Handle missing values: drop rows missing title or publish_time
df_clean = df.dropna(subset=["title", "publish_time"]).copy()

print("Cleaned data dimensions:", df_clean.shape)

# Part 3: Data Analysis and Visualization

# 1. Count papers by year
year_counts = df_clean["year"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values)
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.title("Publications by Year")
plt.tight_layout()
plt.savefig("outputs/publications_by_year.png")
plt.close()

# 2. Top journals
top_journals = df_clean["journal"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.title("Top Journals Publishing COVID-19 Research")
plt.tight_layout()
plt.savefig("outputs/top_journals.png")
plt.close()

# 3. Word cloud of titles
titles = " ".join(df_clean["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
wordcloud.to_file("outputs/title_wordcloud.png")

# 4. Distribution by source
source_counts = df_clean["source_x"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=source_counts.values, y=source_counts.index)
plt.xlabel("Number of Papers")
plt.ylabel("Source")
plt.title("Distribution of Paper Counts by Source")
plt.tight_layout()
plt.savefig("outputs/top_sources.png")
plt.close()

print("Analysis complete. Visualizations saved in 'outputs/' folder.")


# Part 4: Streamlit Application
def run_streamlit_app():
    st.title("CORD-19 Data Explorer")
    st.write("Simple exploration of COVID-19 research papers")

    # Sidebar filters
    year_range = st.slider("Select year range",
                           int(df_clean["year"].min()),
                           int(df_clean["year"].max()),
                           (2020, 2021))

    # Filter data
    filtered_df = df_clean[
        (df_clean["year"] >= year_range[0]) & (df_clean["year"] <= year_range[1])
    ]

    st.subheader("Sample of Data")
    st.write(filtered_df.head())

    # Publications by year
    st.subheader("Publications by Year")
    year_counts_filtered = filtered_df["year"].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(year_counts_filtered.index, year_counts_filtered.values)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Publications")
    ax.set_title("Publications by Year")
    st.pyplot(fig)

    # Top journals
    st.subheader("Top Journals")
    top_journals_filtered = filtered_df["journal"].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_journals_filtered.values, y=top_journals_filtered.index, ax=ax)
    ax.set_title("Top Journals Publishing COVID-19 Research")
    st.pyplot(fig)

    # Word cloud
    st.subheader("Word Cloud of Titles")
    titles = " ".join(filtered_df["title"].dropna().astype(str).tolist())
    if titles.strip():
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.write("No titles available for the selected range.")
