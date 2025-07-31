# titanic-survival-prediction
A machine learning model that predicts passenger survival on the Titanic dataset based on demographic and travel information

Запустим сервис titanic-service:

"""
docker build -t titanic-service .

docker run -d --name titanic-service -p 500:5000 titanic-service
"""
