from django import forms
from aplikacja import models

class addCommentForm(forms.ModelForm):
    class Meta:
        model = models.Ratings
        fields = ["FirstName","LastName","Text","Rate"]

class UpdateBrandDataForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = "__all__"

class UpdateStatisticForm(forms.ModelForm):
    class Meta:
        model = models.Done
        fields = "__all__"

class addNewMessageForm(forms.ModelForm):
    class Meta:
        model = models.Messages
        fields = ["author","phone","email","text"]

class addNewMainCategoryForm(forms.ModelForm):
    class Meta:
        model = models.MainCategory
        fields = ["name","image"]

class addNewCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ["name","image","category"]
        
class addNewObjectForm(forms.ModelForm):
    class Meta:
        model = models.Object
        fields = ["name","image","category"]


