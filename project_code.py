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
    print("----------------------------")
    print(f"Total Cases   : {int(total_cases)}")
    print(f"Total Deaths  : {int(total_deaths)}\n")

    return country_df

def visualize_trends(df, country):
    country_df = df[df['location'] == country]

    # Line chart – Total cases over time
    plt.figure(figsize=(10, 5))
    plt.plot(country_df['date'], country_df['total_cases'], label='Total Cases')
    plt.title(f"COVID-19 Total Cases Over Time ({country})")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Line chart – Total deaths over time
    plt.figure(figsize=(10, 5))
    plt.plot(country_df['date'], country_df['total_deaths'], color='red', label='Total Deaths')
    plt.title(f"COVID-19 Total Deaths Over Time ({country})")
    plt.xlabel("Date")
    plt.ylabel("Total Deaths")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def compare_countries(df):
    latest_date = df['date'].max()
    latest_data = df[df['date'] == latest_date]

    plt.figure(figsize=(8, 5))
    sns.barplot(
        x='location',
        y='total_cases',
        data=latest_data
    )
    plt.title("Total COVID-19 Cases by Country (Latest Date)")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    covid_df = load_data("owid_covid_data.csv")

    analyze_data(covid_df, "India")
    analyze_data(covid_df, "USA")
    analyze_data(covid_df, "Brazil")

    visualize_trends(covid_df, "India")
    visualize_trends(covid_df, "USA")
    visualize_trends(covid_df, "Brazil")

    compare_countries(covid_df)
