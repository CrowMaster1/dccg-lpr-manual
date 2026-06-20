---
title: Dataindsamling
nav_order: 2
layout: default
---

# Dataindsamling

DCCG's database dannes af kodning via indberetninger til LPR samt PATOBANK.

Det kliniske personale anvender kodning i forbindelse med behandling af patienten, der opsamles og struktureres. Databasens population dannes ud fra registreringer i LPR og suppleres med oplysninger fra Patobank

## Population

Databasens patientpopulation er afgrænset ved følgende:

Patienter med førstegangstilfælde og recidiv af cancer i kolon eller rektum, givet ved ICD-10 diagnosekoderne, C180-189 og C209.

Patienter der er 18 år eller ældre på diagnosetidspunktet.

Patienter der har bopæl i Danmark og gyldigt dansk cpr-nummer.

Der er registreret et forløb på en kirurgisk afdeling, eller patienten er behandlet af en kirurgisk afdeling under indlæggelse på anden afdeling på et offentligt sygehus.

Patienter opdeles baseret på histologisk subtype, eller manglende histologi.

Patienter med følgende histologiske subtyper opgøres samlet

Histologiske tumortyper:

- Adenokarcinom
- Lavt differentieret adenokarcinom
- Mucinøst adenokarcinom
- Signetringscelle karcinom
- Udifferentieret karcinom
- Medullært karcinom

Patienter der er klinisk diagnosticeret uden histologisk verifikation, eller har anden histologi end ovenfor opgøres i simplificeret form.

Patienter med kræft i blindtarm (DC18.1) opgøres separat i simplificeret form. Der er ikke krav om indberetning af basisinformationer eller andre variabler til DCCG-databasen for patienter med kræft i blindtarmen. Der er heller ikke krav til DCCG-patologi beskrivelse for disse.

### Eksklusionskriterier

For patienter, hvor DC18.0-9 eller 20.9 er angivet i LPR med kræftpakkeforløbskoden, AFB12X1 (kræft i tyk- og endetarm: pakkeforløb slut, diagnose afkræftet), eller diagnosetillægskoden, ZDW73 (diagnosen senere afkræftet), ekskluderes. -- Se afsnit senere omkring fjernelse af patienter fra LPR.

## Behandling uden primær tumor

Patienter med ukendt primær cancer, hvor MDT beslutter at behandle som kolorektalcancer, indgår ikke i databasen, og skal ikke kodes med DC18.0 -> 18.9 eller 20.9. Disse kodes med diagnosekoden DC80.9 (kræft uden kendt primær). 

## Patientforløbsregistrering/Data punkter

DCCG's database opsamler viden omkring hele patientens forløb. Der defineres datapunkter -- primært omkring diagnosetidspunktet, ved resektioner/endoskopiske procedure, onkologisk behandling samt kontrol da disse har kvalitetsmæssig fokus. Nedenstående figur viser forskellige forløb som en kolorektalcancerpatient kan have samt de datapunkter hvor DCCG opsamler data.

![](/assets/images/patientforloeb.png)

## Mangellister & Data-mangellister

### Mangellister

Der dannes kun mangellister genereret fra patienter, der findes i patobank med kolorektal patologi, hvor der ikke er indberettet cancerdiagnose i LPR

### Data mangellister

For at sikre høj dækningsgrad af databasen produceres data-mangellister. Disse datamangel lister gøres tilgængelige for den indrapporterende afdeling. På sigt oprettes som supplerende indikatorer, således at det er muligt at få hurtig tilbagemelding på ikke komplette data.

Listerne baseres på om patienten i forbindelse med en DCCG-procedure har fået tilknyttet en behandlingsintentionskode/proceduresigte. Såfremt behandlingsintention er tilknyttet, tolkes resterende ikke-registrerede felter, hvor "ukendt" ikke er en mulighed, som verificeret ukendt. Ved manglende behandlingsintention tolkes samtlige ikke-registrerede variabler som "ikke udfyldt".

## Registrering ved multiple værdier

Hvis der i LPR optræder flere værdier af en variabel, vil databasen som udgangspunkt opfatte den værdi, der ligger tættest på proceduren, som den behandlingsbestemmende og inkludere denne. Data vil forsat være tilgængelige via LPR såfremt, man senere vil anvende disse til at beskrive detaljer i et patientforløb.

## Fjernelse af patienter fra databasen -- fejlagtig indberetning i LPR

### Vestdanmark (Systematic EPJ)
Der vælges diagnosen i diagnosebilledet, der vælges herefter kontekst menu (Højre klik) og der vælges "Senere afkræftet"

### Østdanmark (Sundhedsplatformen)
Der tilknyttes ”`ZDW73" til diagnosen I diagnoseoverblikket.

## Synkrone og Metakrone cancer

Databasen understøtter synkrone og metakrone cancere.

Synkrone cancere registres som beskrevet under basisinformationer.

Med synkrone menes en tumor der behandles på samme sygdomsforløb, og hvor behandlingsstrategien er samlet for disse.

For metakrone cancere oprettes nyt sygdomsforløb og canceren behandles som "ny" med fuld registrering.

Ved ny tumor i samme segment, som f.eks. segment hvor der tidligere er foretaget polypektomi, besluttes lokalt om det drejer sig om recidiv (samme forløb + recidiv kode) eller ny cancer (nyt forløb).

Se sektion omkring recidiv for registrering. 

## Helbredsforløb 

Alle behandlinger tilknyttes patientens helbredsforløb. Disse består af alle kontakter under cancerdiagnosekoden på samtlige afdelinger. Forløbet er ikke tilknyttet en enkelt afdeling men den samlede diagnose. Når patienten ophører med behandling og/eller kontrol er det vigtigt at dette forløb afsluttes. Databasen vil herefter opfatte nye forløb som en ny cancer, såfremt det ikke fremgår af kodning at der er tale om recidiv (se senere).

Patienter der ikke modtager behandling eller ikke følges, med kontroller bør have deres forløb afsluttet. Patienter med åbne forløb uden evt. Kontrol skanninger vil fremgå som manglende hvis forløb ikke er afsluttet. Hvis forløb er afsluttet vil evt. Kontrol skanninger foretaget på andet forløb ikke opfattes som relateret til patientens kolorektalcancerforløb.

## Dataansvar

Ansvaret for udfyldelse af basisinformationer påhviler den udredende afdeling. For patienter, der ikke har fået foretaget regelret udredning, tildeles ansvaret patientens lokale kolorektal-kirurgiske afdeling.