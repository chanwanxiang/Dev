# 中间件的作用:
#     每次请求和响应的时候会被调用

# 中间件的使用举例
#     可以判断每次请求中是否携带了cookie中的某些信息



def simpleMiddleware(getResponse):

    def middleware(request):
        username= request.COOKIES.get('username')
        if username is None:
            print('USERNAME IS NONE')

        # 这里是请求前
        print('before request')

        response = getResponse(request)

        # 这里是请求后
        print('after request')
        return response

    return middleware
    