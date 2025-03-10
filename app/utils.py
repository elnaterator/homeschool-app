from django.http import HttpResponse, HttpRequest
from django.template import loader

def html_response(name: str, request: HttpRequest, context: dict = {}) -> HttpResponse:
    """
    Returns a response with partial html template if HX-Request header is set to true,
    otherwise returns a full html with base template.
    """
    if request.headers.get("HX-Request") == "true":
        template = loader.get_template(f"partials/{name}.html")
    else:
        template = loader.get_template(f"{name}.html")
    return HttpResponse(template.render(context, request))