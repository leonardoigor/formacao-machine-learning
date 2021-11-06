@echo off

 
cmd /k docker compose -f docker-compose.yml -p python down --volumes --rmi all

exit