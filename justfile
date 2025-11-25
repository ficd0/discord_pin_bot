# updates the instance running on server
update:
    ssh server "env -C /home/fedora/pebble git pull origin prod --force --rebase && \
                systemctl --user restart pebble"

# runs pebble
run:
    uv run src/main.py
