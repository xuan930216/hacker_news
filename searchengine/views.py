from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from searchengine.bigquery_search import query_hackernews
import json

from django.core.paginator import Paginator

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
            url = reverse('results')
            if date:
                date = date.strftime('%Y-%m-%d')
                url += '?title=' + title + '&text=' + text + '&date=' + date
            else:
                url += '?title=' + title + '&text=' + text
            return HttpResponseRedirect(url)
            # return render(request, 'result.html', {'result': query_hackernews(request.POST['stories_title'])})
        
    #if not post method will create a blank form
    else:
        form = NewsSearchForm()

    return render(request, 'search.html', {'form': form})

def results(request):
    title = request.GET.get('title', None)
    text = request.GET.get('text', None)
    date = request.GET.get('date', None)
    if title and text:
        query_result =  query_hackernews(title, text, date)

        #store all result
        json_list = []
        for row in query_result:
            #save on record
            data = {}
            data['title'] = row.title
            data['url'] = row.url
            data['text'] = row.text
            data['date'] = row.date.strftime('%Y-%m-%d')
            json_data = json.dumps(data)
            json_list.append(json_data)
        
        paginator = Paginator(json_list, 5)#5 contents prt page
        page = request.GET.get('page')
        result = paginator.get_page(page)

        currentUrl = request.get_full_path

        return render(request, 'results.html', {'result': result, "currentUrl": currentUrl})
    else:
        return HttpResponseRedirect('/search/')
