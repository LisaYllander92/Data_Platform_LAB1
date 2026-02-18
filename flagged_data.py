import pandas as pd


df = pd.read_csv("products_cleaned.csv")

# Skapa en kopia så vi inte ändrar originalet
branching_df = df.copy()

# Konvertera price-kolumnen till numerisk (text som "free" blir NaN)
branching_df["price"] = pd.to_numeric(branching_df["price"], errors='coerce')

# --- CONDITIONS: Skapa True/False för olika problem ---

# Saknat ID (NaN i id-kolumnen)
missing_id_condition = branching_df["id"].isna()

# Tomt namn trots att värde finns (bara whitespace)
wrong_name_condition = (branching_df["name"].astype(str).str.strip() == "") & branching_df["name"].notna()

# Ogiltigt prisformat (blev NaN efter to_numeric, dvs var text som "free")
invalid_price_condition = branching_df["price"].isna()

# Orimligt pris (negativt, noll, eller över 4000) men inte NaN
wrong_price_condition = (
    (branching_df["price"] < 0) |       # Negativt pris
    (branching_df["price"] == 0) |      # Gratis (misstänkt)
    (branching_df["price"] > 4000)      # Extremt högt pris
) & branching_df["price"].notna()       # Men INTE NaN (hanteras av invalid_price)

# Felaktig valuta
wrong_currency_condition = (branching_df["currency"].astype(str).str.strip().str.len() != 3) & branching_df["currency"].notna()

# Ogiltigt datum
wrong_date_condition = pd.to_datetime(branching_df["created_at"], errors='coerce').isna() & branching_df["created_at"].notna()

# --- AVVISA: Omöjliga värden som måste kastas ---
branching_df["is_rejected"] = (
    missing_id_condition |      # Saknat ID → kan inte identifiera produkten
    invalid_price_condition     # Ogiltigt prisformat → kan inte använda priset
)

# --- FLAGGA: Misstänkta värden som behöver granskas ---
branching_df["is_flagged"] = (
    wrong_name_condition |      # Tomt namn → fel vid datainmatning?
    wrong_price_condition |     # Konstigt pris → kolla om det stämmer
    wrong_currency_condition |  # Fel valutaformat → kolla om det stämmer
    wrong_date_condition        # Ogiltigt datum → kolla om det stämmer
)

# --- SPARA: Generera output-filer ---

# Spara bara de avvisade produkterna
rejected_df = branching_df[branching_df["is_rejected"] == True]
rejected_df.to_csv("rejected_values.csv", index=False)

# Spara bara de flaggade produkterna (misstänkta)
flagged_df = branching_df[branching_df["is_flagged"] == True]
flagged_df.to_csv("flagged_values.csv", index=False)

# Spara hela datasetet med is_rejected och is_flagged kolumner
branching_df.to_csv("products_overview.csv", index=False)