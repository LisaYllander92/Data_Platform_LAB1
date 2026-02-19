# Teori
### Data Ingestion:
- Är processen att samla och importera data från olika källor för validering, formatering och vidare analys.
- Exempel från vår kod: 
  - df = pd.read_csv("products.csv", sep=";")

### Data Storage: 
- Är där data lagras efter ingest, oftast i databaser (PostgreSQL, MySQL) eller data lakes. Data kan vara raw (obearbetad) eller processed (transformerad).
- Exempel från vår kod: 
  - Sparat bearbetad data i csv-filer såsom "products_cleaned.csv"  

### Transformed data:
- Är processen att städa, strukturera, summera och integrera data för att göra den användbar.
- Exempel från vår kod: 
  - cleaning_data["id"] = cleaning_data["id"].drop_duplicates() plockar bort id-dubbletter

### Data Access:
- Är när slutanvändare eller applikationer hämtar/läser data från storage för analys, rapportering eller visualisering. 
- Exempel: SQL-queries, API-anrop, dashboards.
- Exempel från vår kod: 
  - df = pd.read_csv("producs_cleaned.csv") eller bara öppnar csv-filerna för att se resultatet

### Psycopg3:
- Är en modern PostgreSQL adapter för Python som används för att köra SQL-queries och kommunicera med PostgreSQL-databaser.

### Pandas: 
- Är ett open-source bibliotek för Python som används för att ändra, städa och analysera data. 
Det använder DataFrames (tabeller) och Series (kolumner) för att hantera CSV, Excel, SQL och andra dataformat.
_ Exempel från vår kod:
  - median_price = analytics["price"].median()
  - missing_price = pd.to_numeric(products["price"], errors='coerce').isnull().sum()

### Pydantic:
- Är ett Python-bibliotek för datavalidering och parsing genom type hints. 
Det säkerställer strukturen vid körning, vilket är användbart för API:er och applikationer.

### ETL (Extract, Transform, Load):
- Är processen att kombinera data från flera källor till ett datalager. 
ETL använder regler för att rensa och organisera rådata och förbereda den för förvaring, data analys och maskininlärning. 
Syftet är att förbereda datan till ett format och struktur som är lättare för analysändamål
- Exempel från vår kod: 
  - Extract --> läser in csv-fil
  - Transform --> transformerar datan i csv-filen för att göra den användbar
  - Load --> sparar transformerad data i separata csv-filer