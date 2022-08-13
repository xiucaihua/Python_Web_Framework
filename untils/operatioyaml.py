#coding:utf-8
import yaml
import os

def base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def readYaml():    #load()对文件进行反序列化，本质上是读取文件里面的内容
    with open(os.path.join(base_dir(),'data','login.yaml'),encoding='utf-8') as f:
        return yaml.safe_load(f)