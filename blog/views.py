from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import BlogPost, BlogCategory, BlogTag, BlogPostTag
from .forms import ContactForm
from user_agents import parse
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404

# def __ua(request):
#     if parse(request.META['HTTP_USER_AGENT']).is_mobile:
#         return 'sp/'
#     else:
#         return ''


class BlogPostFeed(Feed):
    title = "webdirector-blog feed list"
    description_template = "feeds/blogpost.html"

    def items(self):
        return BlogPost.objects.filter(
            status__exact=2
        ).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(BlogPostFeed, self).get_context_data(**kwargs)
        context['foo'] = 'bar'
        return context


class TopView(generic.ListView):

    context_object_name = 'latest_post_list'
    paginate_by = 10

    def get_template_names(self):
        template_name = 'top.html'
        device = ''
        if parse(self.request.META['HTTP_USER_AGENT']).is_mobile:
            device = 'sp/'
        return 'blog/' + device + template_name

    def get_queryset(self):
        """return the last five published questions."""
        queryset = BlogPost.objects.filter(
            status__exact=2
        ).order_by('-created')
        return queryset


class CategoryListView(generic.ListView):

    context_object_name = 'latest_post_list'
    paginate_by = 10

    def get_template_names(self):
        template_name = 'category_search.html'
        device = ''
        if parse(self.request.META['HTTP_USER_AGENT']).is_mobile:
            device = 'sp/'
        return 'blog/' + device + template_name

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['blogcategory'] = BlogCategory.objects.get(
            pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        get_object_or_404(BlogCategory, pk=self.kwargs['category_id'])
        return BlogPost.objects.filter(
            status__exact=2,
            category__exact=self.kwargs['category_id']
        ).order_by('-created')[:10]


class TagListView(generic.ListView):

    context_object_name = 'latest_post_list'
    paginate_by = 10

    def get_template_names(self):
        template_name = 'tag_search.html'
        device = ''
        if parse(self.request.META['HTTP_USER_AGENT']).is_mobile:
            device = 'sp/'
        return 'blog/' + device + template_name

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tagname'] = BlogTag.objects.get(pk=self.kwargs['tag_id'])
        return context

    def get_queryset(self):
        get_object_or_404(BlogTag, pk=self.kwargs['tag_id'])
        return BlogPost.objects.filter(
            status__exact=2,
            blogposttag__tag_id__exact=self.kwargs['tag_id']
        ).order_by('-created')[:10]


class BlogPostView(generic.DetailView):

    model = BlogPost

    def get_template_names(self):
        template_name = 'post_detail.html'
        device = ''
        if parse(self.request.META['HTTP_USER_AGENT']).is_mobile:
            device = 'sp/'
        return 'blog/' + device + template_name

    def get_context_data(self, **kwargs):

        context = super(BlogPostView, self).get_context_data(**kwargs)
        context['blogcategory'] = BlogCategory.objects.get(
            pk=self.kwargs['category_id'])
        return context


class ContactView(FormView):
    form_class = ContactForm

    def get_template_names(self):
        template_name = 'contact.html'
        device = ''
        if parse(self.request.META['HTTP_USER_AGENT']).is_mobile:
            device = 'sp/'
        return device + template_name

    def get_success_url(self):
        template_name = '/contact/finish/'
        device = ''
        if parse(self.request.META['HTTP_USER_AGENT']).is_mobile:
            device = 'sp/'
        return template_name + device

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
