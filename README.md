# image-croppping gui

  * currently
    - displays a black image
    - can draw a green box while dragging

  * issues
    - keeps drawing box as it's dragged (something with callback)

  * suggests
    - instead of dragging size of rectangle, code so box is created around the clicked area

  1. Reqs
    1. load image from disk
    2. display image
    2. draw a box on clicked region (or draggable/resizeable box)
    3. add option(key) to clear box (and retry)
    4. add cropping function
    3. resize region (hardcoded size, but eventually a cmd line arg or text box input to specify size)
    4. display cropped region
    5. prompt approval or discard
    6. if approved, store to disk (default folder for now)
    7. if discard, repeat from #2
    8. add function to exit (q to quit)
    