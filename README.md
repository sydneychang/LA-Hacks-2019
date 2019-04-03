# LA-Hacks-2019

Medical diagnostic tool created by Karen Cavicchio, Ed Yeow, and Sydney Chang.

README.txt

It's the REVENGE OF THE ITCH!

Ever wondered where your Aunt Lorraine keeps getting these strange rashes that 
she puts in the family photo album every week?
No? Well, send this site to her so she can find out and stop showing you!

Disclaimer:
This tool is NOT accurate as a medical diagnosis. No actual doctors worked on this project.
(Although my mom, who's a doctor, was very amused.) If you have a rash, GO SEE A DOCTOR.
Failing that, read our sarcastic responses and suffer in your itchy state.

Featuring: 
Actual advice from (former) pre-med students and 
second hand doctor's instructions from people with first hand experience
dealing with all kinds of lovely skin disorders!

Repo instructions:
to run locally:
    git clone into the Repo
    authenticate with your Google service account key
    pip install -r requirements.txt
    python3 main.py
    visit http://127.0.0.1:5000/ to see what your weird rash is!

publicly hosted site coming soon!

Methodology and Dev Process:

Using: Google AutoML API (Ed and Sydney)

This demonstration uses a relatively small training dataset of 200+ images
(because honestly, we could only process so many pictures of nasty rashes
in the span of 36 hours), which we input into Google's AutoML 
machine learning engine, and use to analyze your rash (or bunny picture, or 
desert rocks image) and diagnose the cause.

Using: Python3, Flask, and Jinja (Karen)

Flask is really convenient to use! Our entire project is done in Python, 
using Flask to serve our web app and a Jinja template to render it. I had never
used Flask or Jinja before, although Python is nothing new. I also used 
json objects and files to store and share data.

Using: Jinja, HTML, and CSS with Bootstrap (Sydney)

Sydney, our resident Bootstrap expert, did our CSS styling to make our web app 
pretty (as pretty as you can get when you're looking at pictures of people's rashes)
and more consistent across platforms.

No Longer Using: Webapp2 and Google's dev_appserver.py (Karen)

As I learned (after a couple hours of troubleshooting and stumping Google's engineers)
dev_appserver.py only supports Python 2 usage, while Google's other APIs require
Python 3. Due to this discrepancy, we converted entirely to using Flask to serve 
our web app. 

No Longer Using: Google Cloud Shell (Karen)

We also developed partially on Google's Cloud Shell, but our main issue arose with the
drastic latency caused by sending single keystrokes over the hackathon's spotty wifi.

Other Related APIs to Consider:
Google Cloud Healthcare API - Google is working on something which will most probably
far outstrip the work we've done here. We wanted to try and use it, but Healthcare is
still in testing, and we needed to apply for permission to use it.
Google Cloud Vision API - Google's pre-trained ML machines, which can recognize general
images. We found that Cloud Vision is sophisticated enough to recognize when images
are medical in nature, (giving it a 'medical' confidence score). We could have 
added more functionality to our app by also running input images through Cloud Vision,
but this is outside the intended use of the application, and the added overhead of
making a second machine learning analysis request did not warrant the extra functionality,
especially when contending with the inconsistent wifi provided at the hackathon.

Future Functionality:

We would love to implement some more features for our app, including:
- Similar detection for other skin ailments (moles, sunburn, bruises, acne, etc)
- An automatic web search for appropriate doctors in your area

README by: Karen Cavicchio
