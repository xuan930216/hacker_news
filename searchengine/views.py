from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect

from searchengine.bigquery_search import query_hackernews

from .forms import NewsSearchForm
# Create your views here.


#search form view
def search(request):
    #if this is a post request, need process the form data and call bigquery function
    if request.POST:
        #create a form instance and populate it with data from the request
        form = NewsSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['stories_title']
            text = form.cleaned_data['stories_text']
            date = form.cleaned_data['date']
            return HttpResponseRedirect('/search/results/')
            # return render(request, 'result.html', {'result': query_hackernews(request.POST['stories_title'])})
        
    #if not post method will create a blank form
    else:
        form = NewsSearchForm()

    return render(request, 'search.html', {'form': form})

def results(request):
    title = request.GET.get('title')
    text = request.GET.get('text')
    date = request.GET.get('date')
    response = "You are looking at the results of title {}, text {}, date {}".format(title, text, date)
    context = {
        'response':response
    }
    return render(request, 'results.html', context)
