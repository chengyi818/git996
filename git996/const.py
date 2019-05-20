#!/usr/bin/env python3
# Author: ChengYi
# Mail: chengyi818@foxmail.cn
# created time: Fri 19 Apr 2019 05:23:50 PM CST

CONFIG_FILE_NAME = ".git996.toml"

REPO_STATUS_BARE = "bare repo"
REPO_STATUS_DIRTY = "dirty"
REPO_STATUS_UPDATED = "updated"
REPO_STATUS_UNTRACKED = "untracked"
REPO_STATUS_CLEAN = "clean"

TEMPLATE_TOML = """title = "git996 template config file"

[global]
return_if_dirty = true

[repo]
    [repo.linux_kernel]
    local_path = "/home/chengyi/code/github/linux_kernel_all"

    [repo.personal_kata]
    local_path = "/home/chengyi/code/github/kata"

    [repo.dotfiles]
    local_path = "/home/chengyi/.homesick/repos/dotfiles"

    [repo.xv6_gitbook]
    local_path = "/home/chengyi/code/github/Fat-Cheng-s-xv6-journey"

    [repo.personal_xv6_source_code]
    local_path = "/home/chengyi/code/github/my_xv6"
"""
