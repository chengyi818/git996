#!/usr/bin/env python3
# Author: ChengYi
# Mail: chengyi818@foxmail.cn
# created time: Fri 19 Apr 2019 02:31:03 PM CST
import threading
from .configer import Configer
from .const import REPO_STATUS_CLEAN
import texttable


class Syncer(object):
    def __init__(self):
        self.configer = Configer()

    def sync(self):
        if not self.configer.parse_config():
            return

        if self.configer.return_if_dirty:
            self.update_status_repos()

        for repo in self.configer.repos:
            if repo.status != REPO_STATUS_CLEAN:
                return

        self.sync_repos()
        self.show_table()

    def update_status_repos(self):
        subthread_list = []
        for repo in self.configer.repos:
            tmpthread = threading.Thread(target=repo.update_local_status,
                                         name="sync repo")
            subthread_list.append(tmpthread)

        for tmpthread in subthread_list:
            tmpthread.start()

        for tmpthread in subthread_list:
            tmpthread.join()

    def sync_repos(self):
        subthread_list = []
        for repo in self.configer.repos:
            tmpthread = threading.Thread(target=repo.sync, name="sync repo")
            subthread_list.append(tmpthread)

        for tmpthread in subthread_list:
            tmpthread.start()

        for tmpthread in subthread_list:
            tmpthread.join()

    def show_table(self):
        tab = texttable.Texttable()
        headings = ['Index', 'Name', 'Local_path', 'Status']
        tab.header(headings)

        index_columns = list()
        name_columns = list()
        local_path_columns = list()
        status_columns = list()

        for i, repo in enumerate(self.configer.repos):
            index_columns.append(i)
            name_columns.append(repo.name)
            local_path_columns.append(repo.local_path)
            status_columns.append(repo.status)

        for row in zip(index_columns, name_columns, local_path_columns,
                       status_columns):
            tab.add_row(row)

        print(tab.draw())
