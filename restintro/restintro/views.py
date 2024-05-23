from django.shortcuts import render, get_object_or_404
from .models import User
from django.http import HttpResponse
import json


def user(request):
    if request.method == 'GET':
        users = User.objects.all()
        serialized_users = [{
            'id': user.id,
            'name': user.name,
            'age': user.age,
            'email': user.email} for user in users]
        return HttpResponse(json.dumps(serialized_users))

    if request.method == 'POST':
        body = json.loads(request.body)
        user = User(name=body['name'], email=body['email'], age=body['age'])
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}))

def get_or_update_or_delete_user(request, id):

    if request.method == 'GET':
        user = get_object_or_404(User, id=id)
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}))

    if request.method == 'PUT':
        body = json.loads(request.body)
        user = get_object_or_404(User, id=id)
        user.name = body['name']
        user.email = body['email']
        user.age = body['age']
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}))

    if request.method == 'DELETE':
        user = get_object_or_404(User, id=id)
        user.delete()
        return HttpResponse(json.dumps({'id': id, 'deleted': True}))