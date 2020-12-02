from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import FormView

from . import forms

# Create your views here.
class GreetView(FormView):
    template_name = 'greeting/index.html'  # テンプレート名(htmlファイル名)
    form_class = forms.GreetForm
    success_url = '/greet'

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            if request.is_ajax():
                """Ajax 処理を別メソッドに切り離す"""
                print('### Ajax request')
                return self.ajax_response(form)
            # Ajax 以外のPOSTメソッドの処理
            return super().form_valid(form)
        # フォームデータが正しくない場合の処理
        return super().form_invalid(form)

    def ajax_response(self, form):
        """jQuery に対してレスポンスを返すメソッド"""
        name = form.cleaned_data.get('name')
        return HttpResponse(f'こんにちは、{name}さん！')