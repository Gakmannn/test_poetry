from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя",help_text="Введите свое имя")
    ip = forms.GenericIPAddressField(widget=forms.TextInput(attrs={"placeholder":"xxx.xxx.xxx.xxx"}))
    # ipReg = forms.RegexField (regex="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    age = forms.IntegerField(initial=18)
    check = forms.BooleanField(required=False)
    yes_No = forms.NullBooleanField(required=False)
    slug = forms.SlugField(required=False)
    file = forms.FileField(required=False)
    languages = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
    comboIp = forms.FilePathField(path="C:\\Users\\N.Gakman\\Documents\\django\\test_poetry\\metanit\\hello\\static",recursive=True)
    date = forms.CharField(widget=forms.SelectDateWidget,required=False)
    field_order = ["age", "name"]