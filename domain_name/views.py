from urllib import response
from django.shortcuts import render
import whois
from domaingistry import Domain
from django.http import JsonResponse
# Create your views here.


def index(request):

    return render(request, "domain-name-index.html")


def check_reg(name):
    try:
        domain_info = whois.whois(name)
        return True
    except:
        return False


def domain_name_checker(request):
    if request.GET.get('domain_name', None) is not None and request.is_ajax():
        domain = request.GET.get('domain_name')
        domain_info_dict = {}
        is_domain_reg = check_reg(domain)
        if is_domain_reg == True:
            domain_info = whois.whois(domain)
            for key, value in domain_info.items():
                domain_info_dict[key] = value
        else:
            domain_info_dict = is_domain_reg
        generated_domains_dict = domain_name_generator(domain)
        response = {"domain_info_dict": domain_info_dict,
                    "generated_domains_dict": generated_domains_dict}
        return JsonResponse(response)
    else:
        return JsonResponse(False)


def domain_name_generator(domain):
    generated_domains_dict = {}
    domain_name = domain.split(".")[0]
    categories = ["common", "new", "extra", "prefix", "suffix", "shuffled"]
    for category in categories:
        d = Domain(domain_name, category)
        generated_domains_dict[category] = d.generate()
    return generated_domains_dict
