import base64
from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
import hashlib

# Create your views here.


def index(request):
    return render(request, "hash-generator-index.html")


def hash_generator(request):
    if request.POST.get('message', None) is not None:
        message = request.POST.get('message')
        message = message.encode()
       
        hash = {}
        md5 = hashlib.md5(message).hexdigest()
        sha1 = hashlib.sha1(message).hexdigest()
        sha256 = hashlib.sha256(message).hexdigest()
        sha3_384 = hashlib.sha3_384(message).hexdigest()
        sha3_224 = hashlib.sha3_224(message).hexdigest()
        sha512 = hashlib.sha512(message).hexdigest()
        sha224 = hashlib.sha224(message).hexdigest()
        blake2s = hashlib.blake2s(message).hexdigest()
        sha384 = hashlib.sha384(message).hexdigest()
        sha3_512 = hashlib.sha3_512(message).hexdigest()
        blake2b = hashlib.blake2b(message).hexdigest()   
        sha3_256 = hashlib.sha3_256(message).hexdigest()
        hash = {"md5": md5, "sha1": sha1, "sha256": sha256,
                "sha3_384": sha3_384, "sha3_224": sha3_224, "sha512": sha512, "sha224": sha224, "blake2s": blake2s, "sha384": sha384, "sha3_512": sha3_512, "blake2b": blake2b, "sha3_256": sha3_256}

        return render(request, "hash-generator-index.html", {"hash": hash})
    return redirect('hash_generator_index')
