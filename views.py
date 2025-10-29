from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from .forms import FeedbackForm

# Display all feedbacks (Read)
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})

# Add new feedback (Create)
def feedback_create(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

# Update feedback (Update)
def feedback_update(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    form = FeedbackForm(request.POST or None, instance=feedback)
    if form.is_valid():
        form.save()
        return redirect('feedback_list')
    return render(request, 'feedback_form.html', {'form': form})

# Delete feedback (Delete)
def feedback_delete(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == "POST":
        feedback.delete()
        return redirect('feedback_list')
    return render(request, 'feedback_confirm_delete.html', {'feedback': feedback})

# Thank you page
def thank_you(request):
    return render(request, 'thank_you.html')
