# E-commerce-Price-Monitoring-Enrichment-Pipeline

## Përshkrim
Ky projekt implementon një pipeline modular për përpunimin e të dhënave, i cili:
1.bën web scraping të produkteve (libra) nga një website publik demo
2.bën pasurim (enrichment) të të dhënave duke konvertuar çmimet me një Currency Exchange API (me fallback nëse API kryesore bie)
3.bën enkriptim të një fushe sensitive (titulli i produktit) me Fernet (AES)
4.ruan rezultatet në JSON dhe CSV.
Pipeline ekzekutohet nga main.py.


## Arkitektura e Projektit
*scraping/ – Nxjerr të dhënat nga website-i (titull, çmim, availability)
*api/ – Merr kurset e këmbimit (FX rates) nga API (me fallback)
*processing/ – Pastron/validon dhe pasuron të dhënat (GBP → EUR/ALL)
*security/ – Enkriptim me Fernet (AES) dhe menaxhim i çelësit nga .env
*storage/ – Ruajtje e output-it në JSON dhe CSV
*main.py – Orkestron të gjithë rrjedhën

Rrjedha e të Dhënave
Website → Scraper → Raw Data → API Enrichment → Processing → Encryption → Storage (JSON/CSV)

## Teknologjitë:
*Python
*requests, beautifulsoup4 (scraping + API calls)
*Currency Exchange API (me fallback)
*cryptography (Fernet AES) për enkriptim
*python-dotenv për leximin e .env

## Siguria
*Çelësi i enkriptimit ruhet në .env (lokalisht) dhe nuk ngarkohet në GitHub.
*.env.example shërben si udhëzues (pa sekret).
*Nëse FERNET_KEY mungon, moduli i sigurisë mund ta gjenerojë automatikisht gjatë ekzekutimit (nëse është aktivizuar në security/encryption.py).

## Kërkesat Paraprake per ekzekutim (Prerequisites)
Për ekzekutimin e projektit kërkohen:

- **Python 3.10 ose më i ri**
- **Git** (për klonimin e repository nga GitHub)
- Lidhje interneti (për web scraping dhe API)

Sigurohuni që Python dhe Git janë të instaluara dhe të aksesueshme nga command line.

## Si të Ekzekutohet Projekti
1) Shkarko prjektin si ZIP file
2) Bej extract, file ZIP qe shkarkove
3) Hap ne terminal file qe more mbas extract
4) EKZEKUTO locationin ku do ta klonosh me comanden: cd FILE=QE=DO
5) EKZEKUTO: git clone https://github.com/Kristi-Madolli/E-commerce-Price-Monitoring-Enrichment-Pipeline.git
6) File qe perfiton mbas klonimit hape ne terminal
7) Ndiq gjithe hapat e meposhtem ne terminalin e fundit qe hape
1) Instalimi i varësive nga root i projektit (ku është main.py)    
EKZEKUTO: python -m pip install -r requirements.txt
2) Krijimi i .env (nëse nuk krijohet automatikisht)
Krijo një file .env në root dhe vendos:
EKZEKUTO: FERNET_KEY=KEY_QE_GJENERON
3) Gjenero key me:
EKZEKUTO: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
5) Ekzekutimi i pipeline-it: 
EKZEKUTO: python main.py


## Output
Pas ekzekutimit krijohen: *output.json, *output.csv
Këto përmbajnë të dhëna të pasuruara dhe me titull të enkriptuar (title_encrypted).

## Shënime
*price_all mund të dalë None nëse API nuk ofron kurs për ALL në atë moment. Kjo trajtohet në mënyrë të kontrolluar (pa prishur pipeline-in).
*Projekti ka strukturë modulare dhe histori zhvillimi me commit-e.

## Autori
Kristi Madolli

