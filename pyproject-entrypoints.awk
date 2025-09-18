
BEGIN {
    target_section = "project.scripts"
    in_section = 0
}

{
    # Cleaning row: removing leading and trailing whitespaces and cut before comment character
    line = $0
    sub(/^[ \t]+/, "", line)
    sub(/[ \t]+$/, "", line)
    sub(/[ \t]*[#;].*$/, "", line)

    # Skip on empty row
    if (line == "") {
        next
    }

    # Check for section header
    if (line ~ /^\[.*\]$/) {
        section = substr(line, 2, length(line) - 2)
        if (section == target_section) {
            in_section = 1
        } else {
            in_section = 0
        }
        next
    }

    # Perform key-value-pair in target section
    if (in_section == 1) {
        if (line ~ /^[a-zA-Z0-9_-]+[ \t]*=[ \t]*.*$/) {
            # extract and print key
            split(line, a, /[ \t]*=[ \t]*/)
            print a[1]
        }
    }
}


# vim: ts=4 et list
