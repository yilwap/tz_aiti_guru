#!/bin/sh
set -e


if [ ! -f .env ]; then
    echo ".env not found"
    cp .env.example .env

    echo ".env created"
    echo "Edit it or press Any key"
    read -r _
fi

docker compose up -d

until docker exec postgres_db pg_isready -U postgres >/dev/null 2>&1; do
    sleep 1
done


docker exec -i postgres_db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" < ./sql/init.sql
