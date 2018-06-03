from django import template
from blog.models import BlogCategory, BlogPost, BlogTag
import re

register = template.Library()


@register.inclusion_tag('blog/includes/categorymenu.html')
def get_blogcategory():
    categorie = BlogCategory.objects.order_by('order')[:5]
    return {'categorie': categorie}


@register.inclusion_tag('blog/includes/latestbloglist.html')
def get_latestbloglist():
    blogpost = BlogPost.objects.filter(
            status__exact=2
        ).order_by('-created')[:5]
    return {'blogpost': blogpost}


@register.inclusion_tag('blog/includes/taglist.html')
def get_taglist():
    blogtag = BlogTag.objects.filter()[:20]
    return {'blogtag': blogtag}


@register.filter()
def custom_html(value):
    # add_section
    text = re.sub(r'\s', '', value)
    text = re.sub('<h2>', '</section><section><h2>', text) + '</section>'
    text = re.sub(r'^</section>', '', text)
    text = re.sub('<h3>(.*?)</section>', r'<h3>\1</section></section>', text)
    text = re.sub('<h3>', r'</section><section><h3>', text)
    text = re.sub(r'^(.*?)</section><section><h3>', r'\1<section><h3>', text)
    text = re.sub('ahref="http', 'a href="http', text)
    text = re.sub(r'<imgsrc="(.*?)"alt=', r'<img src="/static/blog/img/contents/\1" alt=', text)

    # 最初のh1にclassを付与する
    text = re.sub(r'^(.*?)<h2>', r'\1<h2 class="init-h2">', text)

    return text

@register.filter()
def limit_text(str, int):
    return str[:int]+'...'


@register.filter()
def date_format(value):
    return value.strftime('%Y年%m月%d日')


@register.filter()
def add_int(value, int):
    return value + int


@register.filter()
def sub_int(value, int):
    return value - int


@register.filter()
def specify_range(value, int):
    return range(value-int, value+int+1)


@register.simple_tag()
def debug_object_dump(var):
    return vars(var)