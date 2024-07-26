import argparse

def get_my_args_parser():
    parser = argparse.ArgumentParser("just test argparse api", add_help=False) #设置 add_help=False 时，它主要是为了避免与父解析器冲突并保持清晰的参数定义。
    parser.add_argument('epoch', type = int)
    parser.add_argument('--lr', default = 0.01, type = float, help=" ")
    
    return parser #need return parser for parents

def main(args):
    pass

if __name__ == "__main__":
    # 创建参数解析器
    #使用了 parents=[get_my_args_parser()]，这个参数的作用是将 get_my_args_parser() 返回的解析器作为父解析器的一部分，即将子解析器的参数选项添加到父解析器中。
    parser = argparse.ArgumentParser("just test argparse api", parents=[get_my_args_parser()])
    # 解析命令行参数
    args = parser.parse_args()
    print(args.lr, args.epoch)
    main(args)
