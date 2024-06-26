# Chatbot
A chatbot for a website providing educational courses.

## Features
* BERT model which has Siamese networks inside of its encoders and decoders (SBERT model) is used for sentence embedding.
* When a user inputs a query, the most relevant questions are fetched using the SBERT model.
* If the user isn't satisfied with the result, the answer to the next most relevant question is displayed.
* If none of the results satisfy the user, the user can email to the doubt assistant.
* The doubt support team can also add a new question and its corresponding answer.
* The doubt support team can also download the logs related to the user queries like time taken to answer a specific query and the timestamp at which question was asked, which could then be used by the developers to enhance their NLP model.

## Steps to run the project
* Install Django and ReactJS and follow the steps in README.md of the client folder for React specific instructions.
* Install ElasticSearch and Kibana and run both of them at their default ports.
* Run 'python manage.py makemigrations' followed by 'python manage.py migrate' in order to save the model schema in the database inside of api/chatbot folder. Run 'python manage.py runserver' to start the Django server.

[Video showing site's functionality](https://drive.google.com/file/d/1-am8kWfMT-Y1k7SsRn9greYOSHNAceyr/view?usp=sharing)

## NLP implementation details
* The sentence embeddings of each of the sentences already present in the database are found when the React app is first initialized, so that the embeddings are not recalculated again and again when a user queries.
* The similarity scores between the embeddings are calculated using dot product after normalizing each of the embeddings (since dot product is easier to calculate than cosine of the angle between 2 vectors)