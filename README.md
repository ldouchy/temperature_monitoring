# temperature_monitoring

# PostgreSQL & Grafana set up

/!\ Default password as per created via docker official images /!\

## Start the database
```bash
docker run -d \
  --rm \
  --name postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v /home/pi/pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres
```

## install client
```bash
sudo apt-get install postgresql-client
```

## Set up the database
```bash
export PGPASSWORD='mysecretpassword' ; psql -h 127.0.0.1 -p 5432 -U postgres

CREATE DATABASE homesweethome;

\c homesweethome

CREATE TABLE box_experiment_01 (date timestamp unique, probe_t1 real, probe_t2 real);
```

## Start grafana mounting the required folders and show the logs
```bash
export ROOTPATH="/home/pi/temperature_monitoring" && \
sudo docker run -d \
  --rm \
  -p 3000:3000 \
  --name=grafana \
  -v ${ROOTPATH}/provisioning:/etc/grafana/provisioning \
  -v ${ROOTPATH}/dashboards:/var/lib/grafana/dashboards \
  grafana/grafana && \
sudo docker logs grafana --follow
```

## To kill the grafana container
```bash
sudo docker kill grafana
```

# Temperature script

## Quick and dirty loop
```bash
tmux
watch -n 15 "./temperature/temp_66_67.py"
```