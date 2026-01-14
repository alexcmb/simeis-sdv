#!/bin/bash

# Recherche tous les TODO dans les fichiers .rs, .py, .js, .
errors=0
grep -r "// TODO" . --include \*.{rs,py,js,ts} | while read -r line ; do
    if ! echo "$line" | grep -qE "#[0-9]+"; then
        echo "TODO sans issue: $line"
        errors=$((errors+1))
    fi
done

if [ "$errors" -ne 0 ]; then
    echo "$errors TODO sans issue trouvés"
    exit 1
else
    echo "Tous les TODO ont un #issue associé."
fi
