## Running Results Database

Tento projekt představuje webovou aplikaci sloužící jako databáze atletických výsledků. Cílem aplikace je umožnit evidenci a prohlížení informací o **běžcích**, **závodech** a jejich **výsledcích**. Atletické závody generují velké množství dat a jejich organizace v databázovém systému umožňuje efektivní vyhledávání, analýzu a správu těchto informací.

Základními entitami systému jsou **běžec**, **závod** a **výsledek**. Každý závod obsahuje informace jako **název závodu**, **datum konání**, **místo konání** a **délku tratě**. Každý běžec je reprezentován atributy jako **jméno**, **příjmení**, **datum narození** a **klub**. Entita **výsledek** propojuje běžce a závod a obsahuje údaje o **čase výkonu** a **umístění**.

Systém rozlišuje několik rolí uživatelů. **Anonymní návštěvník** může prohlížet seznam závodů a výsledků. **Registrovaný uživatel** může přidávat nové výsledky nebo komentáře k závodům. **Administrátor** má plná oprávnění ke správě databáze a může vytvářet, upravovat nebo mazat záznamy o běžcích, závodech a výsledcích.

Aplikace umožňuje filtrovat závody podle data nebo distance a zobrazovat výsledky jednotlivých běžců. V budoucnu může být systém rozšířen o statistiky výkonů, **osobní rekordy** nebo přehled **sezóny**.

Projekt je implementován pomocí frameworku **Django** a relační **databáze**, která využívá vazby mezi entitami typu jeden k mnoha, například mezi běžcem a jeho výsledky nebo mezi závodem a jeho účastníky.

![Wireframe 1](images/IMG_20260305_203358.jpg.pdf)
![Wireframe 2](images/IMG_20260305_204221.jpg.pdf)
![Diagram](images/IMG_20260305_204244.jpg.pdf)
