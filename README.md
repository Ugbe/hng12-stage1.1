# About
In a desperate attempt to correct the history of this timeline, which has nothing to with the hng12-stage1 repo, but everything to do with the latter's misnomer, I have named this repo so. This is the 2nd task or the actual stage 1 (the 1th) task, a simple Number Classification API.
It is a public API that returns the following information in JSON format:
<ol>
  <li><b>My registered email address</b> for the HNG112 workspace</li>
  <li><b>The datetime of the request</b> as an ISO 8601 formatted timestamp</li>
  <li><b>The Guthub URL</b> to this repository</li>
</ol>

## Setup instructions for running locally
<ol>
  <li>Clone the repository</li>
  <code>git clone https://github.com/Ugbe/hng12-stage1.git
cd hng12-stage1</code>
  <li>Install dependencies</li>
  <code>pip install django</code>
  <li>Run migrations</li>
  <code>cd stageone
python manage.py migrate</code>
  <li>Start development server</li>
  <code>python manage.py runserver</code>
  <li>Navigate to the right endpoint, shown below</li>
</ol>

## API Endpoint URL
GET /api/service

or to test from the web: https://asery.pythonanywhere.com/api/service

### Response Format
    {
      "email": "ugbedeojoabba@gmail.com",
      "current_datetime": "2023-09-08T15:30:45Z",
      "github_url": "https://github.com/Ugbe/hng12-stage1"
      }

### Example Usage:
    curl http://localhost:8000/api/service
  or visit in your browser:
    http://localhost:8000/api/service
## Note:
If you want to hire competent python backend engineers, [this](https://hng.tech/hire/python-developers) is the place to go!

