# 配置文件

# BASE_DIR
#     当前文件的根目录,django会依此来定位工程内的相关文件

# DEBUG
#     调试模式,创建工程后初始值为True,默认工作在调试模式下
#     作用
#         修改代码文件,程序自动重启
#         django程序出现异常,前端显示报错追踪信息,非调试模式下,返回Server Error(500)

# 静态文件
#     项目中的css,js,图片都是静态文件,一般放到一个单独的目录中以方便管理
#     为了提供静态文件,需要配置两个参数
#         STATICFILES_DIRS存放查找静态文件目录
#         STATIC_URL访问静态文件URL前缀

# App应用配置
#     在每个应用目录中都包含了apps.py文件,用于保存该应用相关信息
#     创建应用是,django会向apps.py文件中写入一个该应用的配置类
#         AppConfig.name属性表示这个配置类是加载到哪个应用,默认自动生成
#         AppConfig.verbose_name属性用于设置该应用的直观可读的名字,在Admin管理站点中显示
