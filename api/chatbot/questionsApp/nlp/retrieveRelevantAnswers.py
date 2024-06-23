from elasticsearch8 import Elasticsearch
from sentence_transformers import SentenceTransformer
import numpy as np
from ..models import Question
from django.forms.models import model_to_dict

mapping = {
    'question_id': {
        'type': 'long',
    },
    'question': {
        'type': 'text',
    },
    'answer': {
        'type': 'text',
    },
    'questionEmbedding': {
        'type': 'dense_vector',
        'dims': 768,
        'index': True,
        'similarity': 'dot_product',
    },
}

EMBEDDING_DIMS = 768

ES_INDEX_NAME = "faq_bot_index"     # elasticSearch index name

def initializeEmbeddings():
    global sentence_transformer
    global es

    sentence_transformer = SentenceTransformer('all-mpnet-base-v2')
    
    es = Elasticsearch(
        "https://localhost:9200/",
        basic_auth=('elastic', 'f05Ef+pozNw=ZFRvF=b1'),
        ca_certs='C:/Users/Vaalarivan/Downloads/elasticsearch-8.14.1-windows-x86_64/elasticsearch-8.14.1/config/certs/http_ca.crt',
    )

    es.indices.create(index=ES_INDEX_NAME, mappings=mapping, ignore=400)

    qa_pairs = Question.objects.all()
    
    for qa in qa_pairs:
        qa = model_to_dict(qa)
        qa['question_embedding']=sentence_transformer.encode(qa['question'])
        embedding_norm = np.linalg.norm(qa['question_embedding'])
        qa['question_embedding'] /= embedding_norm
        try:
            es.index(index=ES_INDEX_NAME, document=qa, id=qa['question_id'])
        except Exception as e:
            print(e)

def retrieveRelevantAnswers(question):
    global sentence_transformer
    global es

    input_question_embedding = sentence_transformer.encode(question)
    input_question_embedding_norm = np.linalg.norm(input_question_embedding)
    input_question_embedding /= input_question_embedding_norm

    query = {
        'field': 'question_embedding',
        'query_vector': input_question_embedding,
        'k': 2,
        'num_candidates': 500,
    }

    res = es.knn_search(index=ES_INDEX_NAME, knn=query, source=['question', 'answer'])

    relevantAnswers = [ res['hits']['hits'][i]['_source']['answer'] for i in range(len(res['hits']['hits']))]

    return relevantAnswers