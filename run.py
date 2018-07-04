from app import app
from os import environ
#port=environ.get("PORT")
port = int(os.environ.get('PORT', 33507))
app.run(debug=True, host=0.0.0.0, port=port)
