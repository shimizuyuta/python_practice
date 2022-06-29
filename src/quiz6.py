import re 

with open('./data/app.log', encoding='utf-8') as f:
  logs = [x.strip() for x in f.readlines()]

for log in logs:
  m = re.match(
    r'\d{4}-\d{2}-\d{2} 22:\d{2}:\d{2},\d{3} \[(WARNING|ERROR)\]',
    log)
  if m:
    print(log)