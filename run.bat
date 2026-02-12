@echo off
echo Starting BlackBrain Backend...
cd backend
start cmd /k uvicorn main:app --reload

echo Starting BlackBrain Frontend...
cd ../frontend
start cmd /k npm start

echo BlackBrain App is starting...
pause