import re

def sort_list(unsorted_list):
  # Find the split character in the first element of the list
  split_char = re.search(r'[^\d]', unsorted_list[0]).group()
  
  # Split the list elements into a list of lists, where each inner list
  # contains the element number and element name
  # lst = [[int(re.match(r'\d+', item).group()), item.split(split_char, 1)[1].strip()] for item in unsorted_list]
  lst = [[int(item.split(split_char, 1)[0]), item.split(split_char, 1)[0] ,item.split(split_char, 1)[1].strip()] for item in unsorted_list]

  # Sort the list by element number
  lst.sort(key=lambda x: x[0])

  # Build the sorted list by combining the element number and element name
  sorted_list = [f"{item[1]}{split_char} {item[2]}" if split_char != ' ' else f"{item[1]}{split_char}{item[2]}" for item in lst]
  
  return sorted_list

def printList(lst):
  for item in lst:
    print(item)

def remove_non_numeric_elements(lst):
  return [item for item in lst if item[0].isdigit()]

def sort_list2(unsorted_list):
  lst = []
  for item in unsorted_list:
      # Use a regular expression to find the split character
      split_char = re.search(r'[^\d][\d]*(?=\D)', item).group()
      # Split the element into the element number and element name
      item_num, item_name = item.split(split_char, 1)
      lst.append([item_num, item_name])
  # Sort the list by element number
  lst.sort(key=lambda x: int(x[0]))
  # Build the sorted list by combining the element number and element name
  sorted_list = [f"{item[0]}{split_char}{item[1]}" for item in lst]
  return sorted_list

lst_to_sort = ['001. Introduction', '010. Expense Tracker  Array Methods & Local Storage', '011. Music Player  HTML5 Audio API', '012. Infinite Scroll Posts  Fetch, AsyncAwait, CSS Loader', '013. Typing Game  DOM, Intervals, Events', '014. Speech Text Reader  Speech Synthesis', '015. Memory Cards  CSS Effects, Local Storage', '016. Lyrics Search App  Fetch, Pagination, Lyrics.ovh API', '017. Relaxer App  CSS Animations, setTimeout', '018. Breakout Game  HTML5 Canvas API', '019. New Year Countdown  DOM, Date & Time', '002. Form Validator  Intro Project', '020. Sortable List  Drag & Drop API', '021. Speak Number Guessing Game  Speech Recognition', '003. Movie Seat Booking  DOM & Local Storage', '004. Custom Video Player  HTML5 Video API', '005. Exchange Rate Calculator  Fetch & JSON Intro', 
'006. DOM Array Methods  forEach, map, filter, sort, reduce', '007. Menu Slider & Modal  DOM & CSS', '008. Hangman Game  DOM, SVG, Events', '009. Meal Finder  Fetch & MealDB API']

lst_to_sort2 = ['1 Introduction', '10 Expense Tracker  Array Methods & Local Storage', '11 Music Player  HTML5 Audio API', '12 Infinite Scroll Posts  Fetch, AsyncAwait, CSS Loader', '13 Typing Game  DOM, Intervals, Events', '14 Speech Text Reader  Speech Synthesis', '15 Memory Cards  CSS Effects, Local Storage', '16 Lyrics Search App  Fetch, Pagination, Lyrics.ovh API', '17 Relaxer App  CSS Animations, setTimeout', '18 Breakout Game  HTML5 Canvas API', '19 New Year Countdown  DOM, Date & Time', '2 Form Validator  Intro Project', '20 Sortable List  Drag & Drop API', '21 Speak Number Guessing Game  Speech Recognition', '3 Movie Seat Booking  DOM & Local Storage', '4 Custom Video Player  HTML5 Video API', '5 Exchange Rate Calculator  Fetch & JSON Intro', 
'6 DOM Array Methods  forEach, map, filter, sort, reduce', '7 Menu Slider & Modal  DOM & CSS', '8 Hangman Game  DOM, SVG, Events', '9 Meal Finder  Fetch & MealDB API']

lst_to_sort3 = ['1 - Introduction', '10 - Expense Tracker  Array Methods & Local Storage', '11 - Music Player  HTML5 Audio API', '12 - Infinite Scroll Posts  Fetch, AsyncAwait, CSS Loader', '13 - Typing Game  DOM, Intervals, Events', '14 - Speech Text Reader  Speech Synthesis', '15 - Memory Cards  CSS Effects, Local Storage', '16 - Lyrics Search App  Fetch, Pagination, Lyrics.ovh API', '17 - Relaxer App  CSS Animations, setTimeout', '18 - Breakout Game  HTML5 Canvas API', '19 - New Year Countdown  DOM, Date & Time', '2 - Form Validator  Intro Project', '20 - Sortable List  Drag & Drop API', '21 - Speak Number Guessing Game  Speech Recognition', '3 - Movie Seat Booking  DOM & Local Storage', '4 - Custom Video Player  HTML5 Video API', '5 - Exchange Rate Calculator  Fetch & JSON Intro', 
'6 - DOM Array Methods  forEach, map, filter, sort, reduce', '7 - Menu Slider & Modal  DOM & CSS', '8 - Hangman Game  DOM, SVG, Events', '9 - Meal Finder  Fetch & MealDB API']

lst_to_sort4 = ['003-Section_Intro_Installing_and_Exploring_Node.js.mkv', '004-Installing_Node.js_and_Visual_Studio_Code.mkv', '005-What_is_Node.js.mkv', '006-Why_Should_I_Use_Node.js.mkv', '007-Your_First_Node.js_Script.mkv', '008-Global_Object.mkv', '009-Modules.mkv', '010-File_System.mkv', '011-Path_Module.mkv', '012-OS_Module.mkv', '013-Events.mkv', '014-HTTP.mkv', '015-Readline.mkv', '016-Stream.mkv', '017-Buffer.mkv', '018-URL_Module.mkv', '019-Query_String_Module.mkv', '020-File_Upload.mkv', '021-Express.mkv', '022-Express_Routing.mkv', '023-Express_Middleware.mkv', '024-Template_Engine.mkv', '025-Express_Validator.mkv', '026-Express_Message.mkv', '027-Express_Session.mkv', '028-Connect_Flash.mkv', '029-Express_MongoDB.mkv', '030-Express_Mongoose.mkv', '031-Express_Mongoose_CRUD.mkv', '032-Express_Mongoose_Pagination.mkv', '033-Express_Mongoose_Relationships.mkv', '034-Express_Mongoose_Authentication.mkv', '035-Express_Mongoose_Passport_Local_Strategy.mkv', '036-Express_Mongoose_Passport_Google_Strategy.mkv']

printList(sort_list2(lst_to_sort))

