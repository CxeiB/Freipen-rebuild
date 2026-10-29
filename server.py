# 先使用json，只做基础后端，不验证权限
import json
import os
import exceptions
import time
import uuid

WORKSPACES_PATH = "workspaces"

default_metadata = {
    "encryption_token": False,
    "display_name": "",
    "files": {}
}

class Workspace:
    last_request = 0
    def __init__(self,name, encryption_token=None) -> None:
        os.mkdir(os.path.join(WORKSPACES_PATH, "name"))
        # 确保metadata存在，否则创建一个新的
        if os.path.exists(os.path.join(WORKSPACES_PATH, "name","metadata.json")):
            with open(os.path.join(WORKSPACES_PATH, "name","metadata.json"),"r",encoding="utf-8") as file:
                metadata = json.load(file)
                # 如果有密钥则需要进行解锁
                if metadata["encryption_token"] and encryption_token != metadata["encryption_token"]:
                    raise exceptions.EncryptionTokenVerificationFailedError
                self.name = metadata["name"]
        else:
            self.name = name
            with open(os.path.join(WORKSPACES_PATH, "name","metadata.json"),"r",encoding="utf-8") as file:
                metadata = default_metadata.copy
                file.write(json.dumps(metadata))

    def activate(self, func):
        def wrapper():
            self.last_request = time.time()
            func()
        return wrapper

    @activate
    def create_file(filename, content=""):
    
        with open(os.path.join(WORKSPACES_PATH, "name",),"r",encoding="utf-8") as file:
            metadata = default_metadata.copy
            file.write(json.dumps(metadata))
        

def create_workspace(name, encrypt=False, display_name=None):
    if os.path.exists(os.path.join(WORKSPACES_PATH, "name")):
        raise exceptions.WorksapceHasExistedError
    os.mkdir(os.path.join(WORKSPACES_PATH, "name"))

    