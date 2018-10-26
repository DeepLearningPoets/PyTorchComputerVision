from pathlib import Path 
import os

class PythonModule:
    def __init__(self, name):
        self.path = Path(name)

    def __call__(self):
        self.path.mkdir(parents=True, exist_ok=True)
        with open(str(self.path.resolve()) + '/' +'__init__.py', 'w') as f:
             pass

class Template:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.dirs = [
                      'models',
                      'data',
                      'utils']
    def __call__(self):
        self.modules = map(lambda x: PythonModule('{}/{}'.format(self.base_dir, x)), self.dirs)
        [module() for module in self.modules]

        with open(self.base_dir + '/' +'train.py', 'w') as f:
            pass


t = Template(base_dir='./resnet')
t()