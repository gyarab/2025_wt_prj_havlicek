## Running Results Database

Tento projekt představuje webovou aplikaci sloužící jako databáze atletických výsledků. Cílem aplikace je umožnit evidenci a prohlížení informací o <u>běžcích</u>, <u>závodech</u> a jejich <u>výsledcích</u>. Atletické závody generují velké množství dat a jejich organizace v databázovém systému umožňuje efektivní vyhledávání, analýzu a správu těchto informací.

Základními entitami systému jsou <u>běžec</u>, <u>závod</u> a <u>výsledek</u>. Každý závod obsahuje informace jako <u>název závodu</u>, <u>datum konání</u>, <u>místo konání</u> a <u>délku tratě</u>. Každý běžec je reprezentován atributy jako <u>jméno</u>, <u>příjmení</u>, <u>datum narození</u> a <u>klub</u>. Entita výsledek propojuje běžce a závod a obsahuje údaje o <u>čase výkonu</u> a <u>umístění</u>.

Systém rozlišuje několik rolí uživatelů. <u>Anonymní návštěvník</u> může prohlížet seznam závodů a výsledků. <u>Registrovaný uživatel</u> může přidávat nové výsledky nebo komentáře k závodům. <u>Administrátor</u> má plná oprávnění ke správě databáze a může vytvářet, upravovat nebo mazat záznamy o běžcích, závodech a výsledcích.

Aplikace umožňuje filtrovat závody podle data nebo distance a zobrazovat výsledky jednotlivých běžců. V budoucnu může být systém rozšířen o statistiky výkonů, <u>osobní rekordy</u> nebo přehled <u>sezóny</u>.

Projekt je implementován pomocí frameworku <u>Django</u> a relační <u>databáze</u>, která využívá vazby mezi entitami typu jeden k mnoha, například mezi běžcem a jeho výsledky nebo mezi závodem a jeho účastníky.
