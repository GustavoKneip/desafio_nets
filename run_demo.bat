@echo off
cd /d %~dp0

REM ---- Create / activate virtual environment ----
call create_env.bat

REM ---- Run docker containers ----
cd app
start "Docker Compose" cmd /k ^
docker-compose down -v ^&^& ^
docker-compose up --build

REM ---- Consumers ----

start "Item Consumer" cmd /k python -m demo.itemConsumerDemo
start "Order Consumer" cmd /k python -m demo.orderConsumerDemo
start "Payment Consumer" cmd /k python -m demo.paymentInfoConsumerDemo
cd ..
