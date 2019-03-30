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

#
# @register.filter()
# def trans_word(value):
#     # text = re.sub(r'  |<br>', '@br@', value)
#     text = re.sub(r'```([\s\S]*?)```', r'@code_m@\1@code_m_e@', value)
#     text = re.sub(r'`(.*?)`', r'@code_s@\1@code_s_e@', text)
#     text = re.sub(r'<blockquote', r'@blockquote@', text)
#     text = re.sub(r'</blockquote>', r'@e_blockquote@', text)
#     text = re.sub(r'<p', r'@p@', text)
#     text = re.sub(r'</p>', r'@e_p@', text)
#     text = re.sub(r'<a href="(.*)">', r'@href \1@', text)
#     text = re.sub(r'</a>', r'@e_href@', text)
#     text = re.sub(r'<script', '@script@', text)
#     text = re.sub(r'</script>', '@e_script@', text)
#     return text
#
# @register.filter()
# def convert_word(value):
#     text = re.sub(r'@code_m@(.*?)@code_m_e@', r'<pre class="prettyprint"><code>\1</code></pre>', value)
#     text = re.sub(r'@code_s@(.*?)@code_s_e@', r'<code class="code-simple">\1</code>', text)
#     text = re.sub('@br@', '<br>', text)
#     text = re.sub('@blockquote@', '<blockquote', text)
#     text = re.sub('@e_blockquote@', '</blockquote>', text)
#     text = re.sub('@p@', '<p ', text)
#     text = re.sub('@e_p@', '</p> ', text)
#     text = re.sub('@href (.*?)@', r'<a href="\1">', text)
#     text = re.sub('@e_href@', '</a> ', text)
#     text = re.sub('@script@', '<script', text)
#     text = re.sub('@e_script@', '</script><p>', text)
#     text = re.sub(r'\[@youtube: (.*)\]', r'<div class="blog_in_iframe"><iframe src="\1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>', text)
#     return text


@register.filter()
def custom_html(text):
    # sectionをつける
    text = re.sub('<h2(.*?)>', r'</section><section><h2\1>', text) + '</section>'
    text = re.sub(r'^</section>', '', text)
    text = re.sub('<h3(.*?)>(.*?)</section>', r'<h3\1>\2</section></section>', text)
    text = re.sub('<h3(.*?)>', r'</section><section><h3\1>', text)
    text = re.sub(r'^(.*?)</section><section><h3(.*?)>', r'\1<section><h3\1>', text)

    #リンクをターゲットブランクにする、ただしindexはターゲットブランクにしない
    text = re.sub('a href="http', 'a target="blank" href="http', text)

    # 画像の保存先を指定する
    text = re.sub(r'<img(.*?)src="(?!http)(.*?)"', r'<img\1src="/media/\2"', text)
    text = re.sub(r'<img(.*?)src=(.*?)>', r'<div class="article-image-container"><img\1src=\2></div>', text)

    # code-prettifyを使うためにpreにclassをつける
    text = re.sub(r'<code>', r'<code class="code-simple">', text)
    text = re.sub(r'<pre><code class="code-simple">', r'<pre class="prettyprint"><code>', text)

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
