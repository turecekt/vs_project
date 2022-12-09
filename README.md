# Závěrečný projekt z předmětu AP1VS
Tento repozitář slouží jako podklad a vzor pro závěrečný projekt z předmětu AP1VS.

## Požadavky na projekt
* Projekt bude řešen formou forku a odevzdán pomocí pull requestu na githubu
* Projekt může zpracovávat tým o 2-5 studentech:
    * hlavní řešitel vytvoří fork a pozve do něj ostatní spoluřešitele
    * každý z řešitelů musí mít v projektu zařazeny commity
    * nakonec hlavní řešitel odevzdá projekt pomocí pull requestu
* Projekt musí být napsán v programovacím jazyce Python 3
* Témata projektu jsou popsána v pdf dokumentu v systému Moodle
* Kód musí být okomentovaný (ideálně všechny entity)
* Kód musí obsahovat unit testy (pokrytí kódu testy by se mělo blížit 100%)
* Zdrojový kód musí projít kontrolním testem na githubu v sekci Actions (je nutné povolit). Tzn. musí projít všechny unit testy a kontola pomocí flake8 a flake8-docstrings
* Zároveň dojde k automatickému vygenerování dokumentace s docstringů pomocí knihovny pdoc.


## Postup
1. Vytvořte si účet na github.com pokud nemáte (všichni členové týmu).
2. Nastavte si přístup na GitHub z vašeho počítače, použijte a credential helper jako je [Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager/blob/main/README.md) nebo si vygenerujte osobní přístupový token: [a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Případně můžete commity provádět přes web GitHubu (což je ale hodně neprogramátorská varianta :wink:).
2. Jeden z řešitelů udělá Fork projektu a upraví nastavení (Settings nahoře v liště ) projektu, ostatní členové projektu se budou účastnit jako přispěvatelé (Contributors) do projektu hlavního řešitele.
    1. Fork projektu:
        * Použijte tlačítko Fork na https://github.com/tureckova/AP1VS-final-project
    2. Nastavení repozitáře v Settings:
        * V sekci Actions -> General je nutné vybrat permissions Allow all actions and reusable workflows
        * V sekci Pages je nutné nastavit Build and Deployment Source na Github Actions.
        
3. Naklonujte si svůj repozitář a nastavte si upstream (toto provedou všichni uživatelé, neboť každý uživatel musí provést alespoň jeden commit):

    Naklonování vašeho repozitáře do aktuálního adresáře:
    
        git clone https://github.com/your_username/AP1VS-final-project.git
        
    Přejděte do adresáře s naklonovaným repozitářem:
    
        cd vs_project
        
    Přiřaďte originální repozitář k vašemu forku:
    
        git remote add upstream https://github.com/tureckova/AP1VS-final-project

3. Aktualizace z originálního repozitáře, přijetí změn z upstream:

        git pull upstream master
    
4. Commitujte vaše změny po logických oddílech, každý commit s výstižným popisem:

        git commit -m "logical commit description"
    
5. Proveďte push vašich změn na server:

        git push
    
6. Otevřete tzv. pull request s názvem a popisem projektu, návod jak na to [zde](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
    
7. Do moodlu každý řešitel odevzdá pouze odkaz na github stránku vašeho projektu - url adresu forku vašeho projektu - a url adresu svého účtu na GitHub.
