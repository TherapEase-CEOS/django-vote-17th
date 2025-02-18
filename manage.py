import sys
import os
import django


#django.setup()

#from user.models import Users
#from account.models import User
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vote_toyproject.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
