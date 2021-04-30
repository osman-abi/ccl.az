from django.utils import translation
from django.shortcuts import redirect


def set_language(request, lang_code):
    translation.activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    return redirect('/'+lang_code)