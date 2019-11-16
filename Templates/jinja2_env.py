from jinja2 import Environment
def environment(**options):
    env = Environment(**options)

    return env

# 1.自定义过滤器
def do_listreverse(li):
    if li == "B":
        return "哈哈"