import re

lst_to_sort = ['1. Introduction', '10. Expense Tracker  Array Methods & Local Storage', '11. Music Player  HTML5 Audio API', '12. Infinite Scroll Posts  Fetch, AsyncAwait, CSS Loader', '13. Typing Game  DOM, Intervals, Events', '14. Speech Text Reader  Speech Synthesis', '15. Memory Cards  CSS Effects, Local Storage', '16. Lyrics Search App  Fetch, Pagination, Lyrics.ovh API', '17. Relaxer App  CSS Animations, setTimeout', '18. Breakout Game  HTML5 Canvas API', '19. New Year Countdown  DOM, Date & Time', '2. Form Validator  Intro Project', '20. Sortable List  Drag & Drop API', '21. Speak Number Guessing Game  Speech Recognition', '3. Movie Seat Booking  DOM & Local Storage', '4. Custom Video Player  HTML5 Video API', '5. Exchange Rate Calculator  Fetch & JSON Intro', 
'6. DOM Array Methods  forEach, map, filter, sort, reduce', '7. Menu Slider & Modal  DOM & CSS', '8. Hangman Game  DOM, SVG, Events', '9. Meal Finder  Fetch & MealDB API']

def print_list(lst):
  for item in lst:
    print(item)

# def sort(lst):
#   return sorted(lst, key=lambda x: int(x[0]))

def sort_list(unsorted_list):
  lst = []
  sorted_list = []
  for item in unsorted_list:
    item_num, item_name = item.split('.', 1)
    lst.append([item_num, item_name])

  lst = sorted(lst, key=lambda x: int(x[0]))
  for item in lst:
    sorted_list.append(item[0]+"."+item[1])
  
  return sorted_list

# sorted_list = []
# lst = []
# for item in lst_to_sort:
#   item_num, item_name = item.split('.', 1)
#   lst.append([item_num, item_name])

# lst = sort(lst)
# for item in lst:
#   sorted_list.append(item[0]+"."+item[1])
  

# print("***************** before sort *****************")
# print_list(lst_to_sort)
# # sorted_lst = sort(lst)
# print("***************** sorted *****************")
# print_list(sort_list(lst_to_sort))
  
re_srt = "0. Introduction"
if re.match(r"(^[0-9]+\.)+", re_srt):
  print("Yes")
else: print("No")


  


