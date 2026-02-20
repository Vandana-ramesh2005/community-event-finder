from flask import Flask, render_template, request

app = Flask(__name__)

# Event Data
events = [
    {"name": "Rock Concert", "date": "March 10", "location": "City Hall", "category": "Music"},
    {"name": "Football Match", "date": "March 15", "location": "Stadium", "category": "Sports"},
    {"name": "AI Conference", "date": "March 20", "location": "Tech Park", "category": "Tech"},
    {"name": "Jazz Night", "date": "March 22", "location": "Downtown Club", "category": "Music"},
    {"name": "Basketball Tournament", "date": "March 25", "location": "Community Arena", "category": "Sports"},
    {"name": "Startup Meetup", "date": "March 28", "location": "Innovation Hub", "category": "Tech"},
]

@app.route("/")
def home():
    selected_category = request.args.get("category")

    if selected_category:
        filtered_events = [event for event in events if event["category"] == selected_category]
    else:
        filtered_events = events

    return render_template("index.html", events=filtered_events)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)