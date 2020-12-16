from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

import json
import random


# Create your views here.


@api_view(["GET"])
def fact_generator(request):
    random_number = random.randint(0, 50)
    with open("assets/facts.json", "r", encoding="utf-8") as facts:
        response = json.load(facts)
        random_fact = response[f"{random_number}"]

    random_fact_dict = {
        "fact": random_fact
    }

    return Response(random_fact_dict)
