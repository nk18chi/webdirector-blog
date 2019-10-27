from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import BlogPost, BlogCategory, BlogTag
from .forms import ContactForm
from user_agents import parse
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.conf import settings

import urllib.parse as urlparse
from urllib.parse import urlencode


def get_alax_next_blogpost_url(arg=None):
    api_url_bloppost = settings.BASE_URL + settings.API_URL + 'blogposts/'
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']

    # creat url to access for DRF
    url_parts = list(urlparse.urlparse(api_url_bloppost))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    param = {'limit': page_size, 'offset': page_size}
    if arg:
        param.update(arg)

    query.update(param)
    url_parts[4] = urlencode(query)

    return urlparse.urlunparse(url_parts)


class BlogPostFeed(Feed):
    title = "webdirector-blog feed list"
    description_template = "feeds/blogpost.html"

    def items(self):
        return BlogPost.objects.filter(
            status__exact=1
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(BlogPostFeed, self).get_context_data(**kwargs)
        context['foo'] = 'bar'
        return context


class TopView(generic.ListView):

    context_object_name = 'latest_post_list'
    paginate_by = settings.REST_FRAMEWORK['PAGE_SIZE']
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        context['ajax_url'] = get_alax_next_blogpost_url()
        return context

    def get_queryset(self):
        """return the last five published questions."""
        queryset = BlogPost.objects.populate(True).filter(
            status__exact=1
        ).order_by('-created_at')
        return queryset


class CategoryListView(generic.ListView):

    context_object_name = 'latest_post_list'
    paginate_by = settings.REST_FRAMEWORK['PAGE_SIZE']
    template_name = 'blog/category_search.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['blogcategory'] = BlogCategory.objects.get(
            pk=self.kwargs['category_id'])
        context['ajax_url'] = get_alax_next_blogpost_url(
            {'category': self.kwargs['category_id']})

        return context

    def get_queryset(self):
        get_object_or_404(BlogCategory, pk=self.kwargs['category_id'])
        return BlogPost.objects.filter(
            status__exact=1,
            category__exact=self.kwargs['category_id']
        ).order_by('-created_at')


class TagListView(generic.ListView):

    context_object_name = 'latest_post_list'
    paginate_by = settings.REST_FRAMEWORK['PAGE_SIZE']
    template_name = 'blog/tag_search.html'

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tagname'] = BlogTag.objects.get(pk=self.kwargs['tag_id'])
        context['ajax_url'] = get_alax_next_blogpost_url(
            {'tag': self.kwargs['tag_id']})
        return context

    def get_queryset(self):
        get_object_or_404(BlogTag, pk=self.kwargs['tag_id'])
        return BlogPost.objects.filter(
            status__exact=1,
            blog_tag__exact=self.kwargs['tag_id']
        ).order_by('-created_at')


class BlogPostView(generic.DetailView):

    model = BlogPost
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):

        context = super(BlogPostView, self).get_context_data(**kwargs)
        context['blogcategory'] = BlogCategory.objects.get(
            pk=self.kwargs['category_id'])
        return context


class ContactView(FormView):

    form_class = ContactForm
    template_name = "static/contact.html"

    def post(self, request, *args, **kwargs):
        form = ContactMailForm(data=request.POST)

        if form.is_valid():
            messages.info(self.request, 'お問い合わせ内容を送信しました。')
            form.send_email()

            return redirect(request.META['HTTP_REFERER'])

        else:
            return self.form_invalid(form)
