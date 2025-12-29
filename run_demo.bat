@echo off
cd /d %~dp0

REM ---- Create / activate virtual environment ----
call create_env.bat

REM ---- Run docker containers ----
cd app

echo Stopping containers and removing volumes...
docker-compose down -v

echo Pruning unused volumes...
docker volume prune -f

echo Starting containers in background...
docker-compose up -d --build

REM ---- Wait for Kafka to be ready ----
echo Waiting for Kafka to start...
timeout /t 15 /nobreak > nul

REM ---- Consumers ----

start "Item Consumer" cmd /k python -m demo.itemConsumerDemo
start "Order Consumer" cmd /k python -m demo.orderConsumerDemo
start "Payment Consumer" cmd /k python -m demo.paymentInfoConsumerDemo
cd ..
