import pandas as pd


def get_post_codes():
    df=pd.read_csv("./data/australian_postcodes.csv")
    df = df[df["state"]=="NSW"]
    df.rename(columns={"long":"longitude", "lat":"latitude"}, inplace=True)
    interested_columns=["postcode", "longitude", "latitude"]
    df=df[interested_columns]
    df=df.drop_duplicates(subset='postcode', keep="first")
    df=df[df['longitude']  > 0]
    return df

def covid_data():
    df=pd.read_csv("./data/covid-19-cases-by-notification-date-and-postcode-local-health-district-and-local-government-area.csv")
    df[['postcode']] = df[['postcode']].fillna(value=0)
    df.postcode = df.postcode.astype(int)
    return df


if __name__ == "__main__":
    covid_df = covid_data()
    post_df = get_post_codes()
    # covid_df = covid_df.join(post_df, how="left", on='postcode', rsuffix='_other')
    covid_df = covid_df.merge(post_df, how="left", on="postcode")
    covid_df.to_csv("./nsw_covid_enriched_data.csv")
    
    