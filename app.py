from flask import Flask, render_template, request, redirect, url_for
from db import db, URL
import random
import string
import re
from urllib.parse import urlparse

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

def extract_keywords(url, length=6):
    """Extract keywords from URL and create a short code"""
    # Parse the URL to get the path
    parsed = urlparse(url)
    # Get path without leading/trailing slashes
    path = parsed.path.strip('/')
    # Split path into components
    components = re.split(r'[/\-_.]', path)
    # Filter out empty components
    components = [c for c in components if c]
    
    if not components:
        # If no meaningful components, use domain name
        domain = parsed.netloc.split('.')
        if len(domain) > 1:
            components = [domain[-2]]  # Use the main part of domain (e.g., 'example' from 'example.com')
    
    # Take first 2-3 components if available
    keywords = components[:min(3, len(components))]
    
    if not keywords:
        # Fall back to random if no keywords available
        return generate_random_code(length)
    
    # Join keywords, truncate, and add random chars to ensure uniqueness
    code = ''.join(keywords)[:length-2]
    # Add 2 random characters to ensure uniqueness
    code += ''.join(random.choices(string.ascii_lowercase + string.digits, k=length-len(code)))
    
    return code.lower()

def generate_random_code(length=6):
    """Generates a random short URL code as fallback"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('original_url')
    
    # Generate a short code based on keywords
    short_code = extract_keywords(original_url)
    
    # Check if short_code already exists and generate a new one if needed
    while URL.query.filter_by(short_url=short_code).first():
        # If exists, add more random characters
        short_code = extract_keywords(original_url) + ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))
    
    short_url = request.host_url + short_code

    # Create a new URL object and add it to the database
    new_url = URL(original_url=original_url, short_url=short_code)
    db.session.add(new_url)
    db.session.commit()

    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    """Redirects to the original URL if the short code exists"""
    url_entry = URL.query.filter_by(short_url=short_code).first()
    if url_entry:
        return redirect(url_entry.original_url)
    return render_template('error.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)