activate_this = '/home/hackto/favours/app-env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import site
site.addsitedir('/home/hackto/favours/app')

from application import app as application
