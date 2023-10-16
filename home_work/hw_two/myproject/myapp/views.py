from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    html = """
    <h1>Добро пожаловать на мой первый сайт!</h1>
    <p>Меня зовут Илья</p>
    """
    logger.info('Посещение главной страницы')
    return HttpResponse(html)

def about(request):
    html = """
    <h1>О себе</h1>
    <p>Немного информации обо мне:</p>
    <ul>
        <li>Имя: Илья</li>
        <li>Возраст: 24</li>
        <li>Любимый цвет: оранжевый</li>
    </ul>
    """
    logger.info('Посещение страницы "О себе"')
    return HttpResponse(html)