from django.shortcuts import render, get_object_or_404
from item.models import Item
from django.contrib.auth.decorators import login_required
from dashboard.models import Action

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse


from item.models import Item

from conversation.models import Conversation

from conversation.forms import ConversationMessagesForm






# Create your views here.
@login_required
def dashboard(request):
    items = Item.objects.filter(published_by=request.user)[0:10]

    return render(request, 'dashboards.html', {
        'items': items,
    })



def insights(request):
    items = Item.objects.filter(published_by=request.user)[0:10]
    actions = Action.objects.all()
    return render(request, 'insights.html', {
        'items': items,
        'actions': actions,
    })




def inbox(request):

    return render(request, 'inbox.html')




def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.published_by == request.user:
        return redirect('dashboard:dashboard')
    
    conversation = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:
        pass #redirect to conversions

    if request.method == 'POST':
        form = ConversationMessagesForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()


            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.published_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
        else:
            form = ConversationMessagesForm()


        return render(request, 'newsms.html', {
            'conversation': conversation,
            'form': form,
        })
    


    return HttpResponse()