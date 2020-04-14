from haystack import indexes
from user.models import expertdetails
from haystack import query


class expertdetailsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return expertdetails

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


