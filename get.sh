#!/bin/bash

# Colors for printing
Yellow='\033[1;33m'
NC='\033[0m' # No Color
Green='\033[0;32m'
RED='\033[0;31m'

# Gets the data from the heroku app
printf "${Yellow}...Requesting Heroku...${NC}\n"
function heroku_app() {
    heroku pg:backups:capture
    rm latest.dump
    heroku pg:backups:download

    pg_ctl status
    if [ $? -eq 3 ]; then
        pg_ctl start
        if [ $? -ne 0 ]; then
            printf "${RED}PG not started${NC}\n"
            exit 1
        fi
    fi

    # Restore the database locally
    PGPASSWORD='admin' pg_restore --clean --no-acl --no-owner -h localhost -U postgres -d postgres latest.dump
}

(cd ../umllabels/ && heroku_app)

# Turn into CSV locally
printf "${Yellow}...Requesting local postgres${NC}\n"

PGPASSWORD='admin' psql -U postgres -f exportdatabase.sql

if [ $? -eq 0 ]; then
    printf "${Green}Success${NC}\n"
else
    printf "${RED}FAILURE${NC}\n"
fi

pg_ctl stop
