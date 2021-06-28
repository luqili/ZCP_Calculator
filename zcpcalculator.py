## trans arr
def text2arr(text:str):
    text = text.replace('J', '11')
    text = text.replace('j', '11')
    text = text.replace('Q', '12')
    text = text.replace('q', '12')
    text = text.replace('K', '13')
    text = text.replace('k', '13')
    if ',' in text:
        arr = text.split(',')
        arr = [int(x.strip()) for x in arr]
        return arr
    elif '，' in text:
        arr = text.split('，')
        arr = [int(x.strip()) for x in arr]
        return arr
    elif ' ' in text:
        arr = text.split(' ')
        arr = [int(x.strip()) for x in arr]
        return arr

def sum_count(v, i, S, memo):
  if i >= len(v): return 1 if S == 0 else 0
  if (i, S) not in memo:  # <-- Check if value has not been calculated.
    count = sum_count(v, i + 1, S, memo)
    count += sum_count(v, i + 1, S - v[i], memo)
    memo[(i, S)] = count  # <-- Memoize calculated result.
  return memo[(i, S)]     # <-- Return memoized value.


def get_subset(v, S, memo):
  subset = []
  for i, x in enumerate(v):
    # Check if there is still a solution if we include v[i]
    if sum_count(v, i + 1, S - x, memo) > 0:
      subset.append(x)
      S -= x
  return subset



def main():
	var = input("张昌蒲计算器启动，请输入计算内容: ")
	arr = text2arr(var)
	halfsum = round(sum(arr, 10) / 2)
	for curr_sum in range(halfsum, 0, -1):
  		memo = dict()
  		if sum_count(arr, 0, curr_sum, memo) > 1:
  			subset1 = get_subset(arr, curr_sum, memo)
  			remaining = [x for x in arr if x not in subset1]
  			memo2 = dict()
  			if sum_count(remaining, 0, curr_sum, memo2) > 0:
  				subset2 = get_subset(remaining, curr_sum, memo2)
  				print(subset1 , subset2)

if __name__ == "__main__":
    main()
