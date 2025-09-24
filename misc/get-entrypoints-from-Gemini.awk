#!/usr/bin/awk -f

BEGIN {
    target_section = "project.scripts"
    in_section = 0
}

{
    # Zeile bereinigen: führende/nachfolgende Leerzeichen entfernen und vor dem Kommentar abschneiden
    line = $0
    sub(/^[ \t]+/, "", line)
    sub(/[ \t]+$/, "", line)
    sub(/[ \t]*[#;].*$/, "", line)

    # Wenn die Zeile leer ist, überspringen
    if (line == "") {
        next
    }

    # Überprüfen, ob es sich um einen Abschnitts-Header handelt
    if (line ~ /^\[.*\]$/) {
        section = substr(line, 2, length(line) - 2)
        if (section == target_section) {
            in_section = 1
        } else {
            in_section = 0
        }
        next
    }

    # Verarbeiten von Schlüssel-Wert-Paaren im Zielabschnitt
    if (in_section == 1) {
        if (line ~ /^[a-zA-Z0-9_-]+[ \t]*=[ \t]*.*$/) {
            # Schlüssel extrahieren und ausgeben
            split(line, a, /[ \t]*=[ \t]*/)
            print a[1]
        }
    }
}
