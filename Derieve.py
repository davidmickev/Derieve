# Dependencies
from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
import requests
import re
from googlesearch import search 
import random
from fake_useragent import UserAgent

Derieve = Flask(__name__)

# Route to /Index or next "action"
@Derieve.route('/')

#define app functionality
def index():
    
    ua = UserAgent()
    final = []
    oi = int(random.randint(0,300))

    # defining if try statements dont work for some reason
    text = "You probably got blocked"
    #soup = "error"

    try:
        for j in search("Consciousness", tld="co.in", lang='en', num = 1, start = oi, stop = 2, pause=8):
            #print("Going to page: {} ".format(oi))
             
            page = requests.get(f'{j}',{"User-Agent": ua.random})
            #page = requests.get(f'{"https://www.popularmechanics.com/science/a34496675/consciousness-electromagnetic-theory/"}',{"User-Agent": ua.random})
            soup = BeautifulSoup(page.content, 'html.parser')
            print("Finished soup request")
    except:
        print("Error, Probably Blocked by Google")
        return render_template("index.html", text = "Probably blocked by google")

    try:
        print("OK")
        text = soup.text[700:10000]
        parsed = text.split(".")

        for result in parsed:
            if result.find("onscious") > 0 and len(result) > 5:
                print(result)
                regex = re.compile('(\[+)\w\d(\])|[()[\]{}]|[\d]|[@#%^""?//?]')
                final.append(re.sub(regex," ",result))
                print(final)
                if len(final) > 6: continue

        return render_template("index.html", text = final)

    except:
        return render_template("index.html", text = "Probably blocked by browser, Check error code under inspection tools and try agian. Unable to parse text for display.")


    return render_template("index.html", text = text)

Derieve.run()