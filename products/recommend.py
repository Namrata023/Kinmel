from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from .models import Product

def get_similar_products(product_id):

    products = Product.objects.all().select_related('category')
    data = []

    for p in products:
        data.append({
            'id': p.id,
            'name': p.name or '',
            'description': p.description or '',
            'tags': getattr(p, 'tags', '') or '',
            'category': p.category.name if p.category else ''
        })

    df = pd.DataFrame(data)

    df['combined'] = (
        df['name'].fillna('') + ' ' +
        df['description'].fillna('') + ' ' +
        df['tags'].fillna('') + ' ' +
        df['category'].fillna('')
    )

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    idx = df[df['id'] == product_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended_ids = [df.iloc[i[0]]['id'] for i in sim_scores]

    return Product.objects.filter(id__in=recommended_ids)