from proxypool.scheduler import Scheduler
import argparse
# argparse 是 Python 内置的一个用于命令项选项与参数解析的模块
# 通过在程序中定义好我们需要的参数，
# argparse 将会从 sys.argv 中解析出这些参数，并自动生成帮助和使用信息

parser = argparse.ArgumentParser(description='IP代理池')
parser.add_argument('--processor', type=str, help=r'传入 getter \ tester \ server')
args = parser.parse_args()

if __name__ == '__main__':
    # 传入的参数 getter tester server
    # 从Scheduler类中根据传入获取 属性、方法后执行
    getattr(Scheduler(), f'run_{args.processor}', Scheduler().run)()
