The Scene Change Detector(SCD) module is a content-aware(compares each frame sequentially looking for changes in content, useful for detecting fast cuts between video scenes, although slower to process)
Python-OpenCV tool which analyzes a video, looking for scene changes or cuts. The output timecodes can then be used with another tool (e.g. mkvmerge, ffmpeg, OpenCV) to extract frames, which is our ROI. A frame-by-frame analysis can also be generated for a video,
to help with determining optimal threshold values or detecting patterns/other analysis methods for a particular video.

The Optical Character Recognition(OCR) module is an implementation of Py-tesseract, an OCR tool for python.
That is, it will recognize and "read" the text embedded in images. Python-tesseract is a python wrapper for Google's Tesseract-OCR.

Scripts:
1. auto.py - simple script to automate the execution of SCD and OCR modules sequentially for the same video.
2. ocr.py - reads "text" embedded in image.
3. scd.py - detects scene changes and outputs time-stamps and frame numbers(CSV format).

Dependencies:
1. OpenCv (python).
2. PyTesseract (python).
3. PySceneDetect (python and terminal).
4. PIL (python).

Usage:
1. Auto (use this only)
  - python auto.py -i "input video path" -t "threshold value"
  - Note:
      - default value of threshold is 5.
      - user is expected to analyse the stats file and determine a suitable threshold value and re-run the code.
      - we are working on automating this process as well. (coming soon...)
      
2. OCR
  - python ocr.py -i "input image path"
  
3. SCD
  - scenedetect -i "input video path" -d content -co scenes.csv -s stats.csv -df 4
  - options:
      - d: content/threshold (2 types of detectors).
      - co: CSV output path for time-stamps.
      - s: CSV output path for frame-by-frame statistics.
      - df: Down-sampling factor for faster processing.
