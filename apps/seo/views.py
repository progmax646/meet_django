from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from seo.modules import Seo

# Create your views here.


@api_view()
def get_pos(request, type, keyword):
    position = Seo.get_position(type, keyword)
    return Response({"type":type,
                     "keyword":keyword,
                     "posiiton": position})