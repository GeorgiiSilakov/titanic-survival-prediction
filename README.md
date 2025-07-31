# titanic-survival-prediction
A machine learning model that predicts passenger survival on the Titanic dataset based on demographic and travel information

Запустим сервис titanic-service:

"""
docker build -t titanic-service . # создание образа

docker run -d --name titanic-service -p 500:5000 titanic-service # Запуск контейнера
"""
