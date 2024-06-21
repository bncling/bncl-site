import os 
import shutil

SYLLABUS_PATH = "/Users/benclingenpeel/Desktop/GW/Summer 2024/1231/Syllabus/1231_Syllabus_Summer_24.pdf"
WEB_SYLLABUS_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents/GW1231_summer_24_syllabus.pdf"

BIRD_PATH = "/Users/benclingenpeel/Desktop/Projects/Bird/birdMap.html"
WEB_BIRD_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/birdMap.html"

NOTES_PATH = "/Users/benclingenpeel/Desktop/GW/Summer 2024/1231/Notes/to_upload.pdf"
WEB_NOTES_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents/1231_summer_24_notes.pdf"

# copy things over
shutil.copy(SYLLABUS_PATH, WEB_SYLLABUS_PATH)
shutil.copy(BIRD_PATH, WEB_BIRD_PATH)
shutil.copy(NOTES_PATH, WEB_NOTES_PATH)

# set the front matter on the bird map
with open(WEB_BIRD_PATH,'r') as contents:
      save = contents.read()
with open(WEB_BIRD_PATH,'w') as contents:
      contents.write("---\nlayout: wrapper\ntitle: Bird Map\n---\n")
with open(WEB_BIRD_PATH, 'a') as contents:
      contents.write(save)

print("Successfully updated files!")

