# HttpResponse对象
#     视图在接收请求并处理后,必须返回HttpResponse对象或子对象
#     HttpRequest对象由django创建,HttpResponse对象由开发人员创建

# HttpResponse
#     可以使用django.http.HttpResponse来构造响应对象
#         HttpResponse(content=响应体,content_type=响应类型,status=状态码)

# HttpResponse子类
#     django提供了一系列HttpResponse的子类,可以快速设置状态码
#         HttpResponseRedirect            301
#         HttpResponsePermanentRedirect   302
#         HttpResponseNotModified         304
#         HttpResponseBadRequest          400
#         HttpResponseNotFound            404
#         HttpResponseForbidden           403
#         HttpResponseNotAllowed          405
#         HttpResponseGone                410
#         HttpResponseServerError         500

# JsonResponse
#     若要返回json数据,可以使用JsonRequest来构造响应对象
#         帮助我们将数据转换为json字符串
#         设置响应头content-type为application/json

# redirect重定向
