import os
home_path = os.getcwd()
project_folder = home_path + "/project_folder"

os.mkdir(project_folder)
os.mkdir(project_folder + "/images")
os.mkdir(project_folder + "/pages")
os.mkdir(project_folder + "/styles")

f = open(project_folder +"/index.html","w+")
f.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n<title>Title of the document</title>\n<link rel='stylesheet' href='styles/main.css'>\n<script type='text/javascript' src='styles/main.js'></script>\n</head>\n<body>\n<button onclick='working()'>JS</button>\nContent of the document......\n</body>\n</html>")