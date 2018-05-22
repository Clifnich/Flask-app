from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'hi'

@app.route('/hi')
def sayhi():
  return 'say hi'

if __name__ == '__main__':
  watch_files = ['log.txt']
  app.run(port=5000,debug=True,extra_files=watch_files)
