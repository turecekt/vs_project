Požadavky na projekt
Projekt bude řešen formou forku a odevzdán pomocí pull requestu na githubu
Projekt může zpracovávat tým o 2-5 studentech:
hlavní řešitel vytvoří fork a pozve do něj ostatní spoluřešitele
každý z řešitelů musí mít v projektu zařazeny commity
nakonec hlavní řešitel odevzdá projekt pomocí pull requestu
Projekt musí být napsán v programovacím jazyce Python verze 3.*
Témata projektu jsou popsána v přiloženém pdf dokumentu
Kód musí být okomentovaný (všechny entity) a být vyčištěn (linterem flake8)
Kód musí obsahovat unit testy (pokrytí kódu musí být alespoň 66%)
Kód musí obsahovat původní workflow soubor (.github/workflows/python_checker.yml), příklad (složku example) odstraňte
Kód splňuje zadání, pokud automatický běh workflow souboru projde bez chyby, tzn. v části build projdou všechny unit testy pomocí pytest, statická analýza pomocí flake8, vygenerování textové dokumentace pomocí pydoc a vygenerování html dokumentace pomocí pdoc a v části deploy se html vystaví na github pages daného repozitáře.
Nastavení prostředí a odevzdání projektu:
Vytvořte si účet na github.compokud nemáte.
Forkněte project, upravte nastavení, naklonujte si repozitář a nastavte si upstream:
Fork projektu:
    požijte tlačítko Fork na https://github.com/turecekt/vs_project
Nastavení repozitáře v Settings:
V sekci Actions -> General je nutné vybrat permissions Allow all actions and reusable workflows
V sekci Pages je nutné nastavit Build and Deployment Source na Github Actions.
Naklonování vašeho repozitáře do aktuálního adresáře:
    git clone https://github.com/<your-username>/vs_project.git
Přejděte do adresáře s naklonovaným repozitářem:
    cd vs_project
Přiřaďte originální repozitář k vašemu forku:
    git remote add upstream https://github.com/turecekt/vs_project.git
Aktualizace z originálního repozitáře, přijetí změn z upstream:
    git pull upstream master
Commitujte vaše změny po logických oddílech, každý commit s výstižným popisem:
    git commit -m "commit description"
Proveďte push vašich změn na server:
    git push
Otevřete tzv. pull request s názvem a popisem projektu:
    návod: zde
Do moodlu každý řešitel odevzdá pouze odkaz na svůj github:
    url adresu vašeho profilu na githubu
