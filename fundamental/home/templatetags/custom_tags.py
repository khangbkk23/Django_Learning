from django import template

register = template.Library()

@register.filter(name='contains')
def contains(value, substring):
    """Return True if substring is in value."""
    try:
        return substring in value
    except Exception:
        return False
