# DLR-2024-2

Öffentliche Materialien für den Fortgeschrittenenkurs 2024 LaTeX am DLR

## Kurstermine

* Dienstag, 2024-08-27
* Donnerstag, 2024-08-29
* Dienstag, 2024-09-03
* Mittwoch, 2024-09-11

An jedem Tag treffen wir uns von 9--11 und 13--15 im virtuellen Kursraum, die Zugangsdaten 
werden per E-Mail versandt.

## "Ground rules"

* "You can say you to me"
* Unterbrecht mich gern (nach ein Satz oder Absatz)
* Bin ich zu schnell? Bitte melden...
* Soll ich etwas wiederholen? Bitte melden...
* Feedback geben: "Seid ihr alle da?" ===> "+"
* 5 Minuten Pause in den einzelnen Blöcken
* Ich weiß nicht alles, aber ich weiß wo ich nachschauen oder wen ich fragen kann


## Wie kommt man an die Materialien?

git installieren und dann auf der Kommandozeile

git clone https://github.com/UweZiegenhagen/DLR-2024-2.git

Updates holt man wie folgt, lokal geänderte Dateien werden dabei überschrieben!

git fetch --all
git reset --hard origin/main

In den nächsten Wochen und Monaten wird das Repository noch öffentlich zugänglich sein, 
irgendwann werde ich es auf privat setzen. Ihr könnt es gern forken, aber dann
bitte in ein privates Repository, da ich gern Wildwuchs verhindern möchte.


## Was wird benötigt

* Ein Rechner (Laptop, Desktop) mit Windows, MacOS oder Linux
* TeX Live 2024 herunterladen und installieren von tug.org/texlive. Eine Anleitung (für TeX Live 2022, es hat sich aber nichts wesentliches geändert) habe ich unter https://www.youtube.com/watch?v=k9KhuZz7k-Q veröffentlicht.
* Wenn ihr unter Linux arbeitet: Bitte nicht aus den Distributionsquellen nehmen, sondern auch von tug.org installieren. Das TeX Live in den Distributionen ist oftmals nicht aktuell oder macht Probleme
* Mac-User installieren bitte MacTeX (auch auf der tug.org Seite frei verfügbar)
* Ein Editor zur Bearbeitung der TeX-Dateien: TeX Live bringt für Mac und Windows TeXworks mit, einen guten und einfach zu bedienenden Editor, den ich persönlich gern benutze. Andere Optionen sind Visual Studio Code (VSC), TeXshop, etc.
* Grundkenntnisse von Git bzw. Github sind nicht verkehrt, da alle meine Dateien im Github liegen.

## Kursinhalte

Die Kursinhalte sind flexibel und orientieren sich am Bedarf und Tempo der 
Teilnehmerinnen und Teilnehmer, mit dem folgenden Ablauf plane ich:


### Themen für die Termine:

  * LaTeX-Probleme lösen, die sich nicht mit zwei Minuten Googeln erledigen lassen, das "Minimalbeispiel"
  * LaTeX-Korrekturfunktionen
  * Akronyme und andere Indizes


### Tag 1

  * Vorstellung der Beteiligten, wer bin ich und wer seid ihr, was sind eure Lernziele?
  * Fehler finden in LaTeX Dokumenten am praktischen Beispiel
    - $ Zeichen in der Fehlermeldung: eventuell fehlt der mathematische Modus
  * Eine eigene Vorlage bauen
  * hyperref (als letztes Paket laden)
  * LaTeX Präsentationen, Step 1
  * Floats im LaTeX
  * chemformula und \ch{CO2}
  * Schneller TeXen mit Tastaturkürzeln (Autohotkey)
  * TikZ - TikZ ist kein Zeichenprogramm Teil 1
  * Große Dokumente


### Tag 2

  * Unbenutzte Pakete finden
  * TeXStudio konfigurieren, dann Alt+Umschalt-F1
    (https://tex.stackexchange.com/questions/313616/configuring-arara-in-texstudio-on-windows)
  * Siunitx zum Einheitensatz
  * Das Booktabs-Paket für schöne Tabellen
  * Briefe und Lebensläufe mit LaTeX
  * Farbige Boxen mit mdframed
  * Mit LaTeX zitieren: thebibliography, bibtex, biblatex/biber
  * \centering versus center Umgebung
    https://tex.stackexchange.com/questions/23650/when-should-we-use-begincenter-instead-of-centering

### Tag 3

  * moderncv komplettes Beispiel
  * Farbige Boxen mit tcolorbox
  * show Labels im Rand, mehr zu Labels und Referenzen
  * Mehr zu KOMA-Script: lebende Kolumnentitel
  * biblatex Namen abkürzen: firstinits=true beim Laden von biblatex
    https://tex.stackexchange.com/questions/21974/biblatex-abbreviated-author-names
  * Schriftarten in pdflatex, Fonts mit Mathe-Support ==> Tug Font Catalogue
  * Lualatex
  * Seiten rotieren lassen
  * OCG mit LaTeX
  * Existierende Dokumente (aus Word) TeXen: Erfahrungen und Tests
  * TikZ - TikZ ist kein Zeichenprogramm Teil 2 (Nodes und Berechnungen)
  * Python-LaTeX-Schnittstellen
  * Poster mit LaTeX gestalten
  * Formatierung von Gleichungen, amsmath
  * Svens Präambel

### Tag 4

  * Floats richtig fließen lassen
  * Typografie
  * Bilder nachträglich beschriften
  * komplexe Tabellen, Multirow und Multicolumn
  * Glossare
  * Kompilierzeiten verringern  
  * Beamer anpassen
  * TikZ Animationen, mehr TikZ
  * nicematrix
  * varsfromjobname
  * Was sonst noch so geht mit LaTeX: Leaflets, Labels, Pocketmods, ...
  * HID Remapper: https://github.com/jfedor2/hid-remapper :-)
  * Fragestunde

## Literaturempfehlungen

Empfohlen werden:

* Alle Bücher von Herbert Voß (https://www.lehmanns.de/search/quick?PHPSESSID=mi28bh61dhv2nu8keg4hjnkunumgi5ah&mediatype_id=&q=herbert+vo%C3%9F), insbesondere die Einführung
* Der LaTeX Companion in der 3. Auflage, wenn man mehr wissen möchte

