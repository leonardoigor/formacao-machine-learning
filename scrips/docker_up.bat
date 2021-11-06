@echo off

cmd /k docker compose -f ../docker-compose.yml -p python up -d --renew-anon-volumes


exit