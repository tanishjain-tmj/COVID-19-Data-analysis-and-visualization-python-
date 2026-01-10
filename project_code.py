import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    print("Loading COVID-19 dataset...")
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    print("Dataset loaded successfully!\n")
    return df


def analyze_data(df, country):
    country_df = df[df['location'] == country]

    total_cases = country_df['total_cases'].max()
    total_deaths = country_df['total_deaths'].max()

    print(f"COVID-19 Summary for {country}")
    print(f"Total Cases   : {int(total_cases)}")
    print(f"Total Deaths  : {int(total_deaths)}\n")

    return country_df


def advanced_analysis(country_df, country):
    country_df = country_df.copy()
    country_df['daily_cases'] = country_df['new_cases'].fillna(0)

    country_df['month'] = country_df['date'].dt.to_period('M')
    monthly_cases = country_df.groupby('month')['daily_cases'].sum()
    highest_month = monthly_cases.idxmax()

    top_5 = country_df.nlargest(5, 'daily_cases')[['date', 'daily_cases']]
    last_5 = country_df.tail(5)[['date', 'daily_cases']]

    print(f"Advanced Analysis for {country}")
    print(f"Month with highest cases: {highest_month}\n")

    print("Top 5 Days with Highest Cases:")
    print(top_5)

    print("\nLast 5 Days Data:")
    print(last_5)
    print("\n")


def visualize_trends(df, country):
    country_df = df[df['location'] == country].copy()
    country_df['daily_cases'] = country_df['new_cases'].fillna(0)

    plt.figure(figsize=(10, 5))
    plt.plot(country_df['date'], country_df['total_cases'], label='Total Cases')
    plt.title(f"COVID-19 Total Cases Over Time ({country})")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(country_df['date'], country_df['total_deaths'], color='red', label='Total Deaths')
    plt.title(f"COVID-19 Total Deaths Over Time ({country})")
    plt.xlabel("Date")
    plt.ylabel("Total Deaths")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.hist(country_df['daily_cases'], bins=50, color='skyblue')
    plt.title(f"Histogram of Daily New Cases ({country})")
    plt.xlabel("Daily Cases")
    plt.ylabel("Frequency")
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.scatter(country_df['total_cases'], country_df['total_deaths'], alpha=0.5)
    plt.title(f"Cases vs Deaths Scatter Plot ({country})")
    plt.xlabel("Total Cases")
    plt.ylabel("Total Deaths")
    plt.show()

    latest = country_df.iloc[-1]
    plt.figure(figsize=(6, 6))
    plt.pie(
        [latest['total_cases'], latest['total_deaths']],
        labels=['Total Cases', 'Total Deaths'],
        autopct='%1.1f%%',
        colors=['lightblue', 'red']
    )
    plt.title(f"Cases vs Deaths Distribution ({country})")
    plt.show()

    # Monthly bar chart
    country_df['month'] = country_df['date'].dt.to_period('M')
    monthly = country_df.groupby('month')['daily_cases'].sum()

    monthly.plot(kind='bar', figsize=(12, 5), color='green')
    plt.title(f"Monthly COVID-19 Cases ({country})")
    plt.xlabel("Month")
    plt.ylabel("Cases")
    plt.tight_layout()
    plt.show()

    # Quarterly bar chart 
    country_df['quarter'] = country_df['date'].dt.to_period('Q')
    quarterly = country_df.groupby('quarter')['daily_cases'].sum()

    quarterly.plot(kind='bar', figsize=(10, 5), color='purple')
    plt.title(f"Quarterly COVID-19 Cases ({country})")
    plt.xlabel("Quarter")
    plt.ylabel("Cases")
    plt.tight_layout()
    plt.show()


def compare_countries(df):
    latest_date = df['date'].max()
    latest_data = df[df['date'] == latest_date]

    plt.figure(figsize=(8, 5))
    sns.barplot(x='location', y='total_cases', data=latest_data)
    plt.title("Total COVID-19 Cases by Country (Latest Date)")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.show()


if __name__ == "__main__":

    covid_df = load_data("owid_covid_data.csv")

    for country in ["India", "USA", "Brazil"]:
        country_df = analyze_data(covid_df, country)
        advanced_analysis(country_df, country)
        visualize_trends(covid_df, country)

    compare_countries(covid_df)






