import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from views.main_view import main

if __name__ == "__main__":
    main()
