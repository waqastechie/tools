import json
from django.shortcuts import render
import requests
import pandas as pd
from core_web_vitals.models import CoreWebVitals
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
# Create your views here.


def index(request):

    return render(request, "cwv-index.html")


def engine(request):

    if request.GET.get('url', None) is not None and request.is_ajax():
        api_key = "AIzaSyDW6x_jD0x1XwixqVMX2b3vIeEOfUGenNY"
        url = request.GET.get('url')
        device = request.GET.get('device')
        category = request.GET.get('category')

        # device = 'mobile'  # Select here device it can be mobile or desktop
        # category = 'performance'
        df_list = []

        # making api call for URL
        response = requests.get("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" +
                                url+"&strategy="+device+"&category="+category + "&key="+api_key)

        # saving response as json
        if response.status_code == 200:
            data = response.json()
            core_Web_vitals_obj = CoreWebVitals(
                url=url,
                data=json.dumps(data),
                device=device,
                category=category
            )

            core_Web_vitals_obj.save()
            core_Web_vitals_obj = CoreWebVitals.objects.filter(
                url=url).values('data').latest("created_at")
            # print(json.loads(core_Web_vitals_obj["data"]))
           
            return JsonResponse(json.loads(core_Web_vitals_obj["data"]), safe=False)


        else:
            return JsonResponse(False, safe=False)

    # =============================================================================
    #         #Getting Metrics
    #
    # =============================================================================

        try:
            kind=data['kind']

        except KeyError:
            kind=False
        try:
            kind=data['loadingExperience']["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]

        except KeyError:
            kind=False
        try:
            data=data['lighthouseResult']
        except KeyError:

            data='No Values.'

        # First Contentful Paint
        try:
            # First Contentful Paint
            fcp=data['audits']['first-contentful-paint']['displayValue']
        except KeyError:
            # print('no Values')
            fcp=0
        pass

        # Largest Contentful Paint
        try:

            lcp=data['audits']['largest-contentful-paint']['displayValue']
        except KeyError:
            # print('no Values')
            lcp=0
        pass

        # Cumulative layout shift
        try:

            cls=data['audits']['cumulative-layout-shift']['displayValue']
        except KeyError:
            # print('no Values')
            cls=0
        pass

        try:
            # Speed Index
            si=data['audits']['speed-index']['displayValue']
        except KeyError:
            # print('no Values')
            si=0
        pass
        try:

            # Time to Interactive
            tti=data['audits']['interactive']['displayValue']
        except KeyError:
            # print('no Values')
            tti=0
        try:
            # Total Blocking Time
            tbt=data['audits']['total-blocking-time']['displayValue']
        except KeyError:
            # print('no Values')
            tbt=0
        pass

        try:
            # score
            score=data['categories']['performance']['score']
        except KeyError:
            # print('no Values')
            score=0
        pass

        # list with all values

        values=[url, score, fcp, si, lcp, tti, tbt, cls, device]

        # create DataFrame using from score list
        df_score=pd.DataFrame(values)

        # transpose so its columns
        df_score=df_score.transpose()

        # appending scores to empty df outside for loop
        df_list.append(df_score)

        # concatinating list of dataframe into one
        df=pd.concat(df_list)
        # naming columns
        df.columns=['URL', 'Score', 'FCP', 'SI',
                      'LCP', 'TTI', 'TBT', 'CLS', 'Device']

        # removing s from LCA so we can get mean also transforming it to float so we can get mean values
        df['LCP']=df['LCP'].astype(str).str.replace(r's', '').astype(float)
        df['FCP']=df['FCP'].astype(str).str.replace(r's', '').astype(float)
        df['SI']=df['SI'].astype(str).str.replace(r's', '').astype(float)
        df['TTI']=df['TTI'].astype(str).str.replace(r's', '').astype(float)
        df['TBT']=df['TBT'].astype(str).str.replace(r'ms', '')
        df['TBT']=df['TBT'].astype(str).str.replace(r',', '').astype(float)
        df['Score']=df['Score'].astype(float)
        df['CLS']=df['CLS'].astype(float)
        df['Device']=device
        df['URL']=url

        # storing into db

        core_web_vitals_obj, core_web_vitals_created=CoreWebVitals.objects.get_or_create(
            url=url,
            lcp=df["LCP"],
            fcp=df["FCP"],
            si=df["SI"],
            tti=df["TTI"],
            tbt=df["TBT"],
            score=df["Score"],
            cls=df["CLS"],
            device=device
        )
        # print(core_web_vitals_obj)

        if core_web_vitals_obj:
            data={
                "url": core_web_vitals_obj.url,
                "lcp": core_web_vitals_obj.lcp,
                "fcp": core_web_vitals_obj.fcp,
                "si": core_web_vitals_obj.si,
                "tti": core_web_vitals_obj.tti,
                "tbt": core_web_vitals_obj.tbt,
                "score": core_web_vitals_obj.score,
                "cls": core_web_vitals_obj.cls,
                "device": core_web_vitals_obj.device,
            }

            return JsonResponse(data, safe=False)
        else:
            return JsonResponse(False)
    else:
        return JsonResponse(False)
