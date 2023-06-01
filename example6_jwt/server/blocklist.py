"""
blocklist.py

This file just contains the blocklist of the JWT tokens. It will be imported by
app and the logout resource so that tokens can be added to the blocklist when the
user logs out.

Use database instead:
https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking.html 
"""

BLOCKLIST = set()