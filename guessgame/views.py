from django.shortcuts import render,redirect
from .forms import InputtingForm
import random
def guess(request):
    form=InputtingForm()
    return render(request,'index.html',{'form':form})
def resultt(request):
     random_number=random.randint(1,10)
     result=None
     if request.method=='POST':
          user_guess = request.POST.get('guess')
          if user_guess:
               user_guess=int(user_guess)
               
               if random_number==user_guess:
                    result="CORRECT ANSWER"
               else:
                    result=f"The correct number was {random_number}. Try again!"   
     else:
          result="please enter a valid number"
     return render(request, 'results.html', {'result': result})
  
          
     