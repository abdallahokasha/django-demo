from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import LandmarkForm
from .models import Landmark

def landmark_create(request):
	form = LandmarkForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()
		return HttpResponseRedirect("/landmarks")
	context = {
		"form": form,
	}
	return render(request, "landmark_form.html", context)
    # return redirect("landmark_list")
    # return HttpResponseRedirect("/landmarks")
    # return HttpResponseRedirect(reverse('landmark_list'))

def landmark_details(request, id=None): #retrieve
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Landmark, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "landmark_details.html", context)

def landmark_list(request): #list items
	queryset = Landmark.objects.all()
	context = {
		"object_list": queryset, 
		"title": "All Landmarks"
	}
	return render(request, "index.html", context)
