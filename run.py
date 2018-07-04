from app import app
from os import environ
app.run(debug=True, host=0.0.0.0, port=environ.get("PORT", 5000))
