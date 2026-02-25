# Data Platform LAB 1 - Data Pipeline: Product Ingestion & Validation 🚀

### Utvecklat av Lisa Yllander & Rickard Garnau
<img src="img.png" alt="Lisa & Rickard" width="400"> 

## 📋 Projektöversikt
Detta projekt demonstrerar en komplett ETL-pipeline byggd i Python. Syftet är att hantera produktdata genom att läsa in rådata, genomföra avancerad datatvätt (cleaning), identifiera avvikelser och generera analytiska underlag.

## 🛠 Teknikstack
* Programmering & Logik:
    * Python – Huvudspråk för pipelinen.
    * Pandas – För kraftfull datamanipulering och transformering.
    * Pydantic – För strikt datavalidering och schemakontroll.
* Datahantering:
    * CSV – Används som format för både rådata (Ingestion) och slutresultat (Access).
    * ETL-metodik – Strukturerat flöde för Extract, Transform, Load.
* Verktyg & Miljö:
    * uv – Modern och blixtsnabb pakethantering och miljöhantering.
    * Git & GitHub – Versionshantering med ett strukturerat Feature Branch Workflow.

## 📊 Analys & Resultat
Pipelinen genererar automatiskt följande insikter:
* Analytics Summary: Aggregerad data med snittpris, median och statistik över saknade värden.
* Price Analysis: Identifiering av de 10 dyraste produkterna samt prisavvikelser.
* Data Integrity: En dedikerad rapport över avvisade produkter för att säkerställa datakvalitet i mål-systemet.

## 💻 Installation & Körning
Vi använder uv för en snabb och säker utvecklingsmiljö. 
1. Klona repot: 
```bash
git clone git@github.com:LisaYllander92/Data_Platform_LAB1.git
```
2. Synka miljön: 
```bash
uv sync
```
Kör programmet:
```bash
uv run <filnamn.py>
```

## 🤝 Workflow & Samarbete
Vi har arbetat med en Feature Branch Workflow för att säkerställa en stabil main-branch.
1. Add collaborators to repo in GitHub to work together 
2. Skapa branch: git checkout -b feature/namn
3. Synka: git pull origin main
4. Pusha: git push origin feature/namn




