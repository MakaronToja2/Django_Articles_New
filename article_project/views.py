from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article
import random

def home_view(request):
    last_article = Article.objects.last()
    random_article_id = random.randrange(1,last_article.id+1)
    article_obj = Article.objects.get(id=random_article_id)
    content  = {
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id,

    }
    HTML_STRING = render_to_string("home.html", context=content)
    return HttpResponse(HTML_STRING)