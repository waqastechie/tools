from urllib import response
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import requests
from urllib.parse import quote
from yt_keyword_researcher.models import Keyword
from yt_keyword_researcher.models import Suggestion
from django.http import JsonResponse
from django.db.models import Q
import json

# import people_also_ask

# Create your views here.


def index(request):

    return render(request, "yt-keyword-researcher-index.html")


# def people_also_ask_func(suggestion):
#     ques = people_also_ask.get_related_questions(suggestion, 10)
#     return ques


def yt_question_explorer(request):
    if request.GET.get('keyword', None) is not None and request.is_ajax():
        keyword = request.GET.get('keyword')
        response = {}
        questions_list = [keyword]
        q = keyword
        keyword_obj, keyword_created = Keyword.objects.get_or_create(
            keyword=keyword
        )

        if keyword_created == True:

            # its mean new keyword
            # people_also_ask_ques = people_also_ask_func(q)
            # print("people_also_ask")
            # print(people_also_ask_ques)

            # for question in people_also_ask_ques:
            #     # print(" ok")
            #     ques = question.split("?")[0]
            #     suggestion_obj= Suggestion(
            #         keyword_id=keyword.id,
            #         suggestion=ques)
            #     suggestion_obj.save()
            questions_list = google_suggestions(q, questions_list)
            for item in questions_list:
                suggestion_obj = Suggestion(
                    keyword_id=keyword_obj.id,
                    suggestion=item,
                    type="question")
                suggestion_obj.save()

        suggestion_obj = Suggestion.objects.filter(
            (Q(keyword_id=keyword_obj.id) | Q(suggestion__icontains=keyword)) & Q(type__contains='question')).values('suggestion')
        
            
        return JsonResponse(list(suggestion_obj),safe=False)
    else:
        return JsonResponse(False)


def google_suggestions(q, questions_list):
    # url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + q
    # response = requests.get(url, verify=False)
    # suggestions = json.loads(response.text)

    # for word in suggestions[1]:
    #     questions_list.append(word)

    # functions for getting more kws, cleaning and search volume
    questions_list = q_generator(q, questions_list)

    questions_list = clean_df(q, questions_list)

    return questions_list


def q_generator(keyword, questions):
    # we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
    prefixes = ['how', 'which', 'why', 'where', 'who', 'when',
                'are', 'what', 'is', 'can', 'will', 'do', 'does']

    for prefix in prefixes:
        # print(prefix)
        url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + \
            prefix + " " + keyword
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        kws = suggestions[1]
        length = len(kws)

        for n in range(length):
            # print(kws[n])
            questions.append(kws[n])
    return questions

# #############################################################################


def yt_prepositional_explorer(request):

    if request.GET.get('keyword', None) is not None and request.is_ajax():
        keyword = request.GET.get('keyword')
        response = {}
        prep_keyword = [keyword]
        q = keyword
        keyword_obj, keyword_created = Keyword.objects.get_or_create(
            keyword=keyword
        )

        prep_keyword = prepositional_google_suggestions(q, prep_keyword)
        for item in prep_keyword:
            suggestion_obj = Suggestion(
                keyword_id=keyword_obj.id,
                suggestion=item,
                type="preposition")
            suggestion_obj.save()

        suggestion_obj = Suggestion.objects.filter(
            (Q(keyword_id=keyword_obj.id) | Q(suggestion__icontains=keyword)) & Q(type__contains='preposition')).values('suggestion')

        return JsonResponse(list(suggestion_obj),safe=False)
    else:
        return JsonResponse(False)


def prepositional_google_suggestions(q, prep_keyword):

    # url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + q
    # response = requests.get(url, verify=False)
    # suggestions = json.loads(response.text)
    # for related terms
    # for word in suggestions[1]:
    #     prep_keyword.append(word)

    # functions for getting more kws, cleaning and search volume
    prep_keyword = p_generator(q, prep_keyword)
    prep_keyword = clean_df(q, prep_keyword)
    return prep_keyword


def p_generator(keyword, prep_keyword):

    # we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
    suffixes = ['can', 'for', 'is',
                'near', 'to', 'with', 'without']

    for suffix in suffixes:
        # print(suffix)
        url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + \
            keyword + " " + suffix
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        kws = suggestions[1]
        length = len(kws)

        for n in range(length):
            # print(kws[n])
            prep_keyword.append(kws[n])
    return prep_keyword

#################################################################################################################


def yt_comparison_explorer(request):

    if request.GET.get('keyword', None) is not None and request.is_ajax():
        keyword = request.GET.get('keyword')
        response = {}
        comparison_keyword = [keyword]
        q = keyword
        keyword_obj, keyword_created = Keyword.objects.get_or_create(
            keyword=keyword
        )

        comparison_keyword = comparison_google_suggestions(
            q, comparison_keyword)
        for item in comparison_keyword:
            suggestion_obj = Suggestion(
                keyword_id=keyword_obj.id,
                suggestion=item,
                type="compariosn")
            suggestion_obj.save()

        suggestion_obj = Suggestion.objects.filter(
            (Q(keyword_id=keyword_obj.id) | Q(suggestion__icontains=keyword)) & Q(type__contains='compariosn')).values('suggestion')
        
            
        return JsonResponse(list(suggestion_obj),safe=False)
    else:
        return JsonResponse(False)


def comparison_google_suggestions(q, comparison_keyword):

    # url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + q
    # response = requests.get(url, verify=False)
    # suggestions = json.loads(response.text)
    # for related terms
    # for word in suggestions[1]:
    #     comparison_keyword.append(word)

    # functions for getting more kws, cleaning and search volume
    comparison_keyword = comparion_generator(q, comparison_keyword)
    comparison_keyword = clean_df(q, comparison_keyword)
    return comparison_keyword


def comparion_generator(keyword, comparison_keyword):

    # we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
    suffixes = ['and', 'like', 'or',
                'versus', 'vs']

    for suffix in suffixes:
        # print(suffix)
        url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + \
            keyword + " " + suffix
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        kws = suggestions[1]
        length = len(kws)

        for n in range(length):
            # print(kws[n])
            comparison_keyword.append(kws[n])
    return comparison_keyword
##################################################################################################################


def yt_alpha_explorer(request):

    if request.GET.get('keyword', None) is not None and request.is_ajax():
        keyword = request.GET.get('keyword')
        response = {}
        alpha_keyword = [keyword]
        q = keyword
        keyword_obj, keyword_created = Keyword.objects.get_or_create(
            keyword=keyword
        )

        alpha_keyword = alpha_google_suggestions(
            q, alpha_keyword)
        for item in alpha_keyword:
            suggestion_obj = Suggestion(
                keyword_id=keyword_obj.id,
                suggestion=item,
                type="alpha")
            suggestion_obj.save()

        suggestion_obj = Suggestion.objects.filter(
            (Q(keyword_id=keyword_obj.id) | Q(suggestion__icontains=keyword)) & Q(type__contains='alpha')).values('suggestion')
        
            
        return JsonResponse(list(suggestion_obj),safe=False)
    else:
        return JsonResponse(False)


def alpha_google_suggestions(q, alpha_keyword):

    # url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + q
    # response = requests.get(url, verify=False)
    # suggestions = json.loads(response.text)
    # for related terms
    # for word in suggestions[1]:
    #     alpha_keyword.append(word)

    # functions for getting more kws, cleaning and search volume
    alpha_keyword = alpha_generator(q, alpha_keyword)
    alpha_keyword = clean_df(q, alpha_keyword)
    return alpha_keyword


def alpha_generator(keyword, alpha_keyword):

    # we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
    suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'x', 'y', 'z']

    for suffix in suffixes:
        # print(suffix)
        url = "http://suggestqueries.google.com/complete/search?client=chrome&ds=yt&q=" + \
            keyword + " " + suffix
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)

        kws = suggestions[1]
        length = len(kws)

        for n in range(length):
            # print(kws[n])
            alpha_keyword.append(kws[n])
    return alpha_keyword

##################################################################################################################


def clean_df(keyword, questions):
    # removing duplicates from the list
    questions = list(dict.fromkeys(questions))

    # checking if keyword is in the list and removing anything that doesnt contain the keyword
    new_list = [word for word in questions if all(
        val in word for val in keyword.split(' '))]
    return new_list
