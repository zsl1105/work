from haystack import indexes
from user.models import Startup
from haystack import query


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Startup

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
