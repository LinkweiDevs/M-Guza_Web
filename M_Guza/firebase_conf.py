from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyCL_yyulCmFXBhkVPEyG8YMEs9isq03GHQ",
    "authDomain": "m-guza.firebaseapp.com",
    "projectId": "m-guza",
    "storageBucket": "m-guza.appspot.com",
    "messagingSenderId": "1094767826078",
    "appId": "1:1094767826078:web:ab7c5e4f0a95d1ed4c578f",
    "measurementId": "G-2T8GMJ7CLN"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

