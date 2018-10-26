# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models.usuariomodel import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'is_staff', 'is_active', 'nome', 'cpf', 
        'dt_nascimento', 'telefone', 'perfil', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control', 'id':'cpf_user'}),
            'dt_nascimento': forms.DateInput(attrs={'class':'form-control', 'id':'data'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'id':'telefone'}),
            'perfil': forms.Select(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
            }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_staff', 'is_active', 'telefone', 'perfil', 'password']
        exclude = ['nome', 'cpf', 'dt_nascimento']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'id':'telefone'}),
            'perfil': forms.Select(attrs={'class':'form-control'}),
            }
