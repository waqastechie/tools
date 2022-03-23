from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from parrot import Parrot
import torch
import warnings
from nltk import tokenize
import joblib
from django.urls import path
import os
warnings.filterwarnings("ignore")
# Create your views here.


def index(request):

    return render(request, "article-rewriter-index.html")


def article_rewiter(request):
    if request.POST.get('long_text', None) is not None and request.is_ajax():

        text = request.POST.get('long_text')

        def random_state(seed):
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)

        random_state(42)
        cur_dir = os.path.dirname(__file__)  # get current directory
        # full path to text.
        file_path = os.path.join(cur_dir, 'ml_models/parrot_model.pkl')

        parrot = joblib.load(file_path)

        phrases = text
        phrases = tokenize.sent_tokenize(phrases)
        article = []
        for phrase in phrases:
            # print("-"*100)
            # print("Input_phrase: ", phrase)
            # print("-"*100)
            para_phrases = parrot.augment(
                input_phrase=phrase, max_return_phrases=1)
            for para_phrase in para_phrases:
                article.append(para_phrase[0])
                article.append(".")
            print(article)
            return JsonResponse(article, safe=False)
    else:
        return JsonResponse(False)
