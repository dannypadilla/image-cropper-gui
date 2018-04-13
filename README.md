# image-croppping gui

  * dependence
    - python3.6+ (use brew to install python3 - otherwise opencv might not be able to find python3)
    - opencv3.3+ (brew install opencv maybe?) [Linky](https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/)
    - numpy1.14+ (pip3 install numpy)

  * docs
    - [Start Here](https://docs.opencv.org/3.3.0/dc/d4d/tutorial_py_table_of_contents_gui.html "Start with this")
    - [Where code is from](https://docs.opencv.org/3.3.0/db/d5b/tutorial_py_mouse_handling.html)
    - [OpenCV/Python tutorials](https://docs.opencv.org/3.3.0/d6/d00/tutorial_py_root.html "Really good")
    - [OpenCV Python Docs](https://docs.opencv.org/3.3.0/index.html)

## state

  * currently
    - displays a black image
    - can draw a green box while dragging
    - Save image with option(key) 's'
    - Quit with option(key) 'q'
    - able to reselect crop region
    - display cropped region in separate window

  * issues
    - breaking out of cropped region window

  * suggests
    - N/A

  * reqs
    1. load image from disk
    2. display image
    3. draw a box on clicked region (or draggable/resizeable box)
    4. add option(key) to clear box (and retry), save, exit/quit
    5. add cropping and save function
    6. resize region (hardcoded size, but eventually a cmd line arg or text box input to specify size)
    7. prompt approval or discard
    8. if approved, store to disk (default folder for now)
    9. if discard, repeat from #2
    10. add function to exit (q to quit)
    
