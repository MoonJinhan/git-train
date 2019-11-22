from django import forms

check_box = [
    #(인풋, 아웃풋)
    ('one',"하나"),
    ('two',"둘"),
    ('three',"셋"),
]
MONTH_EN=[]

    1:('JAN'),2:('FEB'),3:('MAR'),4:('APR'),5:('MAY'),6:('JUN'),7:('JUL'),8('AGU')
    
    ]  
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(max_length=5,help_text="5자리만 입력하세요.")
    
    # #체크박스
    # content = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    # )
    # #라디오박스
    # content=forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=check_box
    # )
    # #드랍다운
    # content = forms.ChoiceField(
    #     widget=forms.Select,
    #     choices=check_box
    # )

    #날짜
    # content =forms.DateField(
    #     widget=forms=SelectDateWidget(
    #         years=range(1990,2020),
    #         MONTH_EN
    #     )      
    )
        
class Authorform(forms.ModelForm):
    class Meta: 
        model =Author
        field=['name','company']