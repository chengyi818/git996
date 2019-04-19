#!/usr/bin/env python3
# Author: ChengYi
# Mail: chengyi818@foxmail.cn
# created time: Fri 19 Apr 2019 09:51:12 AM CST

import pkg_resources
from .configer import Configer
from .syncer import Syncer
from arghandler import subcmd, ArgumentHandler


@subcmd
def version(parser, context, args):
    git996_version = pkg_resources.get_distribution('git996')
    print(git996_version)


@subcmd('init', help='init git996')
def init(parser, context, args):
    configer = Configer()
    configer.generate_config()


@subcmd('sync', help='sync repositories')
def sync(parser, context, args):
    syncer = Syncer()
    syncer.sync()


def main():
    handler = ArgumentHandler()
    handler.run()


if __name__ == "__main__":
    main()
