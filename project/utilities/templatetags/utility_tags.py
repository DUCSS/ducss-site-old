from django import template
from django.utils.html import escape

register = template.Library()

@register.tag
def escapehtml(parser, token):
    nodelist = parser.parse(('endescapehtml',))
    parser.delete_first_token()
    return EscapeHTMLNode(nodelist)

class EscapeHTMLNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return escape(output).strip().replace('\n', '<br />')

# Copyright 2009, EveryBlock
# This code is released under the GPL.
def raw(parser, token):
    '''Whatever is between {%% raw %} and {%% endraw %} will be preserved as
    raw, unrendered template code.
    '''
    text = []
    parse_until = 'endraw'
    tag_mapping = {
        template.TOKEN_TEXT: ('', ''),
        template.TOKEN_VAR: ('{{', '}}'),
        template.TOKEN_BLOCK: ('{%', '%}'),
        template.TOKEN_COMMENT: ('{#', '#}'),
    }
    # By the time this template tag is called, the template system has already
    # lexed the template into tokens. Here, we loop over the tokens until
    # {% endraw %} and parse them to TextNodes. We have to add the start and
    # end bits (e.g. "{{" for variables) because those have already been
    # stripped off in a previous part of the template-parsing process.
    while parser.tokens:
        token = parser.next_token()
        if token.token_type == template.TOKEN_BLOCK and token.contents == parse_until:
            return template.TextNode(u''.join(text))
        start, end = tag_mapping[token.token_type]
        text.append(u'%s%s%s' % (start, token.contents, end))
    parser.unclosed_block_tag(parse_until)

raw = register.tag(raw)