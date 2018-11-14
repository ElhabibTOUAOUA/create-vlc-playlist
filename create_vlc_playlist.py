import xml.etree.ElementTree as xml
import os

ext_list = ('.mp4', '.mkv', '.avi', '.flv', '.mov', '.wmv', '.vob',
'.mpg','.3gp', '.m4v')		#List of extensions to be checked.

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
	#Removes files whose extension is not mentioned in ext_list from list of files.
		for index,file_name in enumerate(file_list[:]):
			if file_name.endswith(ext_list):
				pass
			else:
				file_list.remove(file_name)
		return file_list
	
	def add_paths(self, video_files):
	#Add path and prefix to files as required in vlc playlist file. 
		for index in range(len(video_files)):
			video_files[index] =( 
			'file:///' + os.path.join(os.getcwd(), video_files[index])).replace('\\','/')
		return video_files
	
	def get_videos(self):
	#Returns list of video files in the directory.
		all_files = os.listdir()
		videos = self.remove_nonvideo_files(all_files)
		return videos


def main():
	playlist = Playlist()
	videos = Videos()
	
	video_files = videos.get_videos()
	video_paths = videos.add_paths(video_files)
	
	for path in video_paths:
		playlist.add_track(path)
	
	playlist_xml = playlist.get_playlist()
	with open('songs.xspf','w') as mf:
		mf.write(xml.tostring(playlist_xml).decode('utf-8'))
	
main()

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