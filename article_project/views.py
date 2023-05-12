from django.http import HttpResponse

from articles.models import Article

def home_view(request):
    name = "Justin"
    article_obj = Article.objects.get(id=2)
    HTML_STRING = f"""
    <h1>{article_obj.title} - Title<br>
    {article_obj.content} - content</h1>
    """
    return HttpResponse(HTML_STRING)