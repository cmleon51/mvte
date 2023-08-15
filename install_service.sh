#!/bin/bash

set -e

program="./main.py"
destination="$HOME/.local/bin/mvte.py"
systemd_user="$HOME/.config/systemd/user"
service="./mvte.service"

if [ ! -e "$destination" ]; then
    cp "$program" "$destination"
fi

if [ ! -d "$systemd_user" ]; then
    mkdir -p "$systemd_user"
fi

cp "$service" "$systemd_user"

echo "service installed. To enable/start it:
    1)systemctl --user daemon-reload
    2)systemctl --user start/enable mvte.service"
