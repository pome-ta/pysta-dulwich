import sys, os
from pprint import pprint
import inspect

# Import dulwich modules
sys.path.insert(0, os.path.abspath('../dulwich'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
dulwich = __import__('dulwich')

from dulwich.repo import Repo

r = Repo('.')
print(r.head())
# b'2f1f0c75eb8d1968b4df8600cb5e645205529fe1'

