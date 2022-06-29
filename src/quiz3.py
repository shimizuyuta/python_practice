scores = {
  '国語': 87, '数学': 86, '英語': 70, '理科': 73, '社会': 80
}

def three_subject_avg(scores):
  score = 0
  for key,value in scores.items():
    # if key == "理科":
    #   break
    if key in ['国語','数学','英語']:
      score += value
  return score / 3

result = three_subject_avg(scores)
print(result)
