from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView

from core.views import LoginRequiredViewedMixin

from .models import Guest


# Create your views here.
class GuestListView(LoginRequiredViewedMixin, ListView):
    model = Guest
    template_name = "guest_list.html"
    context_object_name = "guests"
    ordering = ["-visit_date"]


class GuestCreateView(LoginRequiredViewedMixin, View):
    def get(self, request):
        return render(
            request,
            "guestbook/guest_form.html",
            {"form_data": {"name": "", "institution": "", "purpose": ""}},
        )

    def post(self, request):
        name = request.POST.get("name")
        institution = request.POST.get("institution")
        purpose = request.POST.get("purpose")

        if not name or not institution or not purpose:
            messages.error(request, "All fields are required")
            return render(
                request,
                "guestbook/guest_form.html",
                {
                    "form_data": {
                        "name": name,
                        "institution": institution,
                        "purpose": purpose,
                    }
                },
            )

        Guest.objects.create(name=name, institution=institution, purpose=purpose)
        messages.success(request, "Succesfully added guest data")
        return redirect("guestbook:list")


class GuestUpdateView(LoginRequiredViewedMixin, View):
    def get(self, request, id):
        guest = get_object_or_404(Guest, id=id)
        return render(request, "guestbook/guest_form.html", {"guest": guest})

    def post(self, request, id):
        guest = get_object_or_404(Guest, id=id)

        name = request.POST.get("name")
        institution = request.POST.get("institution")
        purpose = request.POST.get("purpose")

        if not name or not institution or not purpose:
            messages.error(request, "All fields are required")
            return render(
                request,
                "guestbook/guest_form.html",
                {
                    "guest": {
                        "id": id,
                        "name": name or "",
                        "institution": institution or "",
                        "purpose": purpose or "",
                    }
                },
            )

        guest.name = name
        guest.institution = institution
        guest.purpose = purpose
        guest.save()
        messages.success(request, "Update data success")
        return redirect("guestbook:list")


class GuestDeleteView(LoginRequiredViewedMixin, View):
    def get(self, request, id):
        guest = get_object_or_404(Guest, id=id)
        guest.delete()
        messages.success(request, "Delete data success")

        return redirect("guestbook:list")
