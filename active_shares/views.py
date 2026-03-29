from django.shortcuts import render

from .models import Share

def share_list_view(request):
    shares = Share.objects.all()
    context = {
        'shares_list': shares
    }

    return render(request, 'active_shares/share_list.html', context)