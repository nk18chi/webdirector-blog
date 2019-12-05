from django.http import Http404
from django.utils import translation
from django.urls import reverse, resolve
from django import template
from blog.models import BlogCategory, BlogPost, BlogTag
from user_agents import parse
import re

register = template.Library()


@register.inclusion_tag('blog/components/categorymenu.html')
def get_blogcategory():
    categorie = BlogCategory.objects.order_by('order')[:5]
    return {'categorie': categorie}


@register.inclusion_tag('blog/components/latestbloglist.html')
def get_latestbloglist():
    blogpost = BlogPost.objects.filter(
        status__exact=1
    ).order_by('-created_at')[:5]
    return {'blogpost': blogpost}


@register.inclusion_tag('blog/components/taglist.html')
def get_taglist():
    blogtag = BlogTag.objects.filter()[:20]
    return {'blogtag': blogtag}


@register.filter()
def custom_html(text):
    # sectionをつける
    text = re.sub('<h2(.*?)>', r'</section><section><h2\1>',
                  text) + '</section>'
    text = re.sub(r'^</section>', '', text)
    text = re.sub('<h3(.*?)>(.*?)</section>',
                  r'<h3\1>\2</section></section>', text)
    text = re.sub('<h3(.*?)>', r'</section><section><h3\1>', text)
    text = re.sub(r'^(.*?)</section><section><h3(.*?)>',
                  r'\1<section><h3\1>', text)

    # リンクをターゲットブランクにする、ただしindexはターゲットブランクにしない
    text = re.sub('a href="http', 'a target="blank" href="http', text)

    # 画像の保存先を指定する
    text = re.sub(r'<img(.*?)src="(?!http)(.*?)"',
                  r'<img\1src="/media/\2"', text)
    text = re.sub(
        r'<img(.*?)src=(.*?)>',
        r'<div class="article-image-container"><img\1src=\2></div>',
        text)

    # code-prettifyを使うためにpreにclassをつける
    text = re.sub(r'<code>', r'<code class="code-simple">', text)
    text = re.sub(r'<pre><code class="code-simple">',
                  r'<pre class="prettyprint"><code>', text)

    return text


@register.filter()
def limit_text(str, num):
    return str[:num] + '...'


@register.filter()
def date_format(value):
    return value.strftime('%Y-%m-%d')


@register.filter()
def add_int(value, int):
    return value + int


@register.filter()
def sub_int(value, int):
    return value - int


@register.filter()
def specify_range(value, int):
    return range(value - int, value + int + 1)


@register.simple_tag()
def debug_object_dump(var):
    return vars(var)


# https://stackoverflow.com/questions/11437454/django-templates-get-current-url-in-another-language
# https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers
# https://docs.djangoproject.com/en/2.2/topics/http/urls/


class TranslatedURL(template.Node):
    def __init__(self, language):
        self.language = language

    def render(self, context):
        view = resolve(context['request'].path)
        request_language = translation.get_language()
        translation.activate(self.language)
        pattern_name = view.app_names[0] + ":" + \
            view.url_name if view.app_names else view.url_name
        url = reverse(pattern_name, args=view.args, kwargs=view.kwargs)
        translation.activate(request_language)
        return url


@register.tag(name='translate_url')
def do_translate_url(parser, token):
    language = token.split_contents()[1]
    return TranslatedURL(language)
