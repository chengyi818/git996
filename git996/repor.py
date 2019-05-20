#!/usr/bin/env python3
# Author: ChengYi
# Mail: chengyi818@foxmail.cn
# created time: Fri 19 Apr 2019 04:20:13 PM CST
from .const import REPO_STATUS_BARE, REPO_STATUS_DIRTY, REPO_STATUS_UPDATED, REPO_STATUS_UNTRACKED, REPO_STATUS_CLEAN
from git import Repo as Gitrepo


class Repo(object):
    def __init__(self, name=None, local_path=None):
        self.name = name
        self.local_path = local_path
        self.status = None
        self.repo = None

    def update_local_status(self):
        self.repo = Gitrepo(self.local_path)
        if (self.repo.bare):
            self.status = REPO_STATUS_BARE
            return

        if self.repo.untracked_files:
            print(self.local_path, " untrack: ", self.repo.untracked_files)
            self.status = REPO_STATUS_UNTRACKED
            return

        if (self.repo.is_dirty()):
            self.status = REPO_STATUS_DIRTY
            print("Dirty: ", self.local_path)
            return

        self.status = REPO_STATUS_CLEAN

    def sync(self):
        print("sync: ", self.local_path)
        self.repo = Gitrepo(self.local_path)

        if (self.repo.bare):
            self.status = REPO_STATUS_BARE
            return

        if (self.repo.is_dirty()):
            self.status = REPO_STATUS_DIRTY
            return

        remote = self.repo.remotes.origin
        remote.pull()
        self.status = REPO_STATUS_UPDATED
