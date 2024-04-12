from bookapp.models import Profile
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('bookapp/profiles_form.html')
def profiles_form(profiles: Profile = None):

    return {'profiles': profiles}
