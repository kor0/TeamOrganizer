from app import app
from os import environ
#port=environ.get("PORT")
port = os.environ['PORT']
app.run(debug=True, host=0.0.0.0, port=port)
