import xml.etree.ElementTree as xml
import os
import re
import tqdm

VIDEOS_EXTENSIONS = ['.mp4', '.mkv', '.avi', '.flv', '.mov', '.wmv', '.vob',
'.mpg','.3gp', '.m4v']		#List of extensions to be checked.

check_subdirectories = False		#Set false to get files only from cwd.

class Playlist:
	"""Build xml playlist."""
	
	def __init__(self):
	#Defines basic tree structure.
		self.playlist = xml.Element('playlist')
		self.tree = xml.ElementTree(self.playlist)
		self.playlist.set('xmlns','http://xspf.org/ns/0/')
		self.playlist.set('xmlns:vlc','http://www.videolan.org/vlc/playlist/ns/0/')
		self.playlist.set('version', '1')

		self.title = xml.Element('title')
		self.playlist.append(self.title)
		self.title.text = 'Playlist'

		self.trackList = xml.Element('trackList')
		self.playlist.append(self.trackList)

	def add_track(self, path):
	#Add tracks to xml tree (within trackList).
		track = xml.Element('track')
		location = xml.Element('location')
		location.text = path
		track.append(location)
		self.trackList.append(track)
	
	def get_playlist(self):
	#Return complete playlist with tracks.
		return self.playlist

class Videos:
	"""Manage files (videos) to be added to the playlist."""
	def __init__(self):
		pass

	def remove_nonvideo_files(self,file_list):
	#Removes files whose extension is not mentioned in VIDEOS_EXTENSIONS from list of files.
		for index,file_name in enumerate(file_list[:]):
			#if file_name.endswith(tuple(VIDEOS_EXTENSIONS)) or file_name.endswith(tuple(VIDEOS_EXTENSIONS.upper())) :
			if file_name.endswith(tuple(VIDEOS_EXTENSIONS)) or file_name.endswith(tuple(ext.upper() for ext in VIDEOS_EXTENSIONS)):
				pass
			else:
				file_list.remove(file_name)
		return file_list
	
	def edit_paths(self, video_files):
	#Add path and prefix to files as required in vlc playlist file. 
		for index in range(len(video_files)):
			video_files[index] =( 
			'file:///' + os.path.join(video_files[index])).replace('\\','/')
		return video_files
	
	def get_videos(self):
		#Returns list of video files in the directory.
		
		if check_subdirectories == True:
			pathlist = [os.getcwd()]	#List of all directories to be scanned.
			for root, dirs, files in os.walk(os.getcwd()):
				for name in dirs:
						subdir_path = os.path.join(root, name)
						if subdir_path.find('\.') != -1:	#Excludes hidden directories.
							pass
						else:
							pathlist.append(subdir_path)
							
			videos = []
			#Loops through files of root directory and every subdirectory.
			for path in pathlist:
				all_files = os.listdir(path)
				for f in self.remove_nonvideo_files(all_files):
					location = path+ '\\' + f
					videos.append(location)
			return videos
			
		else:
			videos = []
			all_files = os.listdir()
			for f in self.remove_nonvideo_files(all_files):
					location = os.getcwd() + '\\' + f
					videos.append(location)
			return videos

	def sort_list(self, unsorted_list):
		lst = []
		for item in unsorted_list:
				# Use a regular expression to find the split character
				split_char = re.search(r'[^\d][\d]*(?=\D)', item).group()

				# Split the element into the element number and element name
				item_num, item_name = item.split(split_char, 1)
				lst.append([int(item_num), item_num,split_char, item_name])
		# Sort the list by element number
		lst.sort(key=lambda x: int(x[0]))
		# Build the sorted list by combining the element number and element name
		sorted_list = [f"{item[1]}{item[2]}{item[3]}" for item in lst]
		return sorted_list
	
	def remove_non_numeric_elements(self, lst):
		return [item for item in lst if item[0].isdigit()]

def course_playlist_create(course_name):
	
	playlist = Playlist()
	videos = Videos()

	# get the names of all the subdirectories in the courses folder and pass them to the 
	# base_path = os.path.join("E:\\","Courses", "Algorithms  Data Structures","The Coding Interview Bootcamp Algorithms  Data Structures")
	base_path = os.path.join("E:\\","Courses", "Web Development",course_name)
	course_name = base_path.split('\\')[-1]
	playlist.title.text = course_name

	# Sort the subdirectories in the order of their numbers and remove any non-numeric elements
	dirTree = videos.sort_list(videos.remove_non_numeric_elements(next(os.walk(base_path))[1]))
	video_paths = []

	# Iterate through each subdirectory and add the sorted video file paths to the video_paths list
	for sub_dir in dirTree:
		current_dir = os.path.join(base_path, sub_dir)
		# Get a list of files in the current directory that have a valid video file extension
		files = [file for file in os.listdir(current_dir) if any(file.endswith(ext) for ext in VIDEOS_EXTENSIONS)]
		# Sort the list of files by their element number
		sorted_files = videos.sort_list(files)
		# Add the sorted file paths to the video_paths list
		video_paths.extend([os.path.join(current_dir, file) for file in sorted_files])

	# Add each video file path to the playlist
	for path in video_paths:
		playlist.add_track(path)
	
	# Generate the playlist XML and write it to a file
	playlist_xml = playlist.get_playlist()
	with open(f'Output2\{course_name}.xspf','w') as mf:
		mf.write(xml.tostring(playlist_xml).decode('utf-8'))
	
if __name__ == '__main__':
		courses_dir = os.path.join("E:\\","Courses", "Web Development")
		courses = [course for course in os.listdir(courses_dir) if os.path.isdir(os.path.join(courses_dir, course))]
		for course in courses:
			course_playlist_create(course)

'''
playlist(ROOT)
	title /title
	trackList
		track
			location file:///path /location
			title				  /title
			image				  /image
			duration			  /duration
		/track
	/tracklist
/playlist
'''
