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