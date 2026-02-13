# 2025_wt_prj_havlicek
Vznikla v předmětu Webové technologie na Gymnáziu Arabská ve školním roce 2025/2026.

Local development
Aplikace používá Python Virtual Environment, před spuštěním je potřeba vytvořit venv (pokud neexistuje):

# Linux
python3 -m venv venv

# Windows
py -3 -m venv venv
Dále je třeba venv aktivovat:

# [Linux]
source ./venv/bin/activate

# Windows - Bash
source ./venv/Scripts/activate

# Windows - Power shell
...
Je třeba ujistit se, že jsou nainstalovány všechny závislosti:

# (venv)$
pip install -r requirements.txt
