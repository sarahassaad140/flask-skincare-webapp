# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:33:31 2025

@author: User
"""

# create_db.py

from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
