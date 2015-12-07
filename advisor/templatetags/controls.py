from django import template

register = template.Library()


@register.inclusion_tag('elements/rating.html')
def rating(selected_value, editable=False):
    return {
        'rating': selected_value
    }


@register.inclusion_tag('elements/privacy.html')
def privacy(selected_value):
    return None # TODO


@register.inclusion_tag('elements/follow_button.html')
def follow_button(user_to_follow, following=False):
    return None # TODO