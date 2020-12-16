from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


def index(ListAPIView):
    return HttpResponse("Nice!")


class ProductsPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 100
