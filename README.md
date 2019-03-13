# Goals
- Flask and Jinja Template
    - Let's create a basic UI for a search box!


# Part 1
- Make sure you have the packages in `requirements.txt` installed
- Run `app.py`
- Open browser to `http://localhost:5000`, and add `/q?=University of Michigan` to the location
- Edit `app.py` and write code in `index()` function to get `answer` and `result` values
    - You will need to extract the value of `q` found in the location bar of your browser using Flask using: `request.args.get('q')`. `request` is different from `requests` library. `request` is current request that Flask receives from your browser, while `requests` library helps you make requests to external websites / API.
- Look at `templates/index.html`. Can you understand what is happening in the file?
- Instead of typing the query in the browser's address bar every time, let us make an input field that takes the question and shows the result in the same page.
    - Add a form that has an input with `name="q"`
      ```
      <form action="/" method="GET">
          <label>
              <b>Ask the Duck</b>
              <input name="q" type="text" placeholder="Start typing..." />
          </label>
          <button type="submit">Send</button>
      </form>
      ```

