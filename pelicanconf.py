#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys

import os


sys.path.append(os.curdir)

from collections import OrderedDict

AUTHOR = u'ItInDublinBR'
SITENAME = u'IT In Dublin - BR'
SITEURL = ''
API_SERVICE = 'https://itindublin-service-api.herokuapp.com/api/v1'
# API_SERVICE = 'http://localhost:5000/api/v1'

META_DESCRIPTION = '''Esta é uma iniciativa coletiva com o intuito de compartilhar
                      conhecimento e experiências sobre a área e o mercado.
                      Se você trabalha (ou já trabalhou) com TI na Irlanda,
                      provavelmente tem algo a acrescentar.'''

META_KEYWORDS = ['itindublin', 'brasil', 'informacao', 'tecnologia']

TIMEZONE = 'Europe/Paris'
THEME = 'themes/malt'
MALT_BASE_COLOR = 'black'

SITE_LOGO = ''
SITE_LOGO_MOBILE = ''

# STATIC_PATHS = ['wiki_pages']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# EXTRA_TEMPLATES_PATHS = ['malt.templates.wiki']
# TEMPLATE_PAGES = {}
#
# TEMPLATE_PAGES['wiki.html'] = 'wiki/index.html'

WELCOME_TITLE = '''Seja bem vindo ao Grupo
                <p>  {}!'''.format(SITENAME)
WELCOME_TEXT = 'Grupo Profissionais e Estudantes Brasileiros de IT em Dublin'
SITE_BACKGROUND_IMAGE = 'images/banners/ireland_capa_c.jpg'
FOOTER_ABOUT = '''Esta é uma iniciativa coletiva com o intuito de compartilhar
                  conhecimento e experiências sobre a área e o mercado.
                  Se você trabalha (ou já trabalhou) com TI na Irlanda,
                  provavelmente tem algo a acrescentar.'''

DEFAULT_LANG = u'pt'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'blog/categorias'
CATEGORIES_SAVE_AS = 'blog/categorias/index.html'
CATEGORY_URL = 'blog/categorias/{slug}'
CATEGORY_SAVE_AS = 'blog/categorias/{slug}/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = 'blog/autores/{slug}'
AUTHOR_SAVE_AS = 'blog/autores/{slug}/index.html'
AUTHORS_URL = 'blog/autores'
AUTHORS_SAVE_AS = 'blog/autores/index.html'

INDEX_SAVE_AS = "blog/index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['./.plugins']
PLUGINS = [
    'better_figures_and_images',
    'sitemap',
    'tipue_search',
]

GOOGLE_GROUPS_MAIL_LIST_NAME = 'it-irlanda-br'
GOOGLE_ANALYTICS_CODE = 'UA-85207950-1'
RESPONSIVE_IMAGES = True
PYGMENTS_STYLE = "perldoc"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

GITHUB_REPO = "http://github.com/lffsantos/itindublin.github.io"
GITHUB_BRANCH = "master"

OPEN_GRAPH_IMAGE = "/images/logo/logo-inv.png"

# Navbar Links
NAVBAR_HOME_LINKS = [
    {
        "title": "Wiki",
        "href": "wiki",
    },
    {
        "title": "Blog",
        "href": "blog",
    },
    {
        'title': 'Eventos',
        'href': '#',
        'desc': 'Eventos da Relacionados a TI e Meetup do Grupo',
        'children': [
            {
                'title': 'Eventos de Ti',
                'href': 'eventos',
            },
            {
                'title': 'Meetup do Grupo',
                'href': 'encontros',
            }
        ]
    },
    {
        'title': 'Participe',
        'href': '#',
        'desc': 'Encontre e participe da comunidade e compartilhe suas dúvidas e idéias.',
        'children': [
            {
                'title': 'Lista de Discussões',
                'href': 'lista-de-discussoes',
            },

        ]
    },
    {
        'title': 'Contribua',
        'href': '#',
        'desc': 'Veja como contribuir e ajudar a comunidade crescer.',
        'children': [
            {
                'title': 'Contribuir com a Wiki',
                'href': 'como-contribuir-com-a-wiki',
            },
            {
                'title': 'Contribuir com o Blog',
                'href': 'como-publicar-um-artigo',
            },
        ]
    },
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS[0:4] + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

SOCIAL_LINKS = (
    {
        "href": "https://itindublin.herokuapp.com/",
        "icon": "fa-slack",
        "text": "Slack",
    },
    {
        "href": "https://github.com/ITinDublin",
        "icon": "fa-github",
        "text": "GitHub",
    },
    {
        "href": "https://www.facebook.com/groups/ITinDublin/",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
    {
        "href": "https://groups.google.com/forum/#!forum/it-irlanda-br",
        "icon": "fa-envelope",
        "text": "Mailing List",
    },
)

MEMBROS = OrderedDict((
))

MALT_COMUNITY = [
    {
        "title": "Mídias Sociais",
        "text": "Grupo No Facebook",
        "buttons": [
            {
                "icon": "fa fa-facebook",
                "text": "Facebook",
                "href": "https://www.facebook.com/groups/ITinDublin/",
            },
        ],
    },
    {
        "title": "Slack",
        "text": "Grupo do ItInDublin no Slack",
        "buttons": [
            {
                "icon": "fa-slack",
                "text": "Slack",
                "href": "https://itindublin.herokuapp.com/",
            },
        ],
    },
    {
        "title": "Lista de emails",
        "text": "Para quem curte o bom e velho email, "
                "temos a lista de discussão oficial do"
                " ItInDublin no google groups.",
        "buttons": [
            {
                "icon": "fa-email",
                "text": "Lista",
                "href": "https://groups.google.com/forum/#!forum/it-irlanda-br",
            },
        ],
    }
]

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Meetup",
                "icon": "fa-comments",
                "text": "É uma chance de fazer networking com muitos brasileiros da área de TI (alguns estudando,"
                        "alguns trabalhando e outros ainda procurando emprego).<br>"
                        "Ótima oportunidade para tirar dúvidas sobre visto,"
                        "mercado de trabalho, se apresentar para o pessoal e fazer amizades."
                ,
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "encontros",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "Mussum Ipsum, cacilds vidis litro abertis. "
                        "Quem manda na minha terra sou Euzis! Leite de capivaris, "
                        "leite de mula manquis. Mais vale um bebadis conhecidiss, "
                        "que um alcoolatra anonimiss. "
                        "Ta deprimidis, eu conheço uma cachacis que pode alegrar sua vidis.”",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": "Mussum Ipsum, cacilds vidis litro abertis. "
                        "Leite de capivaris, leite de mula manquis. "
                        "Pra lá , depois divoltis porris, paradis. "
                        "Quem num gosta di mé, boa gente num é. undefined",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "projetos",
                    },
                ],
            },
        ]
    },
]
from functions import *

GET_AVATAR = get_avatar
GET_WIKI_PAGES = get_wiki_pages
GET_ARTICLE_AT_GITHUB = get_article_at_github
GET_ARTICLE_IMAGE = get_article_image
GET_LINK = get_link
GET_TAGS_WIKI = get_tags_wiki
GET_GROUPS_MEETUP = get_groups_meetup('content/eventos/meetups.json')

clear_cache_event_group_meetup(API_SERVICE)