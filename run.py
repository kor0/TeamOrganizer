#!flask/bin/python
from app import app
import sys
import os
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', int(sys.argv[1])))
    app.run(debug=True, host='0.0.0.0', port=port)
