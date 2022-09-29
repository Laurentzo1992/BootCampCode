from django.shortcuts import render
from django.http import request, HttpResponse, response



def people(request):
	people = [
	  {
	    'id': 1,
	    'name': 'Bob Smith',
	    'age': 35,
	    'country': 'USA'
	  },
	  {
	    'id': 2,
	    'name': 'Martha Smith',
	    'age': 60,
	    'country': 'USA'
	  },
	  {
	    'id': 3,
	    'name': 'Fabio Alberto',
	    'age': 18,
	    'country': 'Italy'
	  },
	  {
	    'id': 4,
	    'name': 'Dietrich Stein',
	    'age': 85,
	    'country': 'Germany'
	  }
	]
	sortedby_age = sorted(people, key = lambda d: d['age'])
	return render(request, "people/peopl.html", {"people":sortedby_age})


def people_one(request, id=id):
    people = [
	{
	    'id': 1,
	    'name': 'Bob Smith',
	    'age': 35,
	    'country': 'USA'
	},
	{
	    'id': 2,
	    'name': 'Martha Smith',
	    'age': 60,
	    'country': 'USA'
	},
	{
	    'id': 3,
	    'name': 'Fabio Alberto',
	    'age': 18,
	    'country': 'Italy'
	},
	{
	    'id': 4,
	    'name': 'Dietrich Stein',
	    'age': 85,
	    'country': 'Germany'
	}
	]
    
    people_one_list = filter(people, key = lambda d: d['id'])
    return render(request, "people/peopl.html", {"people":people_one_list})

# Create your views here.
