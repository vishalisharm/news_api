from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        headline = request.form['headline']
        info = request.form['info']
        link = request.form['link']

        # Validate the form data
        if not headline or not info or not link:
            return jsonify({'error': 'Missing required fields'})

        # Load the existing JSON file
        with open('data.json', 'r') as f:
            existing_news_items = json.load(f)

        # Add the new item to the JSON array
        new_news_item = {
            'headline': headline,
            'info': info,
            'link': link,
        }

        existing_news_items.append(new_news_item)

        # Save the updated JSON data
        with open('data.json', 'w') as f:
            json.dump(existing_news_items, f, indent=4)

        return jsonify({'success': True})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
