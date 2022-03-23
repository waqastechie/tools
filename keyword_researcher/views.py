from django.shortcuts import render
import requests
import json
from django.db.models import Q
from keyword_researcher.models import Keyword
from keyword_researcher.models import Suggestion
from django.http import JsonResponse
# Create your views here.


def index(request):

    return render(request, "keyword-researcher-index.html")


def keyword_researcher(request):
    if request.GET.get('keyword', None) is not None and request.is_ajax():
        response = {}
        keyword = request.GET.get('keyword')
        keyword_obj, keyword_created = Keyword.objects.get_or_create(
            keyword=keyword
        )
        if keyword_created == True:
            keywords = [keyword]
            url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
            r = requests.get(url, verify=False)
            suggestions = json.loads(r.text)

            for word in suggestions[1]:
                keywords.append(word)

            # functions for getting more kws, cleaning and search volume
            prefixes(keyword, keywords)
            suffixes(keyword, keywords)
            numbers(keyword, keywords)
            get_more(keyword, keywords)
            new_list = clean_df(keywords, keyword)
            for item in new_list:
                suggestion_obj = Suggestion(
                    keyword_id=keyword_obj.id,
                    suggestion=item)
                suggestion_obj.save()

        suggestion_obj = Suggestion.objects.filter(
            Q(keyword_id=keyword_obj.id) | Q(suggestion__icontains=keyword)).values('suggestion')
        return JsonResponse(list(suggestion_obj), safe=False)
    else:
        return JsonResponse(False)


# prefixes adds a value from the prefix list before the keyword we passed
# and get suggestions out of that. Then it appends each of the keyword to
# the keywords lists.

# function passes to parameters:
#     keyword: value we want to check.
#     keywords: list to append values.


def prefixes(keyword, keywords):

    # we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
    # prefixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    #             's', 't', 'u', 'v', 'y', 'x', 'y', 'z', 'how', 'which', 'why', 'where', 'who', 'when', 'are', 'what']
    prefixes = ['how', 'which', 'why', 'where', 'who', 'when', 'are', 'what','is','do','does']
    for prefix in prefixes:
        # print(prefix)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + \
            prefix + " " + keyword
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        kws = suggestions[1]
        length = len(kws)

        for n in range(length):
            # print(kws[n])
            keywords.append(kws[n])


# suffixes adds a value from the prefix list after the keyword we passed
# and get suggestions out of that. Then it appends each of the keyword to
# the keywords lists.

# function passes to parameters:
#     keyword: value we want to check.
#     keywords: list to append values.


def suffixes(keyword, keywords):
    # we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
    suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'y', 'x', 'y', 'z', 'like', 'for', 'without', 'with', 'versus', 'vs', 'to', 'near', 'except', 'has']

    for suffix in suffixes:
        # print(suffix)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + \
            keyword + " " + suffix
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        kws = suggestions[1]
        length = len(kws)

        for n in range(length):
            # print(kws[n])
            keywords.append(kws[n])


# Numbers runs a for loop from 0 to 9 and appends the number as a string
# at the end of the keyword. E.g Broncos 2.  this can give something like
# Broncos 2020 or Broncos 2021 team


# function passes to parameters:
#     keyword: value we want to check.
#     keywords: list to append values.


def numbers(keyword, keywords):
    # we can add more numbers
    for num in range(0, 10):
        # print(num)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + \
            keyword + " " + str(num)
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        kws = suggestions[1]
        length = len(kws)

        for n in range(length):
            # print(kws[n])
            keywords.append(kws[n])


# get more takes the keywords list and runs the keywords via the
# api to get more suggestions. Every new suggestion is stored back in
# the keywords list.

# I set a limit of 1000 Keywords but this can be increased.
# Once it hits 1000 keyowords it stops


def get_more(keyword, keywords):
    for i in keywords:
        # print(i)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + i
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        keywords2 = suggestions[1]
        length = len(keywords2)

        for n in range(length):
            # print(keywords2[n])
            keywords.append(keywords2[n])
            # print(len(keywords))

        if len(keywords) >= 10:  # we can increase this number if we want more keywords
            # print('###Finish here####')
            break


# cleand df performs 2 important things:
#     - Remove dupliactes fro the list
#     - Remove keywords that dont contain the primary keyword.

# e.g: if we searched for Netlfix and playstation is on the list.
#     palaystation will be removed.


def clean_df(keywords, keyword):
    # removing duplicates from the list
    keywords = list(dict.fromkeys(keywords))

    # checking if keyword is in the list and removing anything that doesnt contain th keyword
    new_list = [word for word in keywords if all(
        val in word for val in keyword.split(' '))]

    return new_list
