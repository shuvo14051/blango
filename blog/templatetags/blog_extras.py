from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html


user_model = get_user_model()
register = template.Library()

@register.filter(name="author_details")
def author_details(author, current_user):
    if not isinstance(author, user_model):
        return ""
    
    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
        
    else:
        name = f"{author.username}"

    if author == current_user:
        name = format_html("<strong>{}</strong>", name)

    if author.email:
        # email=escape(author.email)
        # prefix = f'<a href="mailto:{email}">'
        # can do this in a single line
        prefix=format_html('<a href="mailto:{}">', author.email)
        suffix = format_html(f"</a>")
    else:
        prefix = ""
        suffix = ""

    # return mark_safe(f"{prefix}{name}{suffix}")
    # alternative
    return format_html('{}{}{}', prefix, name, suffix)