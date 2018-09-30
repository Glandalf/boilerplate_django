from django.shortcuts import render


def startPage(request):
	""" Just returns a boring welcome page in that case """
	return render(request, 'home.html', locals())


def aboutPage(request):
	""" Just returns another kind of boring static page in that case """
	return render(request, 'about.html', locals())
