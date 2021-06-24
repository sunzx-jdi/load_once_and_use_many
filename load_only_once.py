# 有关load 模型只加载一次，然后调用模型多次的闭包实例
def load_model():
    # 这个地方写加载模型的代码，只会执行一次，由于闭包调用，会保持变量一直在内存中不释放
    # model = load_model()
    a = 5
    print(a)

    # 下面写模型调用的代码，可多次利用 loadmodel 里面 的参数
    def analysis(b):
        # deal_with_model(model)
        # 变量 a 不会被释放
        sum = b * a
        print(sum)
    # 注意返回的是 函数名 这里是函数地址
    return analysis

mul_5 = load_model()
mul_5(10)
mul_5(20)

