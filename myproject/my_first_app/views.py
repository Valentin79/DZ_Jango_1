from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Main page accessed')

    html = '<!DOCTYPE html>\
            <html lang="en">\
            <head>\
            <meta charset="UTF-8">\
            <meta name="viewport" content="width=device-width, initial-scale=1.0">\
            <link rel="stylesheet" href="/static/style.css">\
            <title>Главная</title>\
            </head>\
            <body><h1>Главная</h1></body>\
            </html>'

    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')

    html = '<!DOCTYPE html>\
                <html lang="en">\
                <head>\
                <meta charset="UTF-8">\
                <meta name="viewport" content="width=device-width, initial-scale=1.0">\
                <link rel="stylesheet" href="/static/style.css">\
                <title>Обо мне</title>\
                </head>\
                <body><h1>Обо мне</h1></body>\
                </html>'

    return HttpResponse(html)
