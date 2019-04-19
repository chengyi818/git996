# git996
one command to sync multiple git repositories.

I always have serveral git repositories to sync between home and company everyday.It's too tiring to sync repo one by one.This tool is used to sync all the repos one command.

# Install
```
git clone https://github.com/chengyi818/git996
cd git996
sudo python3 setup.py install
```

# Usage

## 1. create config file
```
git996 init
```
This command will create config file in `~/.git996.toml`.

## 2. modify config file
You should modify config file according your situation.

### return_if_dirty

#### True
git996 will print all path of dirty repo, then git996 will exit

#### False
git996 will ignore dirty repo,just pull clean repo.


## 3. sync all repositories
```
git996 sync
```

# TODO

# LiCENSE
MIT License, See the LICENSE file.
