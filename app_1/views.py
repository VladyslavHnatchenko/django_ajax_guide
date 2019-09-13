from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .forms import ContactForm


def contact_page(request):
    form = ContactForm()
    return render(request, "contact.html", {"ContactForm": form})


def post_contact(request):
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({"success": True}, status=200)
    return JsonResponse({"success": False}, status=400)


class ContactAjax(View):
    form_class = ContactForm
    template_name = "contact_cbv.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        return render(self.request, self.template_name, {"ContactForm": form})

    def post(self, *args, **kwargs):
        if self.request.method == "POST" and self.request.is_ajax():
            form = self.form_class(self.request.POST)
            form.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=400)
