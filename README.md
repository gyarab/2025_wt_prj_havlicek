## Running Results Database

Tento projekt představuje webovou aplikaci sloužící jako databáze atletických výsledků. Cílem aplikace je umožnit evidenci a prohlížení informací o _běžcích_, _závodech_ a jejich _výsledcích_. Atletické závody generují velké množství dat a jejich organizace v databázovém systému umožňuje efektivní vyhledávání, analýzu a správu těchto informací.

Základními entitami systému jsou _běžec_, _závod_ a _výsledek_. Každý _závod_ obsahuje informace jako _název závodu_, _datum konání_, _místo konání_ a _délku tratě_. Každý _běžec_ je reprezentován atributy jako _jméno_, _příjmení_, _datum narození_ a _klub_. Entita _výsledek_ propojuje běžce a závod a obsahuje údaje o _čase výkonu_ a _umístění_.

Systém rozlišuje několik rolí uživatelů. _Anonymní návštěvník_ může prohlížet seznam závodů a výsledků. _Registrovaný uživatel_ může přidávat nové výsledky nebo komentáře k závodům. _Administrátor_ má plná oprávnění ke správě databáze a může vytvářet, upravovat nebo mazat záznamy o běžcích, závodech a výsledcích.

Aplikace umožňuje filtrovat závody podle data nebo distance a zobrazovat výsledky jednotlivých běžců. V budoucnu může být systém rozšířen o statistiky výkonů, osobní rekordy nebo přehled sezónních výsledků.

Projekt je implementován pomocí frameworku Django a relační databáze, která využívá vazby mezi entitami typu jeden k mnoha, například mezi běžcem a jeho výsledky nebo mezi závodem a jeho účastníky.
