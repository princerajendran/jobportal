from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + email)
                return redirect('account:login')
            else:
                # messages.success(request, 'Form not valid')
                context = {'form': form}
                return render(request, 'account/register.html', context)

        context = {'form': form}
        return render(request, 'account/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            # print(user.is_staff)

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('admin:index')
                else:
                    # messages.success(request, 'Login successfully')
                    return redirect('home:home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home:home')
