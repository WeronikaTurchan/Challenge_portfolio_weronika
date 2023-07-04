## Zadanie 1: konfiguracja oprogramowania 
### Podzadanie 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge? 
Cześć, jestem Weronika :) Od dłuższego czasu szukam swojej ścieżki zawodowej, próbowałam nowych rzeczy, rozmawiałam z wieloma ludźmi na temat ich kariery i sama nie wiedziałam, w która stronę chciałabym iść.
 
Po zgłębieniu tematów związanych z szeroko pojętym IT zdecydowałam, że chciałabym spróbować swoim sił w testowaniu oraz Pythonie. 

Moja koleżanka poleciła mi projekty od DareIT, ponieważ sama kiedyś brała udział w wyzwaniu i była bardzo zadowolona. Więc nie mogłam nie spróbować :)

Moim celem jest zdobycie nowych umiejętności i wiedzy z zakresu testowania automatycznego i Pythona. Myślę, że dzięki wsparciu grupy i doświadczonych mentorów uda się to bez problemu :)  

###### Wynik testu PURPUROWEGO 
5 z 14 pytań

## Zadanie 2: Wyszukiwanie selektorów na stronie https://scouts-test.futbolkolektyw.pl/en/login?redirected=true

### Login:
//*[@id="login"]

//input[@id="login"]

//*[contains(@class, 'MuiInputBase-input MuiInput-input')]

### Hasło:
//*[@id="password"]

//input[@type="password"]

//*[contains(@id, 'password')]

### Przypomnij hasło: 
//*[@id="__next"]/form/div/div[1]/a

//a

//*[contains(@class, 'MuiTypography-root MuiLink-root MuiLink-underlineHover jss4 MuiTypography-colorPrimary')]

### Język:
//*[@id="__next"]/form/div/div[2]/div/div

//div[@role="button"]

//*[contains(@aria-haspopup, 'listbox')]

### Przycisk zaloguj: 
//*[@id="__next"]/form/div/div[2]/button/span[1]

//span

//div/button/span

