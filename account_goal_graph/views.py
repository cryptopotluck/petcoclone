from django.shortcuts import render

# Create your views here.
def account_goal(requests):
    return render(requests, 'accoount_goal_graph/goal_graph.html')