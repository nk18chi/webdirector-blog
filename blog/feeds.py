from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import BlogPost


class LatestEntriesFeed(Feed):
    title = "webディレクターブログ"
    link = "http://127.0.0.1"
    # description = "Updates on changes and additions to police beat central."

    def items(self):
        return BlogPost.objects.filter(
            status__exact=2
        ).order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog:post_detail', kwargs={'category_id': item.category_id, 'pk': item.id})