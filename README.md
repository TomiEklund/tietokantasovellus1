Käyttöohje:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>

Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql

Nyt voit käynnistää sovelluksen komennolla

$ flask run

Tämän työn aiheenna on keskustelufoorumisovellus, jossa käyttäjä voi lähettää ja lukea viestejä, nähdä listan omista viesteistään, luoda käyttäjätilin ja hakea viestejä otsikossa tai viestissä olevan sanan perusteella. 

Etusivulla on lista kaikista viesteistä lähetysajan mukaan järjestettynä ja omat viestit -sivulla on lista käyttäjän viesteistä. 

Jos käyttäjällä ei ole viestejä tai käyttäjä ei ole kirjautunut sisään sovellus antaa virheilmoituksen. Virheilmoitus tulee myös, jos käyttäjä yrittää rekisteröityä käyttäjänimellä, joka on varattu tai jos sovellukseen syötetyt viestit, otsikot, käyttäjäntunnukset tai salasanat ovat liian pitkiä tai lyhyitä. 

Ulkoasu hyödyntää Bootstrapin navigointipaneelia ja static-kansiossa sijaitsevaa .css-tidostoa. Viestit tallennetaan messages-tietokantaan ja käyttäjät users-tietokantaan. Moduuli main käynnistää sovelluksen, moduuli db muodostaa yhteyden tietokantaan, moduuli users houlehtii käyttäjien tunnistamisesta, moduulissa messages on viestien lähettämiseen ja viestisivujen muodustumiseen liittyvät funktiot ja moduuli routes huolehtii sovelluksen reitityksistä. 

Salasanat kryptataan werzkeug.security moduulin avulla, tietokannan osoite ja istuntojen käyttämä salainen ovain tallennettu piilotettuun .env tiedostoon ja CSRF-haavoittuvuudet on estetty secrets-moduulin avulla. Sovelluksessa ei ole XSS-haavoittuvuudet ja SQL-injektiot mahdollistavia aukkoja.
