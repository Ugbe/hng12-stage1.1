# About
In a desperate attempt to correct the history of this timeline 😂, which has nothing to with the hng12-stage1 repo, but everything to do with the latter's misnomer, I have named this repo so. This is the 2nd task or the actual stage 1 (the 1th) task, a simple Number Classification API.
It is a public API that takes a number from the GET request and returns some information about it, e.g.
<ol>
  <li>its primality</li>
  <li>its polarity</li>
  <li>a fun fact about the number (gotten from [numbersapi](numbersapi.com])</li>
</ol>
in JSON format

## Setup instructions for running locally
<ol>
  <li>Clone the repository</li>
  <code>git clone https://github.com/Ugbe/hng12-stage1.1.git
cd hng12-stage1.1</code>
  <li>Install dependencies</li>
  <code>pip install django, requests</code>
  <li>Run migrations</li>
  <code>cd stageone
python manage.py migrate</code>
  <li>Start development server</li>
  <code>python manage.py runserver</code>
  <li>Navigate to the right endpoint, shown below</li>
</ol>

## API Endpoint URL
GET /api/service

or to test from the web: https://asery.pythonanywhere.com/api/classify-number?number=x
where x is a placeholder for the number you wish to play with.

### Response Format
    {
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
      }

### Example Usage:
    curl http://localhost:8000/api/classify-number?number=371
  or visit in your browser:
    http://localhost:8000/api/classify-number?number=371
## Note:
If you want to hire competent python backend engineers, [this](https://hng.tech/hire/python-developers) is the place to go!
### Side-note:
The primality checking function I used was pretty cool, hehe. Never knew it could be done that way until today, courtesy of [GeeksfoGeeks](https://www.geeksforgeeks.org/check-for-prime-number/).

