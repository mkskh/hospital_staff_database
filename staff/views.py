from django.shortcuts import render
import requests
from .forms import SearchForm

def index(request):

    url = "http://127.0.0.1:8080/candidates/"
    form = SearchForm(request.POST or None)

    if request.method == "GET":
        response = requests.get(url).json()
        return render(request, 'candidates/index.html', {"response": response, "form": form})
    
    if request.method == "POST" and form.is_valid():
        response = requests.get(url).json()
        key = form.cleaned_data['search']
        city = form.cleaned_data['city']
        gender = form.cleaned_data['gender']
        age_more_than = form.cleaned_data['age_more_than']
        age_less_than = form.cleaned_data['age_less_than']

        search_res = []
        target_fields = {"first_name", "last_name", "email", "phone", "university", "profession"}

        for item in response:
            if not key:
                search_res.append(item)
            else:
                match_found = False
                for title, field in item.items():
                    if title in target_fields:
                        if str(key).lower() in str(field).lower():
                            search_res.append(item)
                            match_found = True
                            break
                if match_found:
                    continue 
        
        if city:
            search_res = [item for item in search_res if item["city"] == city]

        if gender:
            search_res = [item for item in search_res if item["gender"] == gender]

        if age_more_than:
            search_res = [item for item in search_res if item["age"] > age_more_than]

        if age_less_than:
            search_res = [item for item in search_res if item["age"] < age_less_than]

        quantity = len(search_res)
        if quantity == 103:
            quantity = 0

        return render(request, 'candidates/index.html', {"response": search_res, "form": form, "quantity": quantity})


def reset(request):

    url = "http://127.0.0.1:8080/candidates/"
    form = SearchForm()

    response = requests.get(url).json()

    return render(request, 'candidates/index.html', {"response": response, "form": form})