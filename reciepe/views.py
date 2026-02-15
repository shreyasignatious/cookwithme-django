from django.shortcuts import render, redirect, get_object_or_404
from .models import ReciepeData

def home(request):
    if request.method == 'POST':
        # Use correct field names from your form
        reciepe_name = request.POST.get('reciepe_name', '').strip()
        reciepe_desc = request.POST.get('reciepe_desc', '').strip()  # Changed from 'reciepe_description'
        rating = request.POST.get('rating', '').strip()
        image = request.FILES.get('reciepe_img')  # Changed from 'reciepe_image'
        
        # Debug print to check values
        print(f"Name: {reciepe_name}")
        print(f"Desc: {reciepe_desc}")
        print(f"Rating: {rating}")
        print(f"Image: {image}")

        # Validate required fields
        if not reciepe_name or not reciepe_desc:
            return render(request, 'home.html', {
                'error': 'Recipe name and description are required'
            })

        ReciepeData.objects.create(
            reciepe_name=reciepe_name,
            reciepe_description=reciepe_desc,  # Model field is reciepe_description
            rating=rating,
            image=image
        )
        return redirect('home')

    return render(request, 'home.html')

def view_rec(request):
    reciepe_datas = ReciepeData.objects.all()
    return render(request, 'view_rec.html', {'datas': reciepe_datas})

def view_one(request, id):
    data = get_object_or_404(ReciepeData, reciepe_id=id)
    return render(request, 'view_one.html', {'data': data})

def update_rec(request, rec_id):
    rec = get_object_or_404(ReciepeData, reciepe_id=rec_id)

    if request.method == "POST":
        reciepe_name = request.POST.get('reciepe_name', '').strip()
        reciepe_description = request.POST.get('reciepe_description', '').strip()
        rating = request.POST.get('rating', '').strip()
        
        if not reciepe_name:
            return render(request, 'update_rec.html', {
                'data': rec,
                'error': 'Recipe name is required'
            })
        
        rec.reciepe_name = reciepe_name
        rec.reciepe_description = reciepe_description
        rec.rating = rating

        if request.FILES.get('reciepe_image'):
            rec.image = request.FILES.get('reciepe_image')

        rec.save()
        return redirect('view_rec')

    return render(request, 'update_rec.html', {'data': rec})

def delete_rec(request, rec_id):
    rec = get_object_or_404(ReciepeData, reciepe_id=rec_id)
    rec.delete()
    return redirect('view_rec')